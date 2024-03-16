from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send email
        try:
            server = smtplib.SMTP('smtp.example.com', 587)
            server.starttls()
            server.login('amponsahhayford42@gmail.com', 'Amponsahhayford4242')

            subject = 'Feedback from website'
            body = f'Name: {name}\nEmail: {email}\nMessage:\n{message}'
            msg = f'Subject: {subject}\n\n{body}'

            server.sendmail('amponsahhayford42@gmail.com', 'amponsahhayford42@gmail.com', msg)
            server.quit()

            return 'Thank you for your feedback!'
        except Exception as e:
            return f'Sorry, there was an error sending your feedback. Error: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
