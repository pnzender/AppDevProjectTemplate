# Import necessary libraries and modules
from bson.objectid import ObjectId
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import projectsDatabase
import hardwareDatabase

# Import custom modules for database interactions
#import usersDB
#import projectsDB
#import hardwareDB

# Define the MongoDB connection string
client = MongoClient('mongodb+srv://admin:123admin456@cluster0.fxjtzjv.mongodb.net/')
db = client['apad']
db_project = db['project']
db_hardware = db['hardwareset']

# Initialize a new Flask web application
app = Flask(__name__)
#CORS(app)

@app.route("/")
def welcome():
    return "<p>Welcome to flask!</p>"

@app.route('/create_project', methods=['POST'])
def create_project():
    data = request.get_json()

    if not all(key in data for key in ('name', 'description', 'projectId')):
        return jsonify({'error': 'Missing required fields'}), 400

    name =  data['name']
    projectId = data['projectId']
    description = data['description']
    user = 'abc' #replace with the current user

    result = projectsDatabase.createProject(db_project, name, projectId, description, user)

    return result

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    # Extract data from request

    # Connect to MongoDB

    # Attempt to log in the user using the usersDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for the main page (Work in progress)
@app.route('/main')
def mainPage():
    # Extract data from request

    # Connect to MongoDB

    # Fetch user projects using the usersDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for joining a project
@app.route('/join_project', methods=['POST'])
def join_project():
    # Extract data from request

    # Connect to MongoDB

    # Attempt to join the project using the usersDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for adding a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    # Extract data from request

    # Connect to MongoDB

    # Attempt to add the user using the usersDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for getting the list of user projects
@app.route('/get_user_projects_list', methods=['POST'])
def get_user_projects_list():
    # Extract data from request

    # Connect to MongoDB

    # Fetch the user's projects using the usersDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for creating a new project
#@app.route('/create_project', methods=['POST'])
#def create_project():
    # Extract data from request

    # Connect to MongoDB

    # Attempt to create the project using the projectsDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for getting project information
@app.route('/get_project_info', methods=['POST'])
def get_project_info():
    # Extract data from request

    # Connect to MongoDB

    # Fetch project information using the projectsDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for getting all hardware names
@app.route('/get_all_hw_names', methods=['POST'])
def get_all_hw_names():
    # Connect to MongoDB

    # Fetch all hardware names using the hardwareDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

@app.route('/get_hw_info', methods=['POST'])
def get_hw_info():

    data = [{}, {}]
    data[0] = hardwareDatabase.queryHardwareSet("001", db_hardware)
    data[1] = hardwareDatabase.query_hardware("002", db_hardware)

    return jsonify(data)

# Route for checking out hardware
@app.route('/check_out', methods=['POST'])
def check_out():
    # Extract data from request

    # Connect to MongoDB

    # Attempt to check out the hardware using the projectsDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for checking in hardware
@app.route('/check_in', methods=['POST'])
def check_in():
    # Extract data from request

    # Connect to MongoDB

    # Attempt to check in the hardware using the projectsDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for creating a new hardware set
@app.route('/create_hardware_set', methods=['POST'])
def create_hardware_set():
    # Extract data from request

    # Connect to MongoDB

    # Attempt to create the hardware set using the hardwareDB module

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Route for checking the inventory of projects
@app.route('/api/inventory', methods=['GET'])
def check_inventory():
    # Connect to MongoDB

    # Fetch all projects from the HardwareCheckout.Projects collection

    # Close the MongoDB connection

    # Return a JSON response
    return jsonify({})

# Main entry point for the application
if __name__ == '__main__':
    app.run()

