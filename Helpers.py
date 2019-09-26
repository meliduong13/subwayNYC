import requests
import sys
from requests.exceptions import HTTPError


class Helpers:
    # method used to validate the user's input 'user_input' if it is not a value contained in the 'list_input'
    def validate_user_input(self, user_input, list_input):
        try:
            if user_input not in list_input and user_input.upper() not in list_input:
                raise ValueError
            else:
                return user_input
        except ValueError:
            print('Invalid value, you must enter a value from the ones listed below')

    # method to handle server exception. For example, an exception could be that the server is down
    def handle_url_response(self, url):
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
