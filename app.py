"""Flask app for Cupcakes"""

from ctypes import sizeof
from logging.handlers import RotatingFileHandler
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from sqlalchemy import false, update
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)



@app.route('/', methods = ['GET', 'POST'])
def list_all_cupcakes():
    """Show an empty list where cupcakes should appear and a form where new cupcakes can be added."""

    return render_template('home.html')

@app.route('/api/cupcakes', methods = ['GET'])
def get_all_cupcake_data():
    """Get data for all cupcakes"""
    
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.order_by(Cupcake.id.asc()).all()]

    return jsonify(all_cupcakes = all_cupcakes)

@app.route('/api/<int:cupcake_id>', methods = ['GET'])
def get_cupcake_data(cupcake_id):
    """Get data about a single cupcake"""

    cupcake =  Cupcake.query.get_or_404(cupcake_id).serialize()

    return jsonify(cupcake = cupcake)

@app.route('/api/cupcakes', methods = ['POST'])
def create_cupcake():
    """Create a cupcake with flavor, size, rating and image data from the body of the request."""

    new_cupcake = Cupcake(
        flavor = request.json['flavor'],
        size = request.json['size'],
        rating = request.json['rating']
    )
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(new_cupcake = new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods = ['PATCH'])
def update_cupcake(cupcake_id):
    """Update a cupcake with the id passed in the URL and flavor, size, rating and image data from the body of the request. You can always assume that the entire cupcake object will be passed to the backend."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json['flavor']
    cupcake.rating = request.json['rating']
    cupcake.size = request.json['size']
    cupcake.image = request.json['image'],

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods = ['DELETE'])
def delete_cupcake(cupcake_id):
    """Delete cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")     



