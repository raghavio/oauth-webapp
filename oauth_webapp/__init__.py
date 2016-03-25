from flask import Flask

app = Flask(__name__)
app.config.from_object("oauth_webapp.default_settings")

from oauth_webapp import views
