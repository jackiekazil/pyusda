import sys
from collections import namedtuple

import requests


class APIObject(object):
    """
    API Objects pulls data and stores the response.
    """

    def __init__(self, api_url, api_key):

        self.url = '%s?api_key=%s' % (api_url, api_key)
        self.response = requests.get(self.url)
        self.data = self.response.json()


if __name__ == "__main__":
    """
    Run APIObject from the commandline:
    $ python pyusda.py http://api.data.gov/USDA/ERS/data/Arms/Surveys put_your_api_key_here

    The first arg is the api_url. The second is your API_KEY.
    $ python pyusda.py $API_URL $API_KEY

    Where $API_URL is the url that you want to hit and $API_KEY is replaced with your API_KEY.

    If you would like to capture the output run the following:
    $ python pyusda.py 'data/Arms/Surveys' $API_KEY > output.json

    """
    import pprint
    ap = APIObject(sys.argv[1], sys.argv[2])
    pprint.pprint(ap.data)