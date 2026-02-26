# 🐾 Adopt A Pet – Flask Web Application

A full-stack web application built with Flask and SQLAlchemy that allows users to browse pets, filter by species, leave comments, and submit adoption requests.

This project demonstrates backend architecture design, relational database modelling, and server-side rendering using Flask.

---

## 📌 Features

- View latest available pets
- Filter pets by species
- View adopted pets
- Pet detail pages with comments
- Submit adoption requests
- Automatic user creation by email
- Database seed script for sample data

---

## 🛠 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2
- HTML / CSS

---

## 🏗 Project Structure
```bash
adopt_a_pet/
│
├── app.py # App configuration & database setup
├── models.py # Database models and relationships
├── routes.py # Application routes
├── add_data.py # Database seeding script
│
├── templates/ # HTML templates
├── static/ # CSS, images, uploads
│
└── site.db # SQLite database (generated)
```

The application follows separation of concerns:
- Configuration (app)
- Data model (models)
- Request handling (routes)
- Presentation layer (templates)

---

## 🗃 Database Design

### Entities

- Species
- Pet
- User
- AdoptionRequest
- Comment

### Relationships

- One-to-many: Species → Pets
- One-to-many: Pet → Comments
- One-to-many: User → AdoptionRequests
- Cascading deletes enabled

This relational structure is implemented using SQLAlchemy ORM.

---

## 🚀 Installation

Clone the repository:


```bash
git clone https://github.com/yourusername/adopt_a_pet.git
cd adopt_a_pet 
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Initialise database with seed data:
```bash
python add_data.py
```
```bash
Run the application:

python app.py
```
Open in browser:
```bash
http://127.0.0.1:5000
```


## 📚 What I Learned

- Designing relational database schemas

- Managing ORM relationships with SQLAlchemy

- Implementing CRUD operations

- Handling form submissions

- Structuring a Flask application for maintainability

- Writing seed scripts for reproducible environments

## 🔮 Future Improvements

- User authentication system

- Admin dashboard

- Image upload validation

- REST API endpoints

- Pagination

- Deployment (Render / Railway / AWS)