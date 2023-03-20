from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
import random


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
engine = create_engine('sqlite:///cafes.db')


# cafe TABLE Configuration
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
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


def api_response(message):
    if message == "error":
        message = {
            "error": {
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        }
        return message
    if message == "error_dupe":
        message = {
            "error": {
                "Duplicate": "Sorry, we already have that cafe."
            }
        }
        return message
    if message == "error_not_found":
        message = {
            "error": {
                "Not Found": "Cafe doesn't exist in database."
            }
        }
        return message
    if message == "error_not_authorized":
        message = {
            "error": {
                "Not Authorized": "You silly you cant do this without an api-key."
            }
        }
        return message
    if message == "success":
        message = {
            "response": {
                "Success": "Successfully added the new cafe."
            }
        }
        return message
    if message == "success_price":
        message = {
            "response": {
                "Success": "Successfully changed the price."
            }
        }
        return message
    if message == "success_deleted":
        message = {
            "response": {
                "Success": "Successfully deleted the cafe."
            }
        }
        return message


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    # Allows GET requests and serves up a random cafe
    # Get total results from the db
    Session = sessionmaker(bind=engine)
    session = Session()
    total_cafes = session.query(Cafe).count()
    random_num = random.randint(1, total_cafes)
    cafe = session.query(Cafe).get(random_num)
    session.close()
    params = jsonify({
        "cafe": {
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
    }})
    return params


#  HTTP GET - Read Record
@app.route("/all")
def get_all_cafes():
    # Get total of all cafes in db
    Session = sessionmaker(bind=engine)
    session = Session()
    total_cafes = session.query(Cafe).count()
    cafe_data = {"cafe": []}
    for num in range(1, total_cafes):
        cafe = session.query(Cafe).get(num)
        params = {
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price
            }
        cafe_data['cafe'].append(params)
    session.close()
    return jsonify(cafe_data)


@app.route('/search')
def search_all_cafes():
    # get loc
    loc = request.args.get('loc')
    # sql connection
    Session = sessionmaker(bind=engine)
    session = Session()

    # find all the results for location
    cafes = session.query(Cafe).filter(Cafe.location.ilike(f"%{loc}%")).all()
    if len(cafes) == 0:
        session.close()
        return jsonify(api_response("error"))
    else:
        # insert data
        cafe_data = {
            "cafe": [Cafe.to_dict(cafe) for cafe in cafes]
        }
        session.close()
        return jsonify(cafe_data)


#  HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    # Get POST information
    add_data = request.get_json()

    # Extract information and add to database
    with Session(engine) as session:
        existing_cafe = session.query(Cafe).filter_by(name=add_data['name']).first()
        if existing_cafe:
            return jsonify(api_response("error_dupe"))
        cafe = Cafe(**add_data)
        session.add(cafe)
        session.commit()
        return jsonify(api_response("success"))


# HTTP PATCH COFFE PRICE
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    price_data = request.get_json()

    with Session(engine) as session:
        # Get the cafe id and 404 if doesnt exist
        cafe = session.query(Cafe).filter_by(id=cafe_id).first()
        if cafe is None:
            return jsonify(api_response("error_not_found")), 404
        # Update the coffee price and commit
        cafe.coffee_price = price_data['coffee-price']
        session.commit()
    return jsonify(api_response("success_price"))


#  HTTP DELETE - Delete Record
@app.route("/delete-cafe/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    # check for authorization
    api_key = request.headers.get('api-key')
    if api_key != "TopSecretAPIKey":
        return jsonify(api_response("error_not_authorized")), 403

    with Session(engine) as session:
        # check if cafe exists with the id
        cafe = session.query(Cafe).filter_by(id=cafe_id).first()
        if cafe is None:
            # return 404 error
            return jsonify(api_response("error_not_found")), 404
        # Delete the cafe and commit
        session.delete(cafe)
        session.commit()
    return jsonify(api_response("success_deleted"))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
