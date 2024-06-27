import time

import keyboard
import requests

with open('token.txt', 'r') as file:
    token = file.read()

msg = input("What's the message you would like to send? ")
channel = input("What's the channel id? ")
spam = input("Would you like to spam? ")

def send_message():
    global res_msg
    url = "https://discord.com/api/v9/channels/ " + channel + "/messages"

    payload = {
        "content": msg
    }

    headers = {
        "Authorization": token
    }
    res = requests.post(url, payload, headers=headers)
    if res.status_code == 400:
        print("I could message, maybe invalid channel id? ")
        exit()
    if res.status_code == 401:
        print("I could not message, maybe invalid token? ")
        exit()
    elif res.status_code == 200 or 204:
        print(f"Successfully sent message {msg}.")
    else:
        print(res_msg.status_code)

def do_it_again():
    print("Press F6 to send a message to that user again.")
    while True:
        try:
            if keyboard.is_pressed('F6'):
                send_message()
        except:
            exit()

def delayies():
    if spam in ("ye", "yes", "yeah", "yuh", "positive", "100%", "absolutely", "HELL YEAH", "y"):
        delay = int(input("Enter the delay in seconds: "))
        while True:
            send_message()
            time.sleep(delay)
    else:
        send_message()
        do_it_again()

if __name__ == '__main__':
    delayies()
