#!/usr/bin/python3
"""Module that uses requests to access Reddit API"""

import requests
import time
import os


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
    print("Error: Failed to get access token")
    exit(1)

access_token = response.json()['access_token']

# Define function to get headers for authentication


def get_headers():
    """_summary_
    Function to get headers for authentication
    """
    return {
        "User-Agent": user_agent,
        "Authorization": f"Bearer {access_token}"
    }


# Define the base url and headers
base_url = "https://oauth.reddit.com/r/python/top"
headers = get_headers()

# Initial request parameters
params = {
    "limit": 10  # Number 10 posts
}

# # Function to fetch posts with pagination


def get_posts():
    """_summary_
    Function to fetch posts with pagination
    """
    after = None
    while True:
        if after:
            params["after"] = after
        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch posts: {response.status_code}")
            break

        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])

        after = data["data"]["after"]
        if not after:
            break
        time.sleep(1)  # Respect API rate limits


# Fetch and print posts with pagination
get_posts()
