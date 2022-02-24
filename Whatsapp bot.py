
from flask import Flask, Request
import requests
from twilio.twiml.messaging_response import MessagingResponse
app =Flask(__name__)

@app.route('/mybot', methods =['POST'])

def mybot():
    incoming_msg = Request.values.get('Body','').lower()
    resp= MessagingResponse()
    msg=resp.message()
    respond = False
    if 'Hi' in incoming_msg:
        msg.body('Hello, I am a bot')
   
    return str(resp)
if   __name__ == "_main_" :
    app.run()










    