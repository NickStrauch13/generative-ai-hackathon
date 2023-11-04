from query_gpt import query_gpt
from youtube_link_getter import get_youtube_link
from youtube_transcript import getYoutubeTranscript

def main_combined(query="My toilet is broken, what should I do?"):
    # get the youtube link
    youtube_link = get_youtube_link(query)
    # get the transcript
    transcript = getYoutubeTranscript(youtube_link)
    # get the response
    new_query = f"Using this video transcript to help source information '{transcript}', answer this question '{query}'"
    response = query_gpt(query, transcript=transcript, max_tokens=150)
    return response, youtube_link[0]

if __name__ == '__main__':
    query = "how do I create my own dartboard?"
    response, yt_link = main_combined(query)
    print(response)
    print(yt_link)
