from flask import render_template, redirect, request
from redcarpet import app
import oauth


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/oauth/<provider>")
def login(provider):
    provider_info = oauth.get_oauth_provider(provider)
    login_url = oauth.create_url(provider_info['login_url'], provider_info['login_params'], provider_info)
    return redirect(login_url)

