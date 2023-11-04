from query_gpt import query_gpt
from youtube_link_getter import get_youtube_link
from youtube_transcript import getYoutubeTranscript

def main_combined(query="My toilet is broken, what should I do?"):
    # get the youtube link
    youtube_link = get_youtube_link(query)
    # get the transcript
    transcript = getYoutubeTranscript(youtube_link)
    # get the response
    new_query = f"Using this video transcript to help source information '{transcript}', answer this question '{query}' in clear steps"
    response = query_gpt(query, transcript=transcript, max_tokens=150)
    # get the steps
    steps = get_steps(response)
    return steps, youtube_link[0]

def get_steps(rawoutput):
    # the raw output is a string of steps seperated with new lines and numbers, get the steps as a list of strings
    steps = rawoutput.split("\n")
    # remove the numbers
    steps = [step[2:] for step in steps]
    # remove any empty strings
    steps = [step for step in steps if step]
    print(steps)
    return steps




if __name__ == '__main__':
    query = "how do I make my own phone case?"
    response, yt_link = main_combined(query)
    for step in response:
        print(step)
    print(yt_link)
