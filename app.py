from flask import Flask, render_template, request
from sense_emu import SenseHat
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')
   


@app.route('/send',methods=["POST"])
def send():
    sense = SenseHat()
    user = request.form['message']
    name = request.form['from']
    sense.show_message(user + "From" + name)
    return ('Message Received')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

