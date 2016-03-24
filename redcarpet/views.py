from flask import render_template, redirect
from redcarpet import app
import oauth
import utils


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/oauth/<provider>")
def login(provider):
    provider_info = oauth.get_oauth_provider(provider)
    login_url = utils.create_url(provider_info['login_url'], provider_info['login_data'])
    return redirect(login_url)
