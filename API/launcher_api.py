import logging
import ssl
import requests
from utils import ConfigProvider
from data.profile_data import IMPORT_PROFILE_DATA
from models import launcher
from API.shared_vars import SharedVars

logger = logging.getLogger('my_logger')
config = ConfigProvider()


class Launcher(SharedVars):
    """Launcher API endpoints

    Args:
        SharedVars (class): shared states
    """

    def __init__(self, url: str) -> None:
        self.url = url
        self.HEADERS = config.get_headers(super().get_var('access_token'))

    def start_profile(self, folder_id: str, profile_id: str) -> launcher.Response:
        """Start profile

        Args:
            folder_id (str): folider ID
            profile_id (str): profile ID

        Returns:
            Response: profile start response
        """

        URL = self.url + f"/profile/f/{folder_id}/p/{profile_id}/start"
        try:
            data = requests.get(url=URL, headers=self.HEADERS, verify=False)
            logger.info(
                f"Receiving response from {self.start_profile.__name__}: {data.json()}"
            )
            parsed = launcher.Response(**data.json())
            return parsed

        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise

    def start_quick_profile(self, profile_param) -> launcher.Response:
        URL = self.url + '/profile/quick'
        body = launcher.QuickProfile(**profile_param)
        try:
            data = requests.post(
                url=URL, headers=self.HEADERS, data=body.to_json()
            )
            logger.info(
                f"Receiving response from {self.start_quick_profile.__name__}: {data.json()}"
            )
            parsed = launcher.Response(**data.json())
            return parsed

        except requests.exceptions.SSLError as e:
            logger.error(
                f"SSL ceftification verification error {e}. Re-trying with verification skipped"
            )
            data = requests.post(
                url=URL, headers=self.HEADERS, data=body.to_json(), verify=False)
            logger.info(
                f"Receiving response from {self.start_quick_profile.__name__}: {data.json()}"
            )
            parsed = launcher.Response(**data.json())
            return parsed

        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise

    def get_launcher_version(self) -> launcher.VersionResponse:
        URL = self.url + '/version'
        try:
            data = requests.get(url=URL)
            logger.info(
                f"Receiving response from {self.get_launcher_version.__name__}: {data.json()}"
            )
            parsed = launcher.VersionResponse(**data.json())
            return parsed

        except requests.exceptions.SSLError as e:
            logger.error(
                f"SSL ceftification verification error {e}. Re-trying with verification skipped"
            )
            data = requests.get(url=URL, verify=False)
            logger.info(
                f"Receiving response from {self.get_launcher_version.__name__}: {data.json()}"
            )
            parsed = launcher.VersionResponse(**data.json())
            return parsed

        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise

    def stop_profile(self, profile_id: str) -> launcher.Response:
        """Stop profile

        Args:
            profile_id (str): profile ID

        Returns:
            Response: stop profile reponse
        """
        URL = self.url + f"/profile/stop/p/{profile_id}"
        try:
            data = requests.get(url=URL, headers=self.HEADERS)
            logger.info(
                f"Receiving response from {self.stop_profile.__name__}: , {data.json()}"
            )
            parsed = launcher.Response(**data.json())
            return parsed

        except ssl.SSLCertVerificationError as e:
            logger.error(
                f"SSL ceftification verification error {e}. Re-trying with verification skipped"
            )
            data = requests.get(url=URL, headers=self.HEADERS, verify=False)
            logger.info(
                f"Receiving response from {self.stop_profile.__name__}: , {data.json()}"
            )

        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise

    def stop_all_profiles(self) -> launcher.Response:
        """Stop all profiles

        Returns:
            Response: stop profile reponse
        """
        URL = self.url + '/profile/stop_all'
        params = {'type': 'all'}
        try:
            data = requests.get(url=URL, headers=self.HEADERS, params=params)
            logger.info(
                f"Receiving response from {self.stop_all_profiles.__name__}: {data.json()}"
            )
            parsed = launcher.Response(**data.json())
            return parsed

        except requests.exceptions.SSLError as e:
            logger.error(
                f"SSL ceftification verification error {e}. Re-trying with verification skipped"
            )
            data = requests.get(
                url=URL, headers=self.HEADERS, params=params, verify=False
            )
            logger.info(
                f"Receiving response from {self.stop_all_profiles.__name__}: {data.json()}"
            )
            parsed = launcher.Response(**data.json())
            return parsed

        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise

    def retrieve_profile_status(self) -> launcher.ProfileStatusesResponse:
        """Retrieve profile status

        Returns:
            ProfileStatusesResponse: get status response
        """
        URL = self.url + '/profile/statuses'
        try:
            data = requests.get(url=URL, headers=self.HEADERS)
            logger.info(
                f"Receiving response from {self.retrieve_profile_status.__name__}: , {data.json()}"
            )
            parsed = launcher.ProfileStatusesResponse(**data.json())
            return parsed

        except requests.exceptions.SSLError as e:
            logger.error(
                f"SSL ceftification verification error {e}. Re-trying with verification skipped"
            )
            data = requests.get(url=URL, headers=self.HEADERS, verify=False)
            logger.info(
                f"Receiving response from {self.retrieve_profile_status.__name__}: , {data.json()}"
            )
            parsed = launcher.ProfileStatusesResponse(**data.json())
            return parsed

        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise

    def import_cookies(
        self, cookies: str, xpass_load: bool = False
    ) -> launcher.Response:
        """_summary_

        Args:
            cookies (str): cookies as JSON string
            xpass_load (bool, optional): XPASS flag. Defaults to False.

        Returns:
            dict: import cookies response
        """
        URL = self.url + "/cookie_import"
        try:
            body = launcher.CookieImport(
                profile_id=self.profile_id,
                folder_id=self.folder_id,
                cookies=cookies,
                import_advanced_cookies=xpass_load,
            )
            data = requests.post(url=URL, data=body.to_json(), headers=self.HEADERS)
            logger.info(
                f"Receiving response from {self.import_cookies.__name__}: , {data.json()}"
            )
            return launcher.Response(**data.json())
        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise

    def export_profile(self) -> dict:
        """Export profile

        Returns:
            dict: export profile response
        """
        URL = self.url + f"/profile/{self.folder_id}/export"
        try:
            data = requests.post(url=URL, headers=self.HEADERS)
            logger.info(
                f"Receiving response from {self.export_profile.__name__}: , {data.json()}"
            )
            return data.json()
        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise

    def import_profile(self) -> dict:
        """Import profile

        Returns:
            dict: import profile response
        """
        URL = self.url + '/profile/export'
        try:
            path = IMPORT_PROFILE_DATA['import_path']
            file_path = f"{path}{self.profile_id}.zip"
            data = requests.post(url=URL, headers=self.HEADERS)
            logger.info(
                f"Receiving response from {self.import_profile.__name__}: , {data.json()}"
            )
            return data.json()
        except Exception as e:
            logger.error("Unexpected error occurred: %s", e)
            raise
