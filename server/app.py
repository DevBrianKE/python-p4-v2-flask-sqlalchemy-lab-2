from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Customer, Item, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return '<h1>Flask SQLAlchemy Lab 2</h1>'

@app.route('/customers/<int:id>')
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify(customer.to_dict())

@app.route('/items/<int:id>')
def get_item(id):
    item = Item.query.get_or_404(id)
    return jsonify(item.to_dict())

@app.route('/reviews/<int:id>')
def get_review(id):
    review = Review.query.get_or_404(id)
    return jsonify(review.to_dict())

if __name__ == '__main__':
    app.run(port=5555, debug=True)