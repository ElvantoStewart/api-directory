"""
This module is designed to get the list of custom fields from an Elvanto account and output them to a CSV file.

Saves the custom fields into a CSV file called "custom_fields.csv" in your working directory
"""

print("Starting up")
# Bringing the require Python Packages in.
import csv                  # To work with the CSV files
import ElvantoAPI           # To work with the Elvanto API


# Bring the API Key from api.py
import api


print("Initialising the connection")
# Initalising the connection object. This is what we use to make the API Calls
conn = ElvantoAPI.Connection(APIKey=api.key)

print("Getting fields")
fields = conn._Post("people/customFields/getAll")["custom_fields"]["custom_field"]

# This data has a large number of "ID" fields in the results. We don't need these, so lets delete them!

print("Cleaning up the field data and removing un-needed data")
for field in fields:                            # Go over all the fields
    if field["values"]:                         # Check to see if it has multiple values
        new_values = []                         # Create a temporary list to store the values in
        for value in field["values"]["value"]:  # Go over the values for that field
            new_values.append(value["name"])    # Add the values to the list
        field["values"] = new_values            # Overwrite the old Dict object and replace with the list

print("Saving the file")
with open("custom_fields.csv", "w+") as file:               # Opens the CSV Files
    writer = csv.DictWriter(file, list(fields[0].keys()))   # Calls the object that writes the CSV files
    writer.writeheader()                                    # Writes the first row of the CSV file (The headers)
    writer.writerows(fields)                                # Writes the data into the CSV file.

print("Done!")
