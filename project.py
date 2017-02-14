from flask import Flask
app = Flask(__name__)

## import CRUD operations
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/hello')
def HelloWorld():
	restaurants = session.query(Restaurant).all()
	output = ''
	for restaurant in restaurants:
		output += '<h3>%s</h3>' % restaurant.name
		items = session.query(MenuItem).filter_by(restaurant = restaurant).all()
		for item in items:
			output += item.name
			output += '<br>'
			output += item.price
			output += '<br>'
			output += item.description
			output += '<br>'
			output += '<br>' 
		output += '</br>'
	return output

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)