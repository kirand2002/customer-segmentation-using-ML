from flask import Flask, request, make_response

# init app.
application = app = Flask(__name__, template_folder='../templates',static_folder='../static')
app.config['SECRET_KEY'] = 'super secret key'
