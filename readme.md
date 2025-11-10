# ☄️ RightChoice.ai Assignment - User Data Fetcher Script

## 🌍 Overview
This Python Script is coded to fetch user data from a public API (`https://jsonplaceholder.typicode.com/users`), process the JSON response, and display key user details. It also handles API errors and empty responses.

## 💻 Prerequisites
To run this script, you must habe the following installed
1. **Python 3.6+**
2. The `requests` library (for making GET request).

## 🛠️ Installation
1. **Clone the repository** or save `fetchData.py` file to your local machine
2. **Install the required Dependency (`requests`) using pip:
``` bash
pip install reuests
```

## 🧠 Usage

The script supports two primary modes of operation: the main task (displaying all users) and the optional bonus task (filtering by city).

1. **Main Task (Default Run)**

To run the script and display the Name, Username, Email, and City for all fetched users, 
``` bash
python fetchData.py
```

2. **Optional Bonus: Filter by City**

The script contains an optional filter that only prints users whose city name begins with a specific letter (case-insensitive).

To activate this feature, you must uncomment the line in the `if __name__ == "__main__"`: block of the `user_data_fetcher.py file`:

In `user_data_fetcher.py`:
```bash
if __name__ == "__main__":
    # Run the main function. Uncomment the line below to apply 
    # the optional bonus filter for cities starting with 'S'.
    
    fetch_and_display_users(filter_city_start='S')  # <-- UNCOMMENT THIS LINE
    
    # Run the main task without the filter
    # fetch_and_display_users()                      # <-- COMMENT OUT THIS LINE
```

If you uncomment the line `fetch_and_display_users(filter_city_start='S')` and run the script, it will only display users living in cities starting with 'S' (e.g., South River, Sydney, etc.).