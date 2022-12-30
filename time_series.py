from client_database import get_database
from dateutil import parser

db = get_database()
# This drops the time_series_test collection to refresh data.
db.drop_collection("time_series_test")
# This creates a collection named time_series_data in the database.
collection = db["time_series_test"]

# Create a list of time series data points.
time_series_data = [
    {"metadata": {"sensorId": 1, "type": "temperature"}, "timestamp": "2022-01-01T00:00:00", "value": 10},
    {"metadata": {"sensorId": 1, "type": "temperature"}, "timestamp": "2022-01-01T01:00:00", "value": 20},
    {"metadata": {"sensorId": 1, "type": "temperature"}, "timestamp": "2022-01-01T02:00:00", "value": 30},
    {"metadata": {"sensorId": 1, "type": "temperature"}, "timestamp": "2022-01-01T03:00:00", "value": 40},
    {"metadata": {"sensorId": 2, "type": "CO2"}, "timestamp": "2022-01-01T02:00:00", "value": 50},
    {"metadata": {"sensorId": 2, "type": "CO2"}, "timestamp": "2022-01-01T03:00:00", "value": 60},
]

# Insert the time series data into the collection.
collection.insert_many(time_series_data)

# Set Query Filters
start_timestamp = "2022-01-01T01:00:00"
end_timestamp = "2022-01-01T03:00:00"
sensorIdChoice = 1

# Use the find() method to fetch the data with timestamps within the specified range
data = collection.find({"timestamp": {"$gte": start_timestamp, "$lte": end_timestamp}, "metadata.sensorId": sensorIdChoice})

# Print out data
for datapoint in data:
    print(datapoint["value"])