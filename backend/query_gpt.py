import openai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
# set the API key
openai.api_key = os.getenv('OPENAI_API_KEY')


# make funciton to query GPT-3.5
def query_gpt(prompt, engine='gpt-3.5-turbo', max_tokens=100, temperature=0.5, top_p=1, frequency_penalty=0, presence_penalty=0, stop=None, best_of=1, n=1, stream=False, logprobs=None, echo=False):
    response = openai.ChatCompletion.create(
        model=engine,
        messages=[
            {
                "role": "system",
                "content": "You are a chat bot that is here to help with problems around the house ."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop,
        n=n,
    )
    return response


if __name__ == '__main__':
    prompt = "My toilet is broken, what should I do?"
    response = query_gpt(prompt)
    print(response)
    text = response.choices[0].message.content
    print(text)