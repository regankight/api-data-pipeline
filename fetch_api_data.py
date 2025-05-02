import requests
import pandas as pd

def fetch_api_data():
    url = "https://jsonplaceholder.typicode.com/users"
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame(data)
    df.to_csv('data/raw_users.csv', index=False)
    return df
