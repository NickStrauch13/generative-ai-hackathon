
import os
from dotenv import load_dotenv
import requests
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


def get_youtube_link(search_query):
    # Perform the search

    response = requests.get(
        'https://www.googleapis.com/youtube/v3/search',
        params={
            'key': GOOGLE_API_KEY,
            'q': search_query,
            'type': 'video',
            'part': 'snippet',
            'maxResults': 1
        }
    )
    video_id = response.json()['items'][0]['id']['videoId']
    video_url = f'https://www.youtube.com/watch?v={video_id}' 
    return video_url  

