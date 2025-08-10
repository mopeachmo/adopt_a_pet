from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# import models so tables are registered
from models import Species, Pet, User, AdoptionRequest, Comment

# import routes AFTER app & db exist
import routes

if __name__ == '__main__':
    app.run(debug=True)
