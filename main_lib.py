import csv

event = {}
name = {}
times = {}


def load_data(directory = 'CSV'):
    """
    Load data from CSV file into dictionaries
    """

    #load events, people, and times  
    with open(f"{directory}/Test1.csv", encoding = "utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            id = (row["Event"])
            #if the event is a new event, we initialize the dictionary because we are now able to add to this dictionary 
            event.setdefault(id, {"Event": row["Event"]})
            event[id][row["Name"]] = row["Time"]
            id = (row["Name"])
            name.setdefault(id, {"Name": row["Name"]})
            name[id][row["Event"]] = row["Time"]

    #load people by teams 

#time is a string 
def convert_into_seconds(time: str):
    if ':' in time:
        minutes,seconds = time.split(':')
        minutes = float(minutes)
        seconds = float(seconds)
        return (minutes * 60) +seconds
    else:
        return float(time)


