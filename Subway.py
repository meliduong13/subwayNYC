import ast
import csv
import json

from Helpers import *
from Stop import *

stops_dict = {}
helpers = Helpers()

# read the file  'stops.txt' and store its values in a dictionary that associates an id with a Stop object
with open('stops.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        stops_dict[row["stop_id"]] = Stop(row["stop_name"], row["stop_lat"], row["stop_lon"],
                                          row["location_type"], row["parent_station"])


# method to handle server exception. For example, an exception could be thrown when the server is down
def access_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError:
        print(f'An error with the server occurred, try again later.')
        sys.exit(f'Program exiting')
    except Exception:
        print(f'An error occurred, try again later.')
        sys.exit(f'Program exiting')
    else:
        return response


url_get_all_subway_lines = 'http://traintimelb-367443097.us-east-1.elb.amazonaws.com/getSubwaylines'

# retrieve all subway lines
response_get_all_subway_lines = helpers.handle_url_response(url_get_all_subway_lines)
loop = True
lines_list = []
ask_input = True
line_id = ""
json_lines = json.loads(response_get_all_subway_lines.content)

#  put all line id's from the json response to a list
for line in json_lines:
    lines_list.append(line["id"])

# while the user still wants to query a new line, do the code below
while loop:
    while ask_input:
        print('Enter a line from the ones listed:')
        for each in lines_list:
            print(each, end=",")
        print('\n')
        chosen_line = input("")
        line_id = helpers.validate_user_input(chosen_line, lines_list)

        # if the user entered the wrong value, prompt them again until they enter a correct value
        # Once they do enter a correct value, continue to the code below, after the 'else' statement
        if line_id is None:
            ask_input = True
        else:
            ask_input = False

    url_get_stations_for_chosen_line = 'http://traintimelb-367443097.us-east-1.elb.amazonaws.com/getStationsByLine/' \
                                       + line_id
    # get the stops for the chosen line
    response_get_stations_for_chosen_line = helpers.handle_url_response(url_get_stations_for_chosen_line)
    json_stops = json.loads(response_get_stations_for_chosen_line.content)

    # the dictionary that was returned was in a string format, it had to be converted to a dictionary to be read
    # using 'ast.literal_eval'
    json_stops = ast.literal_eval(json_stops)

    # listing all the stops by looping through the list of stops per borough for all borough for a chosen line
    print('Stops of route {0} : '.format(line_id.upper()))
    for borough in json_stops:
        for station in borough["stations"]:
            # printing the station name, id, longitude and latitude. The two last attributes are found in the
            # stops_dict dictionary. We get the information of a Stop object by retrieving it by it's id
            print('{0} ({1}): {2}, {3}'
                  .format(station["name"], station["id"], stops_dict[station["id"]].get_longitude(),
                          stops_dict[station["id"]].get_latitude()))
    print('\n')

    # allow the user to stop the program or continue querying another line
    keep_going = input('To choose another line enter Y, otherwise enter any key to stop the program...')
    if keep_going is 'Y' or keep_going is 'y':
        loop = True
        ask_input = True
    else:
        print('Thank you for using this application!')
        loop = False

#  below I am reassinging these values once the program ends. This is to be able to test the exception catching method
#  'handle_url_response' from the class 'Helpers'
lines_list = None
stops_dict = None
json_stops = None
