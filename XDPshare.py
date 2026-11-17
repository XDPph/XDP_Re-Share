import time
import schedule
import requests

def job():
    page_id = 1207004219167855
    access_token = EAAkJip2wSrgBTD0N4JLfn4OXF9CFxoqlgRwDgsiDCY1VSE1QsFKKTMaYv1xdKNbZCiCa2ZBsSMn4ZCsNtPyArWIObq7CE8xCWUtGl46XutSmZANwxwnk0QZBTHhMvYczhbgT5d74BrI34FCdKskJZASh6NMLfIHYvGrDfZCztzyxU8z2YukuXfRcv4IQBb4x23ZBFGMrT1z5z0ijk3WqyScNlxaRdPP7lYzqZBT3Mr8LX0nz30EjdjoDLM1Lf0q7f2OoyZAgX0PUSEWcABi1zXyn1ZC58TRP4jm7Nd2awZDZD
    
    url = f'https://graph.facebook.com/{page_id}/feed'
    
    payload = {
        'message': 'Hello from my automated Python script!',
        'link': 'https://www.example.com',
        'access_token': access_token
    }
    
    response = requests.post(url, data=payload)
    print("Response status code:", response.status_code)
    print(response.json())

# Schedule the job to run every day at a specific time, or as needed
schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

