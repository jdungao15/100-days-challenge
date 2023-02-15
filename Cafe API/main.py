from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)


##Café TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        """Return dictionary version of Cafe model
            __table__.columns returns a list of columns in the table
            getattr returns the value of the attribute specified"""

        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


# Get Random Cafe
@app.route('/random')
def get_random_cafe():
    # retreive all cafes from the database
    cafes = db.session.query(Cafe).all()
    # choose a random cafe
    random_cafe = random.choice(cafes)

    return jsonify(cafe=random_cafe.to_dict())


# Return all cafes
@app.route('/all')
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


# Search for a cafe
@app.route('/search')
def search_cafe():
    location = request.args.get('loc')  # explain this
    cafes = db.session.query(Cafe).filter_by(location=location).all()
    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error={'Not Found': 'Sorry, we don\'t have a cafe at that location.'})


def str_to_bool(arg_from_url):
    if arg_from_url in ['True', ' true', 'T', 't', 'Yes', 'yes', 'y', '1']:
        return True
    else:
        return False


@app.route("/add", methods=["GET", "POST"])
def add_a_cafe():
    new_cafe = Cafe(name=request.args.get("name"),
                    map_url=request.args.get("map_url"),
                    img_url=request.args.get("img_url"),
                    location=request.args.get("location"),
                    seats=request.args.get("seats"),
                    has_toilet=str_to_bool(request.args.get("has_toilet")),
                    has_wifi=str_to_bool(request.args.get("has_wifi")),
                    has_sockets=str_to_bool(request.args.get("has_sockets")),
                    can_take_calls=str_to_bool(request.args.get("can_take_calls")),
                    coffee_price=request.args.get("coffee_price")
                    )
    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfully added the new cafe"})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    TOP_SECRET_API_KEY = 'TopSecretAPIKey'
    cafe = db.session.query(Cafe).get(cafe_id)
    api_key = request.args.get("api-key")
    if cafe:
        if api_key == TOP_SECRET_API_KEY:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully closed the cafe."}), 200
        else:
            return jsonify({"error": "Invalid API key."}), 403
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in"}), 404


## HTTP GET - Read Record


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
