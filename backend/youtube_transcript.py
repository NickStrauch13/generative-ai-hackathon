from youtube_transcript_api import YouTubeTranscriptApi as yta
import json
import re
def getYoutubeTranscript(video_link):
    video_id = getVideoIDfromLink(video_link)
    transcript = yta.get_transcript(video_id, languages=['en'])

    #concatenate all text into one string
    text = ''
    for i in range(len(transcript)):
        text += transcript[i]['text'] + ' '
    return text
def getVideoIDfromLink(video_link):
    pattern = r'=(.*?)(?:&|$)'
    
    # Searching for the pattern in the provided URL
    match = re.search(pattern, video_link)
    
    # If a match is found, return the captured substring; otherwise return None
    return match.group(1) if match else None
    
print(getYoutubeTranscript("https://www.youtube.com/watch?v=vKTBBc13o88"))