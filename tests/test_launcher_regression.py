import hashlib
import json
import pytest
import websocket
import API
import ssl
import logging
import time
import os
import pathlib
import data
from pytest import FixtureRequest
from models import MLX as mlx_models
from models import launcher

logger = logging.getLogger("my_logger")
path = pathlib.Path()
home_dir = path.home()


class TestLauncherRegression:

    def test_sign_in(self, request: FixtureRequest, mlx_api: API.MLX) -> None:
        logger.info(f"Executing {request.node.name}")
        email = os.getenv("EMAIL")
        hashed_pass = hashlib.md5(os.getenv("PASSWORD").encode()).hexdigest()
        response: mlx_models.SigninResponse = mlx_api.sign_in(
            login=email, password=hashed_pass
        )

        assert response.status.http_code == 200, "Failed sign-in attempt"
        logger.info(f"Finishing {request.node.name}")

    # @pytest.mark.skip(reason="Skipping this test for now.")
    def test_get_launcher_version(
        self, request: FixtureRequest, launcher_api: API.Launcher
    ) -> None:
        logger.info(f"Executing {request.node.name}")
        response: launcher.VersionResponse = launcher_api.get_launcher_version()

        assert response.status.http_code == 200, "Failed to get launcher version"
        assert response.data.env == os.getenv("ENV")
        logger.info(f"Finishing {request.node.name}")

    # @pytest.mark.skip(reason="Skipping this test for now.")
    def test_ws_connection(
        self, request: FixtureRequest, launcher_api: API.Launcher
    ) -> websocket.WebSocket | None:
        logger.info(f"Executing {request.node.name}")
        RETRIES = 3
        DELAY = 2
        URI = "wss://launcher.mlx.yt:45003/ws/data"

        # Connecting to websocket
        for attempt in range(1, RETRIES + 1):
            try:
                logger.info(f"Attempt {attempt} to set up websocket connection")
                ws = websocket.WebSocket()
                ws.connect(url=URI)

                assert ws.connected, "Connection failed"
                logger.info("Connection successfull!")
                break

            except websocket.WebSocketException as e:
                logger.error(f"Connection attempt {attempt} failed: {e}")
                if attempt < RETRIES:
                    logger.info("Attempting to connect again")
                    time.sleep(DELAY)
                else:
                    pytest.fail("Failed to connect to WebSocket after multiple retries")

            except ssl.SSLCertVerificationError as e:
                logger.error(
                    f"SSL Certification error: {e}. Re-connecting with verification skipped"
                )
                ws = websocket.WebSocket(sslopt={"cert_reqs": 0})
                ws.connect(url=URI)

                assert ws.connected, 'Connection failed'
                logger.info("Connection successfull!")
                break

            except Exception as e:
                logger.error(f"Unexpected error occurred: {e}")
                raise

        # Starting a QBP to populate messages.
        logger.info("Starting a QBP")
        response = launcher_api.start_quick_profile(
            profile_param=data.QUICK_PROFILE_SELENIUM
        )
        assert response.status.http_code == 200, 'Failed to start quick profile'

        ws_message = ws.recv()
        parsed = json.loads(ws_message)
        logger.info(f"Websocket messages are : {ws_message}")

        assert parsed, "Empty message"
        assert parsed["Profiles"][0]["IsQuick"] is True, 'Wrong value for IsQuick'
        assert parsed["Profiles"][0]["Status"] == "start_browser"
        ws.close()

    # @pytest.mark.skip(reason="Skipping this test for now")
    def test_get_folder_id(self, request: FixtureRequest, mlx_api: API.MLX) -> None:
        logger.info(f"Executing {request.node.name}")
        response = mlx_api.get_folder_id()

        assert response.status.http_code == 200, 'Failed to retrieve folder_id'
        logger.info(f"Finishing {request.node.name}")

    # @pytest.mark.skip(reason="Skipping this test for now.")
    def test_create_profile(self, mlx_api: API.MLX, request: FixtureRequest) -> None:
        logger.info(f"Executing {request.node.name}")
        body = data.PROFILE_GENERIC
        logger.info("Adding folder_id to the body request")
        body.update({"folder_id": mlx_api.folder_id})
        response = mlx_api.create_profile(profile_params=body)

        assert response.status.http_code == 201, 'Failed to create a profile'
        logger.info(f"Finishing {request.node.name}")

    # @pytest.mark.skip(reason="Skipping this test for now.")
    def test_launcher_profile(
        self, request: FixtureRequest, launcher_api: API.Launcher
    ) -> None:
        logger.info(f"Executing {request.node.name}")
        response: launcher.Response = launcher_api.start_profile(
                # profile_id=launcher_api.get_var('profile_id'),
                # folder_id=launcher_api.get_var('folder_id'),
                profile_id=launcher_api.profile_id,
                folder_id=launcher_api.folder_id,
            )
        assert response.status.http_code == 200, 'Failed to launch profile'
        logger.info(f"Finishing {request.node.name}")

    # def test_adapter_value(self, request: FixtureRequest, mlx_api: API.MLX):
    #     logger.info(f"Executing {request.node.name}")
    #     adapter_log_path = home_dir / 'mlx' / 'logs' / 'tester_a_mlx.log'
    #     baked_meta = {}
    #     start_meta = {}

    #     # Reading the adpater log file to validate
    #     try:
    #         with open(adapter_log_path, 'r') as log_file:
    #             for line in log_file:
    #                 try:
    #                     log_entry: dict = json.loads(line.rstrip())
    #                     if 'raw fingerprint' in log_entry.get('@message', 'No key found'):
    #                         baked_meta.update(log_entry['EXTRA_VALUE_AT_END'])

    #                     elif 'start request' in log_entry.get('@message', 'No key found'):
    #                         start_meta.update(log_entry['EXTRA_VALUE_AT_END'])

    #                 except json.JSONDecodeError:
    #                     logger.exception('An error occurred duting decoding')
    #                     continue
    #     except FileNotFoundError:
    #         logger.exception('No such file found. Check the path again')
        
    #     response = mlx_api.get_baked_meta()
    #     logger.info(f'Baked meta from the log file {baked_meta}')
    #     assert baked_meta == response

    # @pytest.mark.skip(reason="Skipping this test for now.")
    def test_profile_status_before_close(
        self, request: FixtureRequest, launcher_api: API.Launcher
    ) -> None:
        logger.info(f"Executing {request.node.name}")
        response = launcher_api.retrieve_profile_status()
        status_data = response.data

        assert response.status.http_code == 200, 'Failed to retrieve profile status'
        assert launcher_api.profile_id in status_data.states, 'Profile not found'
        assert status_data.active_counter.cloud >= 1, 'No cloud profile running'
        assert status_data.active_counter.quick >= 1, 'No quick profile running'
        assert status_data.states[launcher_api.profile_id].status == 'browser_running'

    # @pytest.mark.skip(reason="Skipping this test for now.")
    def test_close_all_profile(
        self, request: FixtureRequest, launcher_api: API.Launcher
    ) -> None:
        logger.info(f"Executing {request.node.name}")
        time.sleep(2)
        response: launcher.Response = launcher_api.stop_all_profiles()

        assert response.status.http_code == 200, "Failed to stop profile"
        logger.info(f"Finishing {request.node.name}")

    # @pytest.mark.skip(reason="Skipping this test for now.")
    def test_profile_status_after_close(
        self, request: FixtureRequest, launcher_api: API.Launcher
    ) -> None:
        logger.info(f"Executing {request.node.name}")
        response = launcher_api.retrieve_profile_status()
        status_data = response.data

        assert response.status.http_code == 200, 'Failed to retrieve profile status'
        assert len(status_data.states) == 0
        assert status_data.active_counter.cloud == 0, 'Cloud profile still running'
        assert status_data.active_counter.quick == 0, 'Quick profile still running'
        logger.info(f"Finishing {request.node.name}")
