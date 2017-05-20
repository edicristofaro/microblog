import requests
import json
from flask_babel import gettext
from config import MS_TRANSLATOR_CLIENT_SECRET

def microsoft_translate(text, sourceLang, destLang):
    if MS_TRANSLATOR_CLIENT_SECRET == '':
       return gettext('Error: translation service not configured.')
    try:
        # get access token
        token_service_url = 'https://api.cognitive.microsoft.com'
        request_headers = {'Ocp-Apim-Subscription-Key': MS_TRANSLATOR_CLIENT_SECRET}
        response = requests.post(token_service_url + '/sts/v1.0/issueToken', headers=request_headers)
        response.raise_for_status()
        token = response.content

        # translate
        translate_service_url = 'https://api.microsofttranslator.com'
        request_headers = {"Authorization ": 'Bearer ' + token}
        params = {#'from': sourceLang, #optional parameter
                  'to': destLang,
                  'text': text.encode("utf-8")}
        response = requests.get(translate_service_url + '/V2/Ajax.svc/Translate',params=params, headers=request_headers)
        return response.content #["response"]

    except:
       return gettext('Error: Unexpected error.')
