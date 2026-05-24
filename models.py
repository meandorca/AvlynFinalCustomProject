from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

favorites = db.Table(
    'favorites',

    db.Column(
        'user_id',
        db.Integer,
        db.ForeignKey('user.id')
    ),

    db.Column(
        'animal_id',
        db.Integer,
        db.ForeignKey('animal.id')
    )
)


class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(100),
        nullable=False
    )

    saved_animals = db.relationship(
        'Animal',
        secondary=favorites,
        backref='users'
    )


class Animal(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(db.String(100))

    species = db.Column(db.String(50))

    age = db.Column(db.String(50))

    description = db.Column(db.Text)

    image_url = db.Column(db.String(300))