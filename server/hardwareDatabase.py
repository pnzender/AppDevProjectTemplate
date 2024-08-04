# Import necessary libraries and modules
from pymongo import MongoClient
import hardwareSet

'''
Structure of Hardware Set entry:
HardwareSet = {
    'hwName': hwSetName,
    'capacity': initCapacity,
    'availability': initCapacity
}
'''

# Function to create a new hardware set
def createHardwareSet(id, hwSetName, initCapacity, hardwareset):
    hw = {
        "hwId": id,
        "hwName": hwSetName,
        "capacity": initCapacity,
        "availability": initCapacity
    }

    hardwareset.insert_one(hw)

# Function to query a hardware set by its id
def queryHardwareSet(id, hardwareset):
    query = {"hwId": id}
    f = hardwareset.find_one(query)
    return f

# Function to update the availability of a hardware set
def updateAvailability(client, hwSetName, newAvailability):
    # Update the availability of an existing hardware set
    pass

# Function to request space from a hardware set
def requestSpace(client, hwSetName, amount):
    # Request a certain amount of hardware and update availability
    pass

# Function to get all hardware set names
def getAllHwNames(client):
    # Get and return a list of all hardware set names
    pass

