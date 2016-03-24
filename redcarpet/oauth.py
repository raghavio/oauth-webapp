facebook = {
    "name": "Facebook",
    "login_url": "https://www.facebook.com/dialog/oauth",
    "login_data": {
        "client_id": "210978529266397",
        "redirect_uri": "http://localhost:5000/oauth/facebook",
        "scope": "email"
    },
    "secret": "a0facebf9f04574e9776bd5cd15a8464"
}


def get_oauth_provider(provider):
    if provider == "facebook":
        return facebook
