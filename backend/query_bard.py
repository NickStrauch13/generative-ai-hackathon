from bardapi import Bard
import os
from dotenv import load_dotenv
import requests
from bardapi import SESSION_HEADERS
import json
import re
import pprint
import google.generativeai as palm
from bardapi import BardCookies

# cookie_dict = {
#     "__Secure-1PSID": "cwgsO1wJkEzymwcVQATVGtt62xnmdyM8iORmGXseB2iClmEA4UUwHccKT0Tr4WHGxpMjcA.",
#     "__Secure-1PSIDTS": "sidts-CjEBNiGH7uexXNL43UqqkO-hGCVYMfoP0ptYv2WXneATvvnk9-ILX7AktVDXMe25mnkMEAA",
#     "__Secure-1PSIDCC": "ACA-OxOn8Y2IrkO7LW2F5j7TVUQ7jIRreL4MP7SA_ZCVF92EOG17fI_Vr1CvktqO6OAK2cFDQg",
# }


# session = requests.Session()
# token = "cwgsO1wJkEzymwcVQATVGtt62xnmdyM8iORmGXseB2iClmEA4UUwHccKT0Tr4WHGxpMjcA."
# session.cookies.set("__Secure-1PSID", "cwgsO1wJkEzymwcVQATVGtt62xnmdyM8iORmGXseB2iClmEA4UUwHccKT0Tr4WHGxpMjcA.")
# session.cookies.set( "__Secure-1PSIDCC", "ACA-OxOn8Y2IrkO7LW2F5j7TVUQ7jIRreL4MP7SA_ZCVF92EOG17fI_Vr1CvktqO6OAK2cFDQg")
# session.cookies.set("__Secure-1PSIDTS", "sidts-CjEBNiGH7uexXNL43UqqkO-hGCVYMfoP0ptYv2WXneATvvnk9-ILX7AktVDXMe25mnkMEAA")
# session.headers = SESSION_HEADERS


def use_bard(query, token = "", session = ""):
    load_dotenv()
    __Secure_1PSID = os.getenv('__Secure_1PSID')
    __Secure_1PSIDCC = os.getenv('__Secure_1PSIDCC')
    __Secure_1PSIDTS = os.getenv('__Secure_1PSIDTS')
    cookie_dict = {
        '__Secure-1PSID': __Secure_1PSID,
        '__Secure-1PSIDCC': __Secure_1PSIDCC,
        '__Secure-1PSIDTS': __Secure_1PSIDTS,
    }
    # bard = Bard(token = token,session=session)
    # bard = Bard(token_from_browser=True)
    bard = BardCookies(cookie_dict=cookie_dict)
    result = bard.get_answer(query)
    return result


def get_Palm():
    load_dotenv()
    token = os.getenv('PALM_API_KEY')
    palm.configure(api_key = token)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    print(model)

    # prompt = 'use Bard to help me find these Amazon items links: [brush, tongs, towel]'

    # completion = palm.generate_text(
    #     model=model,
    #     prompt=prompt,
    #     temperature=0,
    #     # The maximum length of the response
    #     max_output_tokens=1500,
    # )
    # print(completion.result)
    # Setting temperature=1 usually produces more zany responses!
    # response = palm.chat(messages='help me find these Amazon items links: [brush, tongs, towel]')
    response = palm.chat(messages="help me find these Amazon items links: [brush, tongs, towel]", temperature=0)
    print(response.last)
    return
    

def get_bard():
    load_dotenv()
    token = os.getenv('BARD_API_KEY')
    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", token)
    bard = Bard(token=token, session=session)
    query = 'help me find these Amazon items links: ["brush", "tongs", "towel"]'
    result = bard.get_answer(query)
    print(result)

def extract_item():
    data = {
        'content': 'Here are the links to the Amazon items you requested:\n\n**Brush**\n\n[Image of Amazon brush]\n\nElectric Toothbrush, Sonic Toothbrush with 5 Brushing Modes, IPX7 Waterproof Rechargeable Toothbrush with 3 Brush Heads, 4-Week Battery Life, Timer, Smart Reminder, for Adults and Kids: https://www.amazon.com/electric-toothbrush/s?k=electric+toothbrush\n\n**Tongs**\n\n[Image of Amazon tongs]\n\nOXO Good Grips 12-Inch Locking Tongs with Silicone Tips: https://www.amazon.com/tongs/s?k=tongs\n\n**Towel**\n\n[Image of Amazon towel]\n\nAmazon Basics Quick-Dry Microfiber Sports Towel: https://www.amazon.com/towels/b?ie=UTF8&node=1063244\n\nPlease note that these are just a few examples, and there are many other great products available on Amazon. I hope this helps!'
    }

    data = json.loads(json.dumps(data))
    links = []
    content = data['content'].split('\n\n')
    for i in range(len(content)):
        if content[i].startswith('**'):
            product_name = content[i].strip('**')
            product_link = content[i+1].split(': ')[-1]
            links.append({product_name: product_link})
    for link in links:
        for product, url in link.items():
            print(f'{product}: {url}')

def extract_links(parse_data):
    if(parse_data):
        data = parse_data
    else:
        data = {
            'content': 'Here are the links to the Amazon items you requested:\n\n**Brush**\n\n[Image of Amazon brush]\n\nElectric Toothbrush, Sonic Toothbrush with 5 Brushing Modes, IPX7 Waterproof Rechargeable Toothbrush with 3 Brush Heads, 4-Week Battery Life, Timer, Smart Reminder, for Adults and Kids: https://www.amazon.com/electric-toothbrush/s?k=electric+toothbrush\n\n**Tongs**\n\n[Image of Amazon tongs]\n\nOXO Good Grips 12-Inch Locking Tongs with Silicone Tips: https://www.amazon.com/tongs/s?k=tongs\n\n**Towel**\n\n[Image of Amazon towel]\n\nAmazon Basics Quick-Dry Microfiber Sports Towel: https://www.amazon.com/towels/b?ie=UTF8&node=1063244\n\nPlease note that these are just a few examples, and there are many other great products available on Amazon. I hope this helps!'
        }
    data = json.loads(json.dumps(data))
    amazon_links = re.findall(r'https://www.amazon.com/\S+', data['content'])
    for link in amazon_links:
        print(link)


if __name__ == "__main__":
    query = "Assume that you are a Google search engine. You must find these Amazon items links: [brush, tongs, towel, gloves]."
    res = use_bard(query)
    # print(res)
    # extract_links(res)
    print(res['content'])

    
