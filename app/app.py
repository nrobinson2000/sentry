from sentry import sentry
from flask import Flask, request, render_template

DIRECTIONS = ['left', 'right', 'up', 'down']

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/move', methods=['POST'])
def move():
    direction = request.args.get('direction')

    if direction not in DIRECTIONS:
        return '', 400

    if direction == 'left':
        sentry.left()
    elif direction == 'right':
        sentry.right()
    elif direction == 'up':
        sentry.up()
    elif direction == 'down':
        sentry.down()

    return ''

@app.route('/api/stop', methods=['POST'])
def stop():
    sentry.stop()

    return ''

@app.route('/api/fire', methods=['POST'])
def fire():
    sentry.fire()

    return ''


@app.route('/api/toggle', methods=['POST'])
def toggle():
    sentry.toggle()

    return ''





app.run('0.0.0.0', debug=True)
