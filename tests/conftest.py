# flake8: noqa
import pytest
import logging
import API
import utils

# Create a logger with a name specific to your project
logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

# Create a handler and a formatter (console/file handler as needed)
handler = logging.FileHandler(filename="my_logs.log", mode="w")
formatter = logging.Formatter(
    fmt="%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]",
    datefmt="%d/%m/%Y %H:%M:%S",
)
handler.setFormatter(formatter)
logger.addHandler(handler)

# Avoid duplicating logs
logger.propagate = False

@pytest.fixture(scope="session")
def config() -> utils.ConfigProvider:
    """Setting up a config provider

    Returns:
        utils.ConfigProvider: ConfigProvider class
    """
    return utils.ConfigProvider()


@pytest.fixture(scope="session")
def mlx_api(config: utils.ConfigProvider) -> API.MLX:
    logger.info("MLX API instantiated")
    URL = config.get_url()
    return API.MLX(url=URL)


# @pytest.fixture(scope="session")
# def emp_api(config: utils.ConfigProvider) -> API.EMP:
#     logger.info("EMP API instantiated")
#     URL = config.get_url()
#     return API.EMP(url=URL)


@pytest.fixture(scope="session")
def launcher_api(config: utils.ConfigProvider) -> API.Launcher:
    logger.info("Launcher API instantiated")
    URL = config.get_launcher_url()
    return API.Launcher(url=URL)
