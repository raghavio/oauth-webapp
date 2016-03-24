import urllib

facebook = {
    "name": "Facebook",
    "client_id": "210978529266397",
    "client_secret": "a0facebf9f04574e9776bd5cd15a8464",
    "redirect_uri": "http://localhost:5000/oauth/facebook",
    "scope": "email",
    "login_url": "https://www.facebook.com/dialog/oauth",
    "login_params": ["client_id", "redirect_uri", "scope"]
}


def get_oauth_provider(provider):
    if provider == "facebook":
        return facebook


def create_url(url, params, provider_info):
    values = {}
    for param in params:
        values[param] = provider_info[param]
    return url + "?" + urllib.urlencode(values)
