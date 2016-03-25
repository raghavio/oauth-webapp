import requests
import urllib
from oauth_webapp import app


def get_oauth_provider(provider):
    def upper():
        return provider.upper()

    return app.config.get(upper())


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

    def get_thumbnail():
        if provider == "facebook":
            return "http://graph.facebook.com/{}/picture?type=large".format(fields["id"])

    thumbnail = get_thumbnail()
    fields["thumbnail"] = thumbnail
    data = {"fields": fields, "provider": provider}
    return data
