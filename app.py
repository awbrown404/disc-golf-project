# import dependencies
from flask import Flask, render_template
import pymongo

# create connection to MongoDB 
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.disc_golf_db

# connect to specific collections
courses = db.nc_courses
discs = db.innovadiscs

# develop routes
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("layout.html")

@app.route('/history')
def history():
    return render_template("history.html", title = "History of NC Disc Golf")

@app.route('/courses_map')
def courses_map():
    return render_template("courses_map.html", title = "Course Map")

@app.route('/innova')
def innova():
    return render_template("innova.html", title = "Innova")

if __name__ == "__main__":
    app.run(debug=True)