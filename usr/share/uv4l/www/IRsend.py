from flask import Flask, render_template, request
from os import curdir
from flask_basicauth import BasicAuth
import subprocess

# Simple command

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'your_username'
app.config['BASIC_AUTH_PASSWORD'] = 'your_password'

basic_auth = BasicAuth(app)

@app.route("/")
@basic_auth.required
def main():
    templateData = {}
    return render_template('WebRtcIR.html', **templateData)

@app.route("/WebRtcIR.html")
@basic_auth.required
def main_WebRtcIR():
    templateData = {}
    return render_template('WebRtcIR.html', **templateData)


# @app.route('/send/<button>')
@app.route('/send/')
@basic_auth.required
# def send_ir_command(button):
def send_ir_command():
    command = ['irsend','SEND_ONCE']
    remote = request.args.get('remote')
    btn = request.args.get('btn')
    command.append(remote)
    command.append(btn)
    command = " ".join(command)
    subprocess.call(command, shell=True)
    return "{} {} - OK".format(remote, btn)


if __name__ == "__main__":
    print(curdir)
    app.run(host='0.0.0.0', port=8092, debug=True, ssl_context=('/etc/uv4l/selfsign.crt', '/etc/uv4l/selfsign.key'))
    
