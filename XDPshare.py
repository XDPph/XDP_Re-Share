import requests
import time

PAGE_ID = 1207004219167855
ACCESS_TOKEN = EAAkJip2wSrgBTD0N4JLfn4OXF9CFxoqlgRwDgsiDCY1VSE1QsFKKTMaYv1xdKNbZCiCa2ZBsSMn4ZCsNtPyArWIObq7CE8xCWUtGl46XutSmZANwxwnk0QZBTHhMvYczhbgT5d74BrI34FCdKskJZASh6NMLfIHYvGrDfZCztzyxU8z2YukuXfRcv4IQBb4x23ZBFGMrT1z5z0ijk3WqyScNlxaRdPP7lYzqZBT3Mr8LX0nz30EjdjoDLM1Lf0q7f2OoyZAgX0PUSEWcABi1zXyn1ZC58TRP4jm7Nd2awZDZD
SOURCE_PAGE_ID = 100068515465928
SINCE_TIMESTAMP = '2026-11-14T12:00:00'

def fetch_and_post():
    feed_url = f'https://graph.facebook.com/v19.0/{SOURCE_PAGE_ID}/feed'
    params = {
        'access_token': ACCESS_TOKEN,
        'since': SINCE_TIMESTAMP
    }
    
    response = requests.get(feed_url, params=params)
    if response.status_code != 200:
        print(f"Error fetching posts: {response.text}")
        return
        
    posts = response.json().get('data', [])
    if not posts:
        print("No new posts found.")
        return

    post_url = f'https://graph.facebook.com/v19.0/{PAGE_ID}/feed'
    
    for post in reversed(posts):
        message = post.get('message', '')
        link = post.get('permalink_url', '')
        
        if not message and not link:
            continue

        payload = {
            'message': message,
            'link': link,
            'access_token': ACCESS_TOKEN
        }
        
        post_response = requests.post(post_url, data=payload)
        if post_response.status_code == 200:
            print(f"Successfully posted: {post.get('id')}")
        else:
            print(f"Failed to post: {post_response.text}")

if __name__ == '__main__':
    fetch_and_post()
