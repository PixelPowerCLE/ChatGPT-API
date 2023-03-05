import os
import PySimpleGUI as sg
# https://www.pysimplegui.org/
import openai

OPENIAKEY = os.getenv('OPENAI_KEY')
# How to set environmental variables
# https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html

openai.api_key = OPENIAKEY
messages = []

sg.theme('DarkTeal9')   # Add a touch of color
# Layout for the first window to setup the type of chatbot
layout = [  [sg.Text('What type of chatbot would you like to create?')],
            [sg.InputText(enable_events=True,key='ChatType')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Layout for the conversation with the chatbot
chatlayout = [  [sg.Text('Say hello to you new assistant!')],
                [sg.Output(size=(80,20))],
                [sg.InputText(enable_events=True,key='UserChat')],
                [sg.Button('Ok', visible=False, bind_return_key=True), sg.Button('Close')] ] # Button bound to enter key

# Create the first window
window = sg.Window('ChatGPT API Python GUI', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        system_msg = "What type of chatbot would you like to create?"
        messages.append({"role": "system", "content": system_msg})
        break

window.close()

# Create the second window
window = sg.Window('ChatGPT API Python GUI', chatlayout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks close
        break
    if event == 'Ok':
        messages.append({"role": "user", "content": window['UserChat'].get()})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print("\n" + reply + "\n")

window.close()
