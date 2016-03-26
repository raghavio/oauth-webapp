"""
Handles all the OAuth related stuff.
Like exchanging auth code for access token and getting making API calls to get user data. Basically just that.
"""
import requests
import urllib
from oauth_webapp import app


def get_oauth_provider(provider):
    """
    Gets the oauth configuration of the provided provider.
    :param provider: Provider. Like facebook, google etc.
    :return: A dictionary with all the OAuth configuration.
    """

    def upper():
        """
        Uppercase the 'provider' string because configuration key is stored in CAPS in config file.
        """
        return provider.upper()

    return app.config.get(upper())


def get_access_token(provider, code):
    """
    Gets access token in exchange of authorization code by making a POST request to token API url.
    :param provider: provider
    :param code: authorization code
    :return: Response which contains token and extra details like expire time etc.
    """
    provider_info = get_oauth_provider(provider)

    payload = {"code": code}
    for param in provider_info["token_params"]:
        payload[param] = provider_info[param]

    resp = requests.post(provider_info["token_url"], data=payload)
    return resp.json()


def create_url(url, params, provider_info):
    """
    Creates a url with params encoded as query parameters.
    :param url: URL to which we append query parameters.
    :param params:  List of parameters to append.
    :param provider_info: Provider configuration. We use to get values of the params.
    :return: URL with query parameters appended to it.
    """
    values = {}
    for param in params:
        values[param] = provider_info[param]
    return url + "?" + urllib.urlencode(values)


def get_user_data(provider, token):
    """
    Gets user data by making call to provider's API.
    :param provider: you know what
    :param token: Access token we got by exchanging authorization code.
    :return: A dictionary object containing the user data. Structure given below.

            {
                "fields": {"name": ..., "email": ...},
                "provider": <provider>
            }
    """
    provider_info = get_oauth_provider(provider)
    payload = {"access_token": token}

    params = provider_info.get("user_data_params")
    if params:
        payload.update(provider_info["user_data_params"])

    resp = requests.get(provider_info["user_data_api"], params=payload)
    fields = resp.json()

    def get_thumbnail():
        """
        This is an inner function exclusive to just the outer function. So better to put it here.
        Anyway, this gets thumbnail (profile image) which will be different for different providers. Hence this
        function.
        :return: URL to thumbnail
        """
        if provider == "facebook":
            return "http://graph.facebook.com/{}/picture?type=large".format(fields["id"])

    thumbnail = get_thumbnail()
    fields["thumbnail"] = thumbnail
    data = {"fields": fields, "provider": provider}
    return data
