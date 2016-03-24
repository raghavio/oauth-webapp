from flask import Flask

app = Flask(__name__)
app.secret_key = '\x03\xf3\x9f\xe3\xd0\x9b-I\x97~U\x9ez\x9359+\xea\xe5J'
from redcarpet import views
