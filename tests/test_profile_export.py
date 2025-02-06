from typing import Generator
from pytest import FixtureRequest
from pydantic import ValidationError
from models.launcher.profile_export_status_response import ProfileExportStatusResponse as pesr
import API
import logging

logger = logging.getLogger("my_logger")


class TestExportProfile:

    def test_export_profile(
        self, create_profile: Generator,
        launcher_api: API.Launcher, sign_in: tuple, request: FixtureRequest
    ):
        logger.info(f"Executing {request.node.name}")
        logger.info("Exporting profile")
        token, _ = sign_in
        pid = create_profile[0]

        try:
            resp_data = launcher_api.export_profile(token=token, pid=pid)
            response = pesr(**resp_data)
            assert response.status.http_code == 200, 'Wrong http code'
            assert response.status.message == 'Export in progress'

            assert response.data.profile_id == pid
            assert response.data.status == 'running'

        except (ValidationError, AssertionError) as e:
            logger.error("Validation or Assertion error occurred: %s", e)
            raise
        except Exception as e:
            logger.error("Unenxpected error occured: %s", e)
            raise
        finally:
            logger.info(f"Finishing {request.node.name}")
