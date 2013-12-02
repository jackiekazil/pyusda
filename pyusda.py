import sys
from collections import namedtuple

import requests


class APIObject(object):
    # api_url Example: 'data/Arms/Surveys'
    # key Register here: 'https://api.data.gov/signup'

    def __init__(self, api_url, api_key, base_url='http://api.data.gov/USDA/ERS/'):

        self.url = self._setup_url(api_url, api_key, base_url)
        self.response = self._get_data()
        self.data = self.response.json()

    def _setup_url(self, api_url, api_key, base_url):
        url = '%s%s?api_key=%s' % (base_url, api_url, api_key)
        return url

    def _get_data(self):
        self.response = requests.get(self.url)
        return self.response


if __name__ == "__main__":
    import pprint
    ap = APIObject(sys.argv[1], sys.argv[2])
    pprint.pprint(ap.data)

python pyusda.py 'data/Arms/Surveys' $API_KEY
{u'dataTable': [{u'surveyDesc': u'Crop production practices',
                 u'survey_abb': u'CROP'},
                {u'surveyDesc': u'Farm finances', u'survey_abb': u'FINANCE'}],
 u'infoTable': [{u'message': u'NO ERROR', u'recordCount': 2}]}