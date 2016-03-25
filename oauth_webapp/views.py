import json
from flask import render_template, redirect, request, session, url_for, jsonify
from oauth_webapp import app
import oauth


def is_new_user(email):
    with open("database", "r") as database:
        for user in database.readlines():
            user_data = json.loads(user)
            if user_data["email"] == email:
                return False
    return True


def create_new_user(user_data):
    with open("database", "a") as database:
        fields = user_data["fields"]

        provider = user_data["provider"]
        email = fields["email"]
        user_id = fields["id"]
        name = fields["name"]

        data_to_store = {"provider": provider, "email": email, "id": user_id, "name": name}

        database.write(json.dumps(data_to_store))
        database.write("\n")


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
