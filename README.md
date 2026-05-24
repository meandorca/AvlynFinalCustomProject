# Animal Adoption Tracker

## Project Overview

Animal Adoption Tracker is a Flask web application that allows users to browse different animals available for adoption, create accounts, log in, and save their favorite animals.

The website displays multiple animals on the homepage, and each animal has its own individual profile page with more detailed information and images. Users can create an account to access the favorites feature, which allows them to save and remove animals from their personal favorites list.

I chose to build this project because I wanted to create something interactive, visually appealing, and easy to use while also practicing Flask routing, databases, user authentication, templates, and relationships between database models. I also love animals, and I hope you do too!


# How the Application Works

When a user first visits the website, they are taken to the homepage where they can browse all available animals currently stored in the database.

Each animal card includes:
- The animal’s name
- Species
- Age
- Description
- An image
- A button to save the animal to favorites

Users can click on an animal’s name to open a separate detail page for that specific animal.

If a user wants to save animals to their favorites list, they must first create an account using the register page. After registering, they can log in through the login page.

Once logged in:
- The user can save animals to favorites
- View their favorites page
- Remove animals from favorites
- Log out of their account

If a user attempts to save a favorite without being logged in, the application displays a popup message asking them to log in or create an account first.


# Main Features

- Dynamic homepage displaying animals from a database
- Individual animal detail pages
- User registration system
- User login and logout functionality
- Favorites system for logged in users
- Ability to remove favorites
- Database integration using Flask-SQLAlchemy
- Styled interface using custom CSS
- Local image storage for animal photos

# Database Model Explanation

This project uses SQLite as the database system along with Flask-SQLAlchemy for database management. The database file is automatically created and stored locally as animals.db

## User Model

The User model stores account information for each user.

Properties:
- id
- username
- password

## Animal Model

The Animal model stores information about each animal profile displayed on the website.

Properties:
- id
- name
- species
- age
- description
- image_url

## Favorites Relationship

The application also includes a favorites relationship between users and animals.

This allows:
- One user to save multiple animals
- One animal to be saved by multiple users

This relationship is managed using a separate association table inside the database.

# How To Run The Project

## 1. Download or Clone the Repository

Clone the GitHub repository using:

git clone https://github.com/meandorca/AvlynFinalCustomProject

Or download the ZIP file directly from GitHub and extract it.

## 2. Open the Project Folder

Open the project folder in:
- VS Code
- Terminal
- Or another Python IDE

## 3. Install Required Packages

Make sure Python is installed on your computer. Then install all required packages at once using the project's requirements file:

pip install -r requirements.txt

(Mac users may need to use pip3 install -r requirements.txt)

## 4. Run the Application

Start the Flask server with:

python3 app.py

or on some systems:

python app.py

## 5. Open the Website

After running the server, open your browser and go to:

http://127.0.0.1:5000/

Google Chrome is recommended for the best performance.

# Technologies Used

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- HTML
- CSS
- Jinja Templates



Thank you for showing interest in my project. Enjoy ! 