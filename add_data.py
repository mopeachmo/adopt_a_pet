import os
from datetime import datetime
from app import app, db
from models import Species, Pet, User, AdoptionRequest, Comment

RESET_DB = True  # Set to True to reset the database

# Directory for static pet images
STATIC_PETS_DIR = os.path.join(app.root_path, 'static', 'pets')

def run():
    with app.app_context(): # Create an application context for database operations
        if RESET_DB:
            db.drop_all()
        db.create_all()  # Create all tables

        # Add initial data --- Species ---
        dog = Species(name='Dog')
        cat = Species(name='Cat')
        rabbit = Species(name='Rabbit')
        bird = Species(name='Bird')
        db.session.add_all([dog, cat, rabbit, rabbit])
        db.session.flush()  # Flush to get IDs for relationships

        # Add initial data --- Pets ---
        pets = [
            Pet(
                name='Gabu',
                age=12,
                breed='Papillon',
                description='Friendly and house-trained.',
                image_url="/static/uploads/gabu.jpg",
                species=dog,
                available=True,
            ),
            Pet(
                name='Hansel',
                age=8,
                breed='Domestic Shorthair',
                description='Calm and cuddly.',
                image_url="/static/uploads/hansel.jpg",
                species=cat,
                available=True,
            ),
            Pet(
                name='Derek',
                age=1,
                breed='Domestic Shorthair',
                description='Curious little boy.',
                image_url="/static/uploads/derek.jpg",
                species=cat,
                available=True,
            ),
            Pet(
                name='Geoffrey',
                age=10,
                breed='Seagull',
                description='Well-mannered gentleman.',
                image_url="/static/uploads/geoffrey.jpg",
                species=bird,
                available=True,
            ),
            Pet(
                name='Saffi',
                age=8,
                breed='Labrador Retriever',
                description='Loves to hop around.',
                image_url="/static/uploads/saffi.jpg",
                species=dog,
                available=False,
            ),
            Pet(
                name='Zady',
                age=6,
                breed='Mix',
                description='Loves to play with toys.',
                image_url="/static/uploads/zady.jpg",
                species=dog,
                available=True,
            ),
            Pet(
                name='Russel',
                age=13,
                breed='',
                description='A sweet old',
                image_url="/static/uploads/russel.jpg",
                species=dog,
                available=True,
            ),
            Pet(
                name='Dodo',
                age=100,
                breed='Dodo',
                description='Extinct but still adorable.',
                image_url="/static/uploads/dodo.jpg",
                species=bird,
                available=False,
            ),
            Pet(
                name='Brownie',
                age=3,
                breed='Egyptian Goose',
                description='A friendly bird with lovery voise',
                image_url="/static/uploads/brownie.jpg",
                species=bird,
                available=True,
            ),
            Pet(
                name='Louis',
                age=4,
                breed='Terrier',
                description='A bit needy but very loving.',
                image_url="/static/uploads/louis.jpg",
                species=dog,
                available=True,
            ),
            Pet(
                name='Badeni',
                age=6,
                breed='Domestis longhair',
                description='A beautiful cat with a long coat. He lost his left eye in an accident, but still playful.',
                image_url="/static/uploads/badeni.jpg",
                species=cat,
                available=True,
            ),
        ]
        db.session.add_all(pets)

        # Add initial data --- Users ---
        users = [
            User(name='Momo', email='momo@sample.com'),
            User(name='Tom', email='tom@sample.com'),
        ]
        db.session.add_all(users)
        db.session.flush()

        # Add initial data --- Comments ---
        comments = [
            Comment(author='Visitor', body='What a cutie!', pet=pets[0]),
            Comment(author='Alex', body='Does Hansel get along with dogs?', pet=pets[1]),
        ]
        db.session.add_all(comments)

        # Add initial data --- Adoption Requests ---
        req = AdoptionRequest(
            user=users[0],
            pet=pets[0],
            message='We have a garden and can walk daily.',
            created_at=datetime.utcnow(),
        )
        db.session.add(req)

        db.session.commit()

        # Print the number of records in each table
        print(
            "Seed complete → "
            f"Species={Species.query.count()}, "
            f"Pets={Pet.query.count()}, "
            f"Users={User.query.count()}, "
            f"Requests={AdoptionRequest.query.count()}, "
            f"Comments={Comment.query.count()}"
        )

# Ensure the static directory exists
if __name__ == '__main__':
    run()