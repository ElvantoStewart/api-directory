import csv
import ElvantoAPI
import json
key = "YOUR API KEY"
con = ElvantoAPI.Connection(APIKey=key)


# Getting the information about the groups from the file.
groups = []
with open("groups.csv") as file:
    reader = csv.DictReader(file)
    for group in reader:
        groups.append(group)

print("Groups loaded! Here they are!")
print(json.dumps(groups, indent=4))

print("Lets create the groups!")
for group in groups:
    if group["Address Line 2"]:
        # If the group has a line 2 in it's address it needs to be structured differently.
        info = {
            "name":group["Group Name"],
            "meeting_address": "{}, {}".format(group["Address"], group["Address Line 2"]),
            "meeting_city": group["City"],
            "meeting_start_date": group["Start"],
            "meeting_start_time": group["Start Time"],
            "meeting_end_time": group["End Time"],
            "meeting_frequency": {
                "type": group["Frequency"],
                "count": group["Count"],
                "day": group["Meeting Day"]
            }
        }
        print("Creating the following group: {}".format(info["name"]))
        print(json.dumps(info, indent=4))
        result = con._Post("groups/create", **info)
        print(json.dumps(result, indent=4))
    else:
        info = {
            "name":group["Group Name"],
            "meeting_address": group["Address"],
            "meeting_city": group["City"],
            "meeting_start_date": group["Start"],
            "meeting_start_time": group["Start Time"],
            "meeting_end_time": group["End Time"],
            "meeting_frequency": {
                "type": group["Frequency"],
                "count": group["Count"],
                "day": group["Meeting Day"]
            }
        }
        print("Creating the following group: {}".format(info["name"]))
        print(json.dumps(info, indent=4))
        result = con._Post("groups/create", **info)
        print(json.dumps(result, indent=4))
