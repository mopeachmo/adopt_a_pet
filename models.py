from app import db
from datetime import datetime

# Create the database models
# Declaring the Species model
class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key column
    name = db.Column(db.String(40), unique=True, nullable=False) # species name column
    pets = db.relationship('Pet', backref='species', lazy='dynamic', cascade='all, delete, delete-orphan') # relationship to Pet model

# Declaring the Pet model
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key column
    name = db.Column(db.String(60), nullable=False, index=True) # pet name column
    age = db.Column(db.Integer, nullable=False) # pet age column
    breed = db.Column(db.String(60), nullable=False) # pet breed column
    description = db.Column(db.Text, nullable=True) # pet description column
    image_url = db.Column(db.String(250), nullable=True) # URL for pet image
    available = db.Column(db.Boolean, default=True, index=True) # availability status
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False) # foreign key to Species model
    comments = db.relationship('Comment', backref='pet', lazy='dynamic', cascade='all, delete, delete-orphan') # relationship to Comment model
    requests = db.relationship('AdoptionRequest', backref='pet', lazy='dynamic', cascade='all, delete, delete-orphan') # relationship to AdoptionRequest model

# Declaring the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key column
    name = db.Column(db.String(80), unique=True, nullable=False) # name column
    email = db.Column(db.String(120), unique=True, nullable=False, index=True) # email column
    requests = db.relationship('AdoptionRequest', backref='user', lazy='dynamic', cascade='all, delete, delete-orphan') # relationship to AdoptionRequest model

# Declaring the AdoptionRequest model
class AdoptionRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key column
    message = db.Column(db.Text, nullable=False) # message from user
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False) # foreign key to Pet model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # foreign key to User model
    status = db.Column(db.String(20), default='pending') # status of the request
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # timestamp of request creation

# Declaring the Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary key column
    author = db.Column(db.String(80), nullable=False) # author of the comment
    body = db.Column(db.Text, nullable=False) # comment content column
    pet_id = db.Column(db.Integer, db.ForeignKey('pet.id'), nullable=False) # foreign key to Pet model
    created_at = db.Column(db.DateTime, default=datetime.utcnow) # timestamp of comment creation
