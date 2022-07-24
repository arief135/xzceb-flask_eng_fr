"""Module English/French translator"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Translate English text to French
    """
    if english_text is None:
        return None

    result = language_translator.translate(
        text=english_text, model_id="en-fr"
    ).get_result()
    if len(result["translations"]) > 0:
        return result["translations"][0]["translation"]
    else:
        return None


def french_to_english(french_text):
    """
    Translate French text to English
    """
    if french_text is None:
        return None

    result = language_translator.translate(
        text=french_text, model_id="fr-en"
    ).get_result()
    if len(result["translations"]) > 0:
        return result["translations"][0]["translation"]
    else:
        return None
