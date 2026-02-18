#!/usr/bin/python3
"""
Utilities to fetch posts from JSONPlaceholder and either print
their titles or save full posts to a CSV file.

Functions
- fetch_and_print_posts(): fetches posts and prints the HTTP status
  code followed by each post title.
- fetch_and_save_posts(): fetches posts, prints the HTTP status code,
  and writes posts to `posts.csv` with columns `id`, `title`, `body`.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from JSONPlaceholder and print each post title.

    The function performs an HTTP GET request to
    https://jsonplaceholder.typicode.com/posts, prints the response
    status code to stdout, then prints the `title` of each post.

    Args:
        None

    Returns:
        None

    Side effects:
        Prints the HTTP status code and post titles to stdout.
    """
    page_response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {page_response.status_code}")

    data = page_response.json()
    for post in data:
        print(post["title"])


def fetch_and_save_posts():
    """
    Fetch posts and save them to a CSV file named `posts.csv`.

    The function performs an HTTP GET request to
    https://jsonplaceholder.typicode.com/posts, prints the response
    status code to stdout, converts the JSON payload into a list of
    dictionaries with keys `id`, `title` and `body`, then writes that
    list to `posts.csv` (UTF-8 encoded) including a header row.

    Args:
        None

    Returns:
        None

    Side effects:
        - Prints the HTTP status code to stdout.
        - Creates or overwrites a file named `posts.csv` in the
          current working directory.
    """
    page_response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print(f"Status Code: {page_response.status_code}")
    if page_response.status_code == 200:
        data = page_response.json()

    posts_list = []

    for post in data:
        post_dic = {
            "id": post["id"], "title": post["title"], "body": post["body"]
        }
        posts_list.append(post_dic)

    with open("posts.csv", "w", encoding="UTF-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(posts_list)
