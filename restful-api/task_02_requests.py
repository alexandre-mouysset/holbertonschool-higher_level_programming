#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():

    page_response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {page_response.status_code}")

    data = page_response.json()
    for post in data:
        print(post["title"])


def fetch_and_save_posts():

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
