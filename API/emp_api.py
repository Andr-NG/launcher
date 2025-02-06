import requests
import logging
import data
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


load_dotenv()
logger = logging.getLogger("my_logger")


class EMP:
    """Emergency panel endpoints
    """

    def __init__(self, url: str) -> None:
        self.url = url
        self.env = os.getenv(f"EMP_{os.getenv('ENV')}")
        self.basic_auth = HTTPBasicAuth(username='admin', password=os.getenv(self.env))

    def get_email_token(self) -> dict:
        """EMP get email token

        Args:
            email (str): email

        Returns:
            dict: EMP get token response
        """
        params = {'email': os.getenv('email')}
        URL = self.url + '/emp/verification_token'
        try:
            data = requests.get(url=URL, params=params, auth=self.basic_auth)
            logger.info(
                f"Receiving response from {self.get_email_token.__name__}: , {data.json()}"
            )
            return data.json()
        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise

    def set_restrictions(self, workspace_id: str) -> dict:
        """

        Args:
            workspace_id (str): workspace id

        Returns:
            dict: set restrictions response
        """
        body = data.RESTRICTIONS
        body['workspace_id'] = workspace_id
        try:
            URL = self.url + '/emp/restrictions'
            res = requests.post(url=URL, json=body, auth=self.basic_auth)
            logger.info(
                f"Receiving response from {self.set_restrictions.__name__}: , {data.json()}"
            )
            return res.json()
        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise
