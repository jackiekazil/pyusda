pyusda
======

Script and instructions to interact with USDA's API

### Run APIObject from the commandline
```
$ python pyusda.py http://api.data.gov/USDA/ERS/data/Arms/Surveys put_your_api_key_here
```

The first arg is the api_url. The second is your API_KEY.
```
$ python pyusda.py $API_URL $API_KEY
```
Where $API_URL is the url that you want to hit and $API_KEY is replaced with your API_KEY.

If you would like to capture the output run the following:
```
$ python pyusda.py 'data/Arms/Surveys' $API_KEY > output.json
```
The output.json file in this repo has an example of how the output would be stored.


### Example of usage from ipython, a python interpretor.
```python
In [1]: api_key = 'put_your_api_key_here'

In [2]: from pyusda import APIObject

In [3]: ap = APIObject('http://api.data.gov/USDA/ERS/data/Arms/Surveys', api_key)

In [4]: ap.url
Out[4]: 'http://api.data.gov/USDA/ERS/data/Arms/Surveys?api_key=wpe3bvzE0cO9VpVMSCfo6ULSq4ecjy2BKVZ6sOvF'

In [5]: ap.response
Out[5]: <Response [200]>

In [6]: ap.data
Out[6]:
{u'dataTable': [{u'surveyDesc': u'Crop production practices',
   u'survey_abb': u'CROP'},
  {u'surveyDesc': u'Farm finances', u'survey_abb': u'FINANCE'}],
 u'infoTable': [{u'message': u'NO ERROR', u'recordCount': 2}]}

In [7]: ap.data['dataTable']
Out[7]:
[{u'surveyDesc': u'Crop production practices', u'survey_abb': u'CROP'},
 {u'surveyDesc': u'Farm finances', u'survey_abb': u'FINANCE'}]

In [8]: for survey in ap.data['dataTable']:
   ...:         print survey
   ...:
{u'survey_abb': u'CROP', u'surveyDesc': u'Crop production practices'}
{u'survey_abb': u'FINANCE', u'surveyDesc': u'Farm finances'}
```
