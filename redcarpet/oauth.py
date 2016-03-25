import requests
import urllib

facebook = {
    "name": "Facebook",
    "client_id": "210978529266397",
    "client_secret": "a0facebf9f04574e9776bd5cd15a8464",
    "redirect_uri": "http://localhost:5000/oauth/facebook",
    "scope": "email",
    "login_url": "https://www.facebook.com/dialog/oauth",
    "login_params": ["client_id", "redirect_uri", "scope"],
    "token_url": "https://graph.facebook.com/v2.3/oauth/access_token",
    "token_params": ["client_id", "redirect_uri", "client_secret"],
    "user_data_api": "https://graph.facebook.com/v2.5/me",
    "user_data_params": {"fields": "name, first_name, last_name, email, gender, link, id"}
}


def get_oauth_provider(provider):
    if provider == "facebook":
        return facebook


def get_access_token(provider, code):
    provider_info = get_oauth_provider(provider)
    url = create_url(provider_info["token_url"], provider_info["token_params"], provider_info)
    resp = requests.get(url, params={"code": code})
    return resp.json()


def create_url(url, params, provider_info):
    values = {}
    for param in params:
        values[param] = provider_info[param]
    return url + "?" + urllib.urlencode(values)


def get_user_data(provider, token):
    provider_info = get_oauth_provider(provider)
    payload = {"access_token": token}
    payload.update(provider_info["user_data_params"])
    resp = requests.get(provider_info["user_data_api"], params=payload)
    fields = resp.json()

    def get_thumbnail(provider, id):
        if provider == "facebook":
            return "http://graph.facebook.com/{}/picture?type=large".format(id)

    thumbnail = get_thumbnail(provider, fields["id"])
    data = {"fields": fields, "thumbnail": thumbnail}
    return data
