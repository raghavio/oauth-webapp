from flask import render_template, redirect, request, session
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


@app.route("/oauth/<provider>")
def oauth_callback(provider):
    if "code" in request.args:
        code = request.args["code"]
        token_data = oauth.get_access_token(provider, code)
        token = token_data['access_token']
    elif "error" in request.args:
        pass
