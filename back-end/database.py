from model import (
    Wind, 
    WinchMotor, 
    Accelerometer, 
    AIS, 
    BMS, 
    Gyroscope, 
    GPS, 
    RudderMotor, 
    Sailencoder, 
    Waypoint
)

# MongoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://ubcsailbot:raye2021@sensordatacluster.sxfhu.mongodb.net/test")
database = client.SensorData 
# Same thing as a table in SQL

sensorDatabaseDictionary = {
    "wind": {
        "collection": database.wind,
        "model": Wind
    },
    "accelerometer": {
        "collection": database.accelerometer,
        "model": Accelerometer
    },
    "ais": {
        "collection": database.ais,
        "model": AIS
    },
    "winch_motor": {
        "collection": database.winchmotor,
        "model": WinchMotor
    },
    "gps": {
        "collection": database.gps,
        "model": GPS
    },
    "bms": {
        "collection": database.bms,
        "model": BMS
    },
    "gyroscope": {
        "collection": database.gyroscope,
        "model": Gyroscope
    },
    "rudder_motor": {
        "collection": database.ruddermotor,
        "model": RudderMotor
    },
    "sailencoder": {
        "collection": database.sailencoder,
        "model": Sailencoder
    },
    "waypoint": {
        "collection": database.waypoint,
        "model": Waypoint
    },
    "winch_motor": {
        "collection": database.winchmotor,
        "model": WinchMotor
    }
}

# TODO: have sensor_uri be replaced by an argument "properties" which is a dictionary that contains 
#       specific properties that you want to query from the database (e.g. time frame, uri, etc)
async def fetch_sensor_data(sensor_type, sensor_uri = None):
    """
    Returns all the sensor data based on the specified type, and optionally, the uri (sensorID). 

    Parameters:
    sensor_type (string): the type of sensor (e.g wind, winchmotor, etc.).
    sensor_uri (string): the uri of the sensor (OPTIONAL). 

    Returns List: the list of all queried sensor data from the database 
    """

    queried_data = []
    query = {}
    if(sensor_uri is not None): 
        query = { "sensor_id": sensor_uri }

    sensor_data = sensorDatabaseDictionary[sensor_type]["collection"].find(query)
    async for document in sensor_data:
        queried_data.append(sensorDatabaseDictionary[sensor_type]["model"](**document))

    return queried_data
    
# async def fetch_one_todo(title):
#     document = await collection.find_one({"title": title})
#     return document 

async def add_sensor_data(sensor_type, sensor_data):
    """
    Adds the sensor data to the specified database collection.

    Parameters:
    sensor_type (string): the collection to add the sensor data to.
    sensor_data (json): the data containing the sensor data information.
    """
    document = sensor_data 
    result = await sensorDatabaseDictionary[sensor_type]["collection"].insert_one(document)
    return result
