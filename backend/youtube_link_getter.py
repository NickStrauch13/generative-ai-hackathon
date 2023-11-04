import os
import isodate  # Install this library using pip
from dotenv import load_dotenv
import requests

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

def get_youtube_link(search_query):
    # Step 1: Perform the search
    search_query = search_query+' audio guide clear steps'
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/search',
        params={
            'key': GOOGLE_API_KEY,
            'q': search_query,
            'type': 'video',
            'part': 'snippet',
            'maxResults': 10  # Fetch more results in case the first few videos are longer than 5.5 minutes
        }
    )
    
    video_ids = [item['id']['videoId'] for item in response.json()['items']]

    # Step 2: Retrieve video details
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/videos',
        params={
            'key': GOOGLE_API_KEY,
            'id': ','.join(video_ids),
            'part': 'contentDetails'
        }
    )

    for item in response.json()['items']:
        duration = isodate.parse_duration(item['contentDetails']['duration'])
        if duration.total_seconds() <= 5.5 * 60:  # Check if duration is less than or equal to 5.5 minutes
            return f"https://www.youtube.com/watch?v={item['id']}", duration.total_seconds()/60  # Return the video link and duration in minutes
    
    return None  # Return None if no suitable video found

# # Test
print(get_youtube_link("my toilet is broken, what should i do?"))