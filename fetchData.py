import requests as req
import sys
from typing import List, Dict, Any


# API endpoint
API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_and_display_users(filter_city: str = None):

    print(f"--- Fetching User Data from {API_URL} ---")
    if(filter_city):
        print(f"Applying bonus filter: Only showing users in cities starting with '{filter_city}'")
    
    try:
        # step 1: GET Request
        res = req.get(API_URL, timeout=10)

        # step 2: handling exceptions
        res.raise_for_status()

        # step 3: parsing JSON data
        users : List[Dict[str, Any]] = res.json()

        # step 4: checking for empty list
        if not users:
            print("Error: The API returned an empty list of users")
            return 
        
        # step 5: create an counter for display
        user_cnt = 0

        # step 6: iterating over each user
        for user_data in users:
            
            name = user_data.get('name', 'N/A')
            usrname = user_data.get('username', 'N/A')
            email = user_data.get('email', 'N/A')

            city = user_data.get('address', {}).get('city', 'N/A')

            # filter logic
            if filter_city:
                # skip the user if the city doesn's starts with the specified letter
                if not city.upper().startswith(filter_city.upper()):
                    continue
            
            user_cnt += 1

            # print each user data
            print(f"\nUser {user_cnt}:")
            print(f"    Name: {name}")
            print(f"    Username: {usrname}")
            print(f"    Email: {email}")
            print(f"    City: {city}")
            print("-"*30)

            if user_cnt == 0:
                print("No users found matching the filter criteria")

    except req.exceptions.HTTPError as e:
        print(f"\nAPI Request Error: Failed to retrieve data")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occured: {e}")
        sys.exit(1)

if __name__ == "__main__":

    # Run the main function. Uncomment the line below to apply 
    # the optional bonus filter for cities starting with 'S'.
    fetch_and_display_users(filter_city='S')

   # Run without the filter
    # fetch_and_display_users()




