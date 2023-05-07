import logging
from typing import Optional, Union

import requests


class Verification:
    @staticmethod
    def verificate_cep(cep: str) -> Union[Optional[tuple[bool]], tuple]:
        logging.info("Initiating request to BrasilAPI")

        api_request = "https://brasilapi.com.br/"
        request_api = requests.get(f"{api_request}/api/cep/v2/{cep}")

        if request_api.status_code != 200:
            logging.exception("Problems making the request")
            return (False, None, None, None, None)

        cep_informations = request_api.json()

        return (
            cep_informations["cep"],
            cep_informations["state"],
            cep_informations["city"],
            cep_informations["neighborhood"],
            cep_informations["street"],
        )
