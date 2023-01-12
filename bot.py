import slack 
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ["SIGNING_SECRET"],"/slack/events", app)

client = slack.WebClient(token=os.environ["SLACK_TOKEN"])
## we do it this way so that we can keep .env file secret

client.chat_postMessage(channel='#test', text="Running!")
## ^ how to send a message
@slack_event_adapter.on("message")
def message(payload):
  ## payload is data that slack sends
  event = payload.get("event", {})
  user_id = event.get("user")

  if user_id == "U02CNPB3JQ2":
    client.chat_postMessage(channel='#test', text="alex sent a message")

  if user_id == "U040F1XJLHF":
    client.chat_postMessage(channel='#test', text="gavin sent a message")

  if user_id == "U031QGL11EU":
    client.chat_postMessage(channel='#test', text="ryan sent a message")

if __name__ == "__main__":
  app.run(debug=True) ## can change port through port=whatever
