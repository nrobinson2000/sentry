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

@app.route('/api/toggle-light', methods=['POST'])
def toggle_light():
    sentry.toggle_light()

    return ''

@app.route('/api/light-color', methods=['POST'])
def light_color():
    args = request.args

    r = args.get('r')
    g = args.get('g')
    b = args.get('b')

    if r and g and b and r.isdigit() and g.isdigit() and b.isdigit():
        r = int(r)
        g = int(g)
        b = int(b)

        sentry.light_on(r, g, b)

        return ''

    return '', 400


app.run('0.0.0.0', 80)
