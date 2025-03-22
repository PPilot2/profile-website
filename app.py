from flask import Flask, render_template, request
import os
import requests

MAILGUN_KEY = os.getenv('MAILGUN_KEY', 'MAILGUN_KEY')
print(MAILGUN_KEY)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        author = request.form['author']
        subject = request.form['subject']
        text = request.form['text']
        send_simple_message(author, subject, text)
        return render_template('index.html', message='Email sent!')
    return render_template('index.html', message=None)

def send_simple_message(author, subject, text):
  	return requests.post(
  		"https://api.mailgun.net/v3/sandbox06d7a2fefbf845779b7cd6b371703032.mailgun.org/messages",
  		auth=("api", MAILGUN_KEY),
  		data={"from": author,
			"to": "Prahalad Anand <prahaladanand6@gmail.com>",
  			"subject": subject,
  			"text": text})

if __name__ == '__main__':
    app.run(debug=True)