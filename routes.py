from flask import render_template, request, redirect, url_for, abort, flash
from app import app, db
from models import Species, Pet, User, AdoptionRequest, Comment

# Define the routes for the application
@app.route('/')
def home():
    pets = Pet.query.filter_by(available=True).order_by(Pet.id.desc()).limit(12).all() # Get the latest 12 available pets
    species = Species.query.order_by(Species.name).all() # Get all species ordered by name
    return render_template('home.html', pets=pets, species=species) # Render the home page with pets and species

# Route to list all pets with optional filtering by species and search query
@app.route('/pets')
def list_pets():
    sp = request.args.get('species','').strip() # Get the species filter from query parameters
    query = Pet.query.filter_by(available=True) # Start with a query for available pets
    if sp:
        query = query.join(Species).filter(Species.name == sp) # Filter by species if provided
    pets = query.order_by(Pet.id.desc()).all() # Execute the query to get the list of pets
    species = Species.query.order_by(Species.name).all() # Get all species ordered by name
    return render_template('pets.html', pets=pets, species=species) # Render the pets page with the list of pets, species, search query, and selected species

@app.route('/pets/adopted')
def adopted_pets():
    pets = Pet.query.filter(Pet.available == False).order_by(Pet.id.desc()).all() # Get all adopted pets ordered by ID
    species = Species.query.order_by(Species.name).all() # Get all species ordered by name
    return render_template('pets.html', pets=pets, species=species) # Render the pets page with the list of all pets, species, search query, and selected species
                            
# Route to view details of a specific pet and add comments
@app.route('/pet/<int:pet_id>', methods=['GET', 'POST'])
def pet_detail(pet_id):
    pet = Pet.query.get_or_404(pet_id) # Get the pet by ID or return a 404 error if not found
    if request.method == 'POST': # Handle comment submission
        author = request.form['author'].strip() # Get the author from the form data
        body   = request.form['body'].strip() # Get the comment body from the form data
        if author and body:
            db.session.add(Comment(author=author, body=body, pet=pet)) # Create a new comment if author and body are provided
            db.session.commit()
            return redirect(url_for('pet_detail', pet_id=pet.id)) # Redirect to the pet detail page after adding the comment
    comments = pet.comments.order_by(Comment.created_at.desc()).all() # Get all comments for the pet ordered by creation date
    return render_template('pet_detail.html', pet=pet, comments=comments) # Render the pet detail page with the pet and its comments     

# Route to handle adoption requests for a specific pet
@app.route('/adopt/<int:pet_id>', methods=['GET', 'POST'])
def adopt(pet_id):
    pet = Pet.query.get_or_404(pet_id) # Get the pet by ID or return a 404 error if not found
    if request.method == 'POST': 
        name = request.form['name'].strip() # Get the name from the form data
        email = request.form['email'].strip() # Get the email from the form data
        msg = request.form.get('message', '').strip() # Get the message from the form data, default to empty string
        if not (name and email):
            abort(400) # Return a 400 error if name or email is missing
        # find or create lightweight user
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(name=name, email=email) 
            db.session.add(user)
        req = AdoptionRequest(user=user, pet=pet, message=msg)
        db.session.add(req)
        db.session.commit()
        return redirect(url_for('request_thanks', req_id=req.id)) # Redirect to thank you page after request submission
    return render_template('adopt_form.html', pet=pet) # Render the adoption form for the pet

# Route to thank the user after submitting an adoption request
@app.route('/adopt/thanks/<int:req_id>')
def request_thanks(req_id): 
    req = AdoptionRequest.query.get_or_404(req_id) # Get the adoption request by ID or return a 404 error if not found
    return render_template('adopt_thanks.html', req=req) # Render the thank you page with the adoption request details


