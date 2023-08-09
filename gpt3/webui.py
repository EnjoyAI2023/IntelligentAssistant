#-*-coding:utf-8-*-
# date:2023-08-02
# Author: Eric
# function: ChatGpt Text
'''
    文本输入提问，
    文本&语音形式回答。
'''
import sys
sys.setrecursionlimit(sys.getrecursionlimit()*5)
import os
from utils.utils import *
from utils.chatgpt_config import *
print("chatgpt_config well done !")
import gradio as gr
import random
import time
from threading import Thread
import pyttsx3


with gr.Blocks() as demo:
    gr.Image("./samples/slogan6.png",label="EnjoyAI")
    # chatbot = gr.Chatbot()
    chatbot = gr.Chatbot(label="EnjoyAI - ChatGPt 3.5:",color_map="lightblue")
    # msg = gr.Textbox()
    msg1 = gr.Textbox(inputs="text",label=["User"], info="用户提问")
    # msg2 = gr.Textbox(outputs="audio", label=["语音"])

    ck1 = gr.Checkbox(label=["开启语音播放"])
    clear = gr.ClearButton([msg1, chatbot])

    def respond(message,ck,chat_history):
        global tts_str
        #-----------------------------------------------------------------------
        try:
            ask_str = message
            ans = chatbot_response(ask_str)
            print("User : ",ask_str)
            print("ChatGpt : ",ans)
            bot_message = ans
            if(ck):
                tts_str = ans
        except:
            print(" WARNING: GPT Net Timeout 网络超时请重新提问。")
            bot_message = " WARNING: GPT Net Timeout 网络超时请重新提问。"

        #-----------------------------------------------------------------------
        chat_history.append((message,bot_message))
        time.sleep(1)
        # print("chat_history:",chat_history)
        return "", chat_history

    msg1.submit(respond, [msg1, ck1,chatbot], [msg1,chatbot])


def webui():
    demo.launch()

def tts():
    global tts_str
    #语音模块初始化
    engine = pyttsx3.init()
    while True:
        if len(tts_str)>0:
            say_text(engine,tts_str)
            print("tts : {}".format(tts_str))
            tts_str= ""
        time.sleep(1)

if __name__ == "__main__":


    global tts_str
    tts_str = ""

    t1 = Thread(target=webui)
    t2 = Thread(target=tts)

    # 启动线程运行
    t1.start()
    t2.start()

    # 等待所有线程执行完毕
    t1.join()  # join() 等待线程终止，要不然一直挂起
    t2.join()
