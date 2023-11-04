from youtube_transcript_api import YouTubeTranscriptApi as yta
import json
import re
import os
import isodate  
from dotenv import load_dotenv
import requests

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

def getVideoIDfromLink(video_link):
    pattern = r'=(.*?)(?:&|$)'
    match = re.search(pattern, video_link)
    return match.group(1) if match else None

def getYoutubeTranscript(video_id):
    try:
        transcript = yta.get_transcript(video_id, languages=['en'])
    except:
        return None
    
    text = ' '.join([entry['text'] for entry in transcript])
    return text

def get_youtube_link(search_query, page_token=None):
    search_query += ' audio guide clear steps'
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/search',
        params={
            'key': GOOGLE_API_KEY,
            'q': search_query,
            'type': 'video',
            'part': 'snippet',
            'maxResults': 1,
            'pageToken': page_token  # Pass the page token here
        }
    )
    # Extract video link
    if response.json().get('items'):
        return "https://www.youtube.com/watch?v=" + response.json()['items'][0]['id']['videoId']
    else:
        if 'error' in response.json() and 'message' in response.json()['error']:
            print(response.json()['error']['message'])
        return None

def find_suitable_video(search_query):
    page_token = None
    count = 0
    while True:
        count += 1
        if count > 20:
            return None
        video_link = get_youtube_link(search_query, page_token)  # Pass the page token here
        if not video_link:
            break
        # print(video_link)

        video_id = getVideoIDfromLink(video_link)
        transcript_text = getYoutubeTranscript(video_id)
        
        if transcript_text:
            word_count = len(transcript_text.split())
            if 100 <= word_count <= 1000:
                return video_link, transcript_text

        # Get the next page token for the next iteration
        response = requests.get(
            'https://www.googleapis.com/youtube/v3/search',
            params={
                'key': GOOGLE_API_KEY,
                'q': search_query,
                'type': 'video',
                'part': 'snippet',
                'maxResults': 1,
                'pageToken': page_token  # This will be used for pagination
            }
        )
        page_token = response.json().get('nextPageToken')
        if not page_token:
            break  # Break if there's no more videos to fetch

    return None
# Example usage:
# search_query = "how to bake a cake"
# video_link = find_suitable_video(search_query)
# print(video_link)
# print(transcript)  # This will print the transcript of the suitable video
