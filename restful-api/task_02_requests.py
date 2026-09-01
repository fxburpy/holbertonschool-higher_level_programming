#!/usr/bin/python3
"""Fetch and process post data from JSONPlaceholder."""

import csv
import requests


POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print the response status and every post title."""
    response = requests.get(POSTS_URL)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save selected fields to ``posts.csv``."""
    response = requests.get(POSTS_URL)
    if response.status_code == 200:
        posts = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            for post in response.json()
        ]
        with open("posts.csv", "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts)
