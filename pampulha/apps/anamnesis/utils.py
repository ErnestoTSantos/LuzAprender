import logging
from typing import Optional, Union

import requests


class Verification:
    @staticmethod
    def verificate_cep(cep: str) -> Union[Optional[tuple[bool]], tuple]:
        """
        Callback request payload:
        {
          "cep": "89010025",
          "state": "SC",
          "city": "Blumenau",
          "neighborhood": "Centro",
          "street": "Rua Doutor Luiz de Freitas Melro",
          "service": "viacep",
          "location": {
            "type": "Point",
            "coordinates": {
              "longitude": "-49.0629788",
              "latitude": "-26.9244749"
            }
          }
        }
        """

        logging.info("Initiating request to BrasilAPI")

        api_request = "https://brasilapi.com.br/"
        request_api = requests.get(f"{api_request}/api/cep/v2/{cep}")

        if request_api.status_code != 200:
            logging.exception("Problems making the request")
            return (False, None, None, None, None)

        cep_informations = request_api.json()

        return (
            cep_informations.get("cep"),
            cep_informations.get("state"),
            cep_informations.get("city"),
            cep_informations.get("neighborhood"),
            cep_informations.get("street"),
        )
