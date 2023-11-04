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

def get_youtube_link(search_query):
    search_query += ' audio guide clear steps'
    response = requests.get(
        'https://www.googleapis.com/youtube/v3/search',
        params={
            'key': GOOGLE_API_KEY,
            'q': search_query,
            'type': 'video',
            'part': 'snippet',
            'maxResults': 10
        }
    )

    # Extract video links
    video_links = ["https://www.youtube.com/watch?v=" + item['id']['videoId'] for item in response.json()['items']]
    return video_links

def find_suitable_video(search_query):
    video_links = get_youtube_link(search_query)

    for link in video_links:
        video_id = getVideoIDfromLink(link)
        transcript_text = getYoutubeTranscript(video_id)
        
        if transcript_text:
            word_count = len(transcript_text.split())
            if 100 <= word_count <= 1000:
                return link, transcript_text

    return None  # Return None if no suitable video found

# Example usage:
search_query = "how to bake a cake"
video_link = find_suitable_video(search_query)
print(video_link)
