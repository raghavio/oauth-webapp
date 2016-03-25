from flask import render_template, redirect, request, session, url_for, jsonify
from oauth_webapp import app
from helpers import is_new_user, create_new_user
import oauth


@app.route("/")
def index():
    user_data = session.get("user_data")
    if user_data:
        if is_new_user(user_data["fields"]["email"]):
            create_new_user(user_data)
        return render_template("home.html")
    else:
        return render_template("index.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


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
        user_data = oauth.get_user_data(provider, token)
        if user_data:
            session["user_data"] = user_data
            return redirect(url_for("index"))
        else:
            pass  # An error occurred TODO
    elif "error" in request.args:
        pass  # User declined to give permissions


@app.route("/api/data", methods=["GET"])
def get_user_data():
    if "user_data" in session:
        return jsonify(session["user_data"])
    else:
        return redirect(url_for("index"))
