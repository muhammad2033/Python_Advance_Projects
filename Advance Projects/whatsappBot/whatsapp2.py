from flask import Flask, request
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
  data = request.form
  # Process incoming message here
  return '', 200

@app.route('/webhook', methods=['POST'])
def webhook():
  data = request.form
  message = data['Body']
  response = generate_response(message)
  send_message(response, data['From'])
  return '', 200

def generate_response(message):
  # Generate response based on message content
  return 'Hello, world!'
import twilio
def send_message(message, recipient):
  # Send a message using the Twilio API
  from twilio.rest import Client
  account_sid = 'YOUR_ACCOUNT_SID'
  auth_token = 'YOUR_AUTH_TOKEN'
  client = Client(account_sid, auth_token)
  message = client.messages.create(
    from_='whatsapp:+923156526523',
    body=message,
    to='whatsapp:' + recipient
  )


if __name__ == '__main__':
    app.run()