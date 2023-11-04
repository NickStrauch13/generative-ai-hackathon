from query_gpt import query_gpt
from youtube_transcript import find_suitable_video
import os
import json

temp_file = os.path.join("conversation_cache","temp.json")

def main_combined(query="My toilet is broken, what should I do?"):
    # get the youtube link
    suitable_video = find_suitable_video(query)
    while suitable_video is None:
        print("Couldn't find a suitable video for the given query.")
        query = input("Please try a different query: ")
        suitable_video = find_suitable_video(query)
    youtube_link = suitable_video[0]
    # get the transcript
    transcript = suitable_video[1]
    # query for solution steps
    new_query = f"Using this video transcript to help source information '{transcript}', answer this question '{query}' in clear steps"
    response = query_gpt(new_query, transcript=transcript, max_tokens=400)
    # get the steps
    steps = get_steps(response)
    # cache the conversation
    cache_conversation(transcript, response, query)
    return steps, youtube_link[0]

def get_steps(rawoutput):
    # the raw output is a string of steps seperated with new lines and numbers, get the steps as a list of strings
    # start at the first 1.
    output = rawoutput[rawoutput.index("1."):]
    steps = output.split("\n")
    # remove the numbers
    steps = [step[2:] for step in steps]
    # remove any empty strings
    steps = [step for step in steps if step]
    return steps

def cache_conversation(transcript, response, query):
    # overrite the temp file cache
    temp_path = os.path.join(os.getcwd(), temp_file)
    # save the transcript, response, and og query to the file using json
    with open(temp_path, 'w') as f:
        json.dump({"transcript": transcript, "response": response, "og_query": query}, f)
        print(f'Temporary file updated: {temp_path}')

    return temp_path

def get_difficulty_and_time():
    # tempfile path
    temp_path = os.path.join(os.getcwd(), temp_file)
    # get the transcript and response from the cache file
    with open(temp_path, 'r') as f:
        data = json.load(f)
    
    transcript = data["transcript"]
    response = data["response"]
    og_query = data["og_query"]
    # query gpt
    diff_query = f"Based on your previous response to the prompt '{og_query}', how difficult is this task and how estimate long would it take for the average homeowner? (example response: Difficulty: x/5, Time: x minutes)- only return in this format DO NOT PUT ANYTHING ELSE BESIDES THIS FORMAT TIME SHOULD BE A SINGULAR NUMBER OF YOUR BEST ESTIMATE."
    diff_response = query_gpt(diff_query, transcript=transcript, prev_response=response, max_tokens=50)
    # get the difficulty and time
    # based on example response , get difficulty value and time string
    diff = diff_response[diff_response.index("Difficulty:"): diff_response.index("/5")]
    time = diff_response[diff_response.index("Time:"):]
    # remove the words difficulty and time
    diff = diff.replace("Difficulty: ", "")
    time = time.replace("Time: ", "")
    return diff, time

def elaborate_step(step_text):
    # load in the temp file
    temp_path = os.path.join(os.getcwd(), temp_file)
    # get the transcript and response from the cache file
    with open(temp_path, 'r') as f:
        data = json.load(f)
    # elaborate on the step text by querying gpt
    elaborate_query = f"Elaborate on this step '{step_text}' in more detail in a clear and concise paragraph"
    elaborate_response = query_gpt(elaborate_query, transcript=data['transcript'], prev_response=data['og_query'], max_tokens=100)
    return elaborate_response

if __name__ == '__main__':
    query = "How would I go about building a shed?"
    response, yt_link = main_combined(query)
    for step in response:
        print(step)
    print(yt_link)
    diff, time = get_difficulty_and_time()
    print(diff)
    print(time)
    print(elaborate_step(response[1]))
