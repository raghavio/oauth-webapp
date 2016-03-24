import urllib


def create_url(url, params):
    return url + '?' + urllib.urlencode(params)
