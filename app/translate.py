try:
    import httplib  # Python 2
except ImportError:
    import http.client as httplib  # Python 3
try:
    from urllib import urlencode  # Python 2
except ImportError:
    from urllib.parse import urlencode  # Python 3
import json
from xml.etree import ElementTree
from flask_babel import gettext
from config import MS_TRANSLATOR_CLIENT_SECRET

def microsoft_translate(text, sourceLang, destLang):
    if MS_TRANSLATOR_CLIENT_SECRET == '':
       return gettext('Error: translation service not configured.')
    try:
        # get access token
        token_service_url = 'api.cognitive.microsoft.com'
        request_headers = {'Ocp-Apim-Subscription-Key': MS_TRANSLATOR_CLIENT_SECRET}
        conn = httplib.HTTPSConnection(token_service_url)
        conn.request('POST', '/sts/v1.0/issueToken', headers=request_headers)
        response = conn.getresponse()
        #response.raise_for_status()
        #print(response.read())
        token = response.read()
        #print(token)

        # translate
        conn = httplib.HTTPSConnection('api.microsofttranslator.com')
        request_headers = {"Authorization ": 'Bearer ' + token}
        #print(request_headers)
        params = {'from': sourceLang,
                  'to': destLang,
                  'text': text.encode("utf-8")}
        conn.request("GET", '/V2/Ajax.svc/Translate?' + urlencode(params), headers=request_headers)
        response = conn.getresponse().read().decode('utf-8')
        #print(response)
        return response #["response"]

    except:
        return gettext('Error: Unexpected error.')
