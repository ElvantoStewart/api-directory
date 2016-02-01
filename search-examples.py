"""
This module will look at some examples of using the people/search endpoint.

Each individual search will again save the data for the members in a CSV file.
"""
print("Starting up")
# Bringing the require Python Packages in.
import csv                              # To work with the CSV files
import ElvantoAPI                       # To work with the Elvanto API
import json


# Bring the API Key from api.py
import api


print("Initialising the connection")
# Initalising the connection object. This is what we use to make the API Calls
conn = ElvantoAPI.Connection(APIKey=api.key)


print("Let's get a list of all the Male Contact's in your database!")
print("We also want their birthdate, and their Marital Status!")

# Constructing the search terms
params = {
    "contact": "yes",
    "gender": "Male"
}
info = [
    "marital_status",
    "birthdate"
]

print("Downloading data!")
male_contacts = conn._Post("people/search", search=params)["people"]["person"]
print("Time to process the data we downloaded")
print("We don't need their profile pictures, let's delete that information")
for contact in male_contacts:
    del(contact["picture"])

print("Ok, we've got all the data we need. Let's save this to a CSV file")
with open("search-results.csv", "w+") as file:
    writer = csv.DictWriter(file, list(male_contacts[0].keys()))
    writer.writeheader()
    writer.writerows(male_contacts)

print("File saved!")
