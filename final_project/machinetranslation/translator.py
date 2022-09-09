import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION, authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(text):
    resp = language_translator.translate(text=text, model_id='en-fr')
    french=resp.get_result()
    return french['translations'][0]['translation']

def frenchToEnglish(text):
    resp = language_translator.translate(text=text, model_id='fr-en')
    eng=resp.get_result()
    return eng['translations'][0]['translation']

# print(englishToFrench('how are you?'))
