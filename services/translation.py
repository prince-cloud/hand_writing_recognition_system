from http import HTTPStatus
from typing import Optional, Tuple
from translate import Translator
from django.conf import settings
import requests

translator = Translator(to_lang="Spanish")
translation = translator.translate("Good Morning!")

print(translation)


class TwiTranslator:
    url = "https://translation-api.ghananlp.org/v1/translate"
    url = "https://translation-api.ghananlp.org/v1/translate"
    primary_key = settings.NLP_PRIMARY_KEY

    def translate(self, text, language="en-tw") -> Tuple[str, Optional[str]]:
        data = {
            "in": text,
            "lang": language,
        }
        headers = {
            "Content-Type": "application/json",
            "Ocp-Apim-Subscription-Key": self.primary_key,
            "Cache-Control": "no-cache",
        }
        print(data)
        print(headers)
        response = requests.post(self.url, json=data, headers=headers)
        if response.status_code == HTTPStatus.OK:
            return response.text, None
        print(response.text)
        return "", response.text
