#!/usr/bin/python3
"""Module that uses requests to access Reddit API and print JSON response"""

import requests
import os

# Reddit app credentials and user details
client_id = "OIrI4vj9LL5jlSy6_VNgWw"
client_secret = os.getenv('REDDIT_SCRT')
user_agent = "python:app_iygeal:1.0.0 (by /u/iygeal)"
username = "iygeal"
password = os.getenv('REDDIT_PWD')

# Obtain access token
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
data = {
    'grant_type': 'password',
    'username': username,
    'password': password
}

headers = {"User-Agent": user_agent}

response = requests.post(
    "https://www.reddit.com/api/v1/access_token", auth=auth, data=data, headers=headers)
if response.status_code != 200:
    print(
        f"Error: Failed to get access token, status code: {response.status_code}")
    print(response.json())
    exit(1)

access_token = response.json()['access_token']

# Function to get headers for authentication


def get_headers():
    """Function to get headers for authentication"""
    return {
        "User-Agent": user_agent,
        "Authorization": f"Bearer {access_token}"
    }


# Define the base URL and headers
base_url = "https://oauth.reddit.com/r/python/top"
headers = get_headers()

# Initial request parameters
params = {
    "limit": 1  # Number of posts per page
}

# Fetch and print the JSON response
response = requests.get(base_url, headers=headers, params=params)
if response.status_code != 200:
    print(f"Failed to fetch posts: {response.status_code}")
else:
    json_response = response.json()
    print(json_response)
