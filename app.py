from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session
)
from models import db, User, Animal

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animals.db'

app.config['SECRET_KEY'] = 'secretkey'

db.init_app(app)

with app.app_context():

    db.create_all()

    if Animal.query.count() == 0:

        animal1 = Animal(
            name="Buddy",
            species="Dog",
            age="2 years",
            description="Friendly golden retriever who loves people.",
            image_url="static/images/goldenr.jpeg"
        )

        animal2 = Animal(
            name="Luna",
            species="Cat",
            age="1 year",
            description="Playful black cat with lots of energy.",
            image_url="static/images/cat.jpeg"
        )

        animal3 = Animal(
            name="Kiwi",
            species="Bird",
            age="4 years",
            description="Very intelligent Cockatoo parrot that can mimic words.",
            image_url="static/images/cockatoo.jpeg"
        )

        animal4 = Animal(
            name="Nala",
            species="Snake",
            age="3 years",
            description="Ball python with a calm temperament.",
            image_url="static/images/ballpython.jpeg"
        )

        animal5 = Animal(
            name="Muff Pie",
            species="Rabbit",
            age="1 year",
            description="Soft white rabbit that enjoys attention.",
            image_url="static/images/whiterabbit.jpeg"
        )

        animal6 = Animal(
            name="Zazu",
            species="Bird",
            age="6 years",
            description="Large tropical Macaw with vibrant feathers.",
            image_url="static/images/macaw.jpeg"
        )

        animal7 = Animal(
        name="Pocus",
        species="Cat",
        age="2 years",
        description="Playful gray cat who loves climbing and cuddles.",
        image_url="static/images/pocuscat.jpeg"
        )

        animal8 = Animal(
            name="Rocky",
            species="Dog",
            age="4 years",
            description="Energetic husky who enjoys running and outdoor adventures.",
            image_url="static/images/rockyhusky.jpeg"
        )

        animal9 = Animal(
            name="Sunny",
            species="Bird",
            age="1 year",
            description="Bright yellow canary with a beautiful singing voice.",
            image_url="static/images/sunny.jpeg"
        )

        animal10 = Animal(
            name="Shadow",
            species="Snake",
            age="3 years",
            description="Calm white kingsnake that enjoys warm environments.",
            image_url="static/images/shadow.jpeg"
        )

        animal11 = Animal(
            name="Mochi",
            species="Rabbit",
            age="1 year",
            description="Small fluffy rabbit with a very gentle personality.",
            image_url="static/images/mochi.jpeg"
        )

        animal12 = Animal(
            name="Bella",
            species="Dog",
            age="5 years",
            description="Friendly golden retriever who loves meeting new people.",
            image_url="static/images/bella.jpeg"
        )

        animal13 = Animal(
            name="Oliver",
            species="Cat",
            age="3 years",
            description="Orange tabby cat who spends all day lounging in sunny spots.",
            image_url="static/images/oliver.jpeg"
        )

        animal14 = Animal(
            name="Hannah",
            species="Bird",
            age="2 years",
            description="Colorful parakeet that enjoys chirping throughout the day.",
            image_url="static/images/hannah.jpeg"
        )

        animal15 = Animal(
            name="Cocoa",
            species="Rabbit",
            age="4 years",
            description="Brown rabbit with soft fur and a calm personality.",
            image_url="static/images/cocoa.jpeg"
        )

        animal16 = Animal(
            name="Zeus",
            species="Dog",
            age="6 years",
            description="Large German shepherd who is protective and loyal.",
            image_url="static/images/zeus.jpeg"
        )

        animal17 = Animal(
            name="Daisy",
            species="Dog",
            age="2 years",
            description="Sweet beagle who loves belly rubs and long walks.",
            image_url="static/images/daisy.jpeg"
        )

        animal18 = Animal(
            name="Leo",
            species="Cat",
            age="5 years",
            description="Curious black cat with bright green eyes.",
            image_url="static/images/leo.jpeg"
        )

        animal19 = Animal(
            name="Blue",
            species="Bird",
            age="3 years",
            description="Blue parrot who enjoys mimicking sounds and music.",
            image_url="static/images/blue.jpeg"
        )

        animal20 = Animal(
            name="Ruby",
            species="Rabbit",
            age="2 years",
            description="Energetic rabbit who loves carrots and hopping around.",
            image_url="static/images/ruby.jpeg"
        )

        animal21 = Animal(
            name="Venom",
            species="Snake",
            age="4 years",
            description="Striped corn snake with a calm and relaxed temperament.",
            image_url="static/images/venom.jpeg"
        )

        animal22 = Animal(
            name="Max",
            species="Dog",
            age="2 months",
            description="Young labrador puppy full of energy and excitement.",
            image_url="static/images/max.jpeg"
        )

        animal23 = Animal(
            name="Nala",
            species="Cat",
            age="4 years",
            description="Elegant siamese cat who enjoys quiet naps by the window.",
            image_url="static/images/nala.jpeg"
        )

        animal24 = Animal(
            name="Angel",
            species="Bird",
            age="2 years",
            description="White cockatiel with a peaceful and friendly personality.",
            image_url="static/images/angel.jpeg"
        )

        animal25 = Animal(
            name="Bunny",
            species="Rabbit",
            age="3 years",
            description="Tiny white rabbit who enjoys attention and treats.",
            image_url="static/images/bunny.jpeg"
        )

        animal26 = Animal(
            name="Titan",
            species="Snake",
            age="5 years",
            description="Large python that enjoys relaxing under heat lamps.",
            image_url="static/images/titan.jpeg"
        )

        animal27 = Animal(
            name="Charlie",
            species="Dog",
            age="14 years",
            description="senior rescue husky with a calm and loving personality.",
            image_url="static/images/charlie.jpeg"
        )

        animal28 = Animal(
            name="Milo",
            species="Cat",
            age="2 months",
            description="Playful kitten who loves toys and chasing strings.",
            image_url="static/images/milo.jpeg"
        )

        animal29 = Animal(
            name="Rio",
            species="Bird",
            age="1 year",
            description="Tropical macaw with colorful feathers and lots of energy.",
            image_url="static/images/rio.jpeg"
        )

        animal30 = Animal(
            name="Hazel",
            species="Rabbit",
            age="4 years",
            description="Quiet rabbit with soft brown fur and floppy ears.",
            image_url="static/images/hazel.jpeg"
        )

        animal31 = Animal(
            name="Echo",
            species="Snake",
            age="2 years",
            description="Small ball python with unique spotted patterns.",
            image_url="static/images/echo.jpeg"
        )


        db.session.add_all([
            animal1,
            animal2,
            animal3,
            animal4,
            animal5,
            animal6,
            animal7,
            animal8,
            animal9,
            animal10,
            animal11,
            animal12,
            animal13,
            animal14,
            animal15,
            animal16,
            animal17,
            animal18,
            animal19,
            animal20,
            animal21,
            animal22,
            animal23,
            animal24,
            animal25,
            animal26,
            animal27,
            animal28,
            animal29,
            animal30,
            animal31

        ])

        db.session.commit()

@app.route("/")
def home():
    query = request.args.get('search')
    if query:
        animals = Animal.query.filter(Animal.species.ilike(f"%{query}%")).all()
    else:
        animals = Animal.query.all()
    return render_template("home.html", animals=animals)


@app.route("/animal/<int:animal_id>")
def animal_detail(animal_id):

    animal = Animal.query.get_or_404(animal_id)

    return render_template(
        "animal_detail.html",
        animal=animal
    )


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User(
            username=username,
            password=generate_password_hash(password) 
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(
            username=username
        ).first()

        # This is where you use the check_password_hash function!
        if user and check_password_hash(user.password, password):

            session["user_id"] = user.id

            return redirect("/")

        else:

            return """
            <h1>User does not exist or password is incorrect.</h1>
            <a href='/register'>Create an Account</a>
            <br><br>
            <a href='/login'>Try Again</a>
            """

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


@app.route("/favorite/<int:animal_id>")
def favorite(animal_id):

    if "user_id" not in session:

        return redirect("/login")

    user = User.query.get(session["user_id"])

    animal = Animal.query.get(animal_id)

    if animal not in user.saved_animals:

        user.saved_animals.append(animal)

        db.session.commit()

    return redirect("/favorites")

@app.route("/remove_favorite/<int:animal_id>")
def remove_favorite(animal_id):

    if "user_id" not in session:

        return redirect("/login")

    user = User.query.get(session["user_id"])

    animal = Animal.query.get(animal_id)

    if animal in user.saved_animals:

        user.saved_animals.remove(animal)

        db.session.commit()

    return redirect("/favorites")


@app.route("/favorites")
def favorites():

    if "user_id" not in session:

        return redirect("/login")

    user = User.query.get(session["user_id"])

    return render_template(
        "favorites.html",
        animals=user.saved_animals
    )


if __name__ == "__main__":
    app.run(debug=True)