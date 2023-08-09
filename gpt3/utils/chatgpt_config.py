#-*-coding:utf-8-*-
# date:2023-08-02
# Author: Eric
# function: ChatGpt 3 config
import os
import openai
from utils.utils import load_json

assert (os.access("key_cfg.json",os.F_OK)), "no exist key_cfg"
gpt_key = load_json("key_cfg.json")
print("gpt_key:",gpt_key)
print("gpt_key len :",len(gpt_key))

openai.api_key = gpt_key["api_key"]
openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

def chatbot_response(msg):
    messages = []
    item =  {"role": "user", "content": msg}
    messages.append(item)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return str(response['choices'][0]['message']['content'])
