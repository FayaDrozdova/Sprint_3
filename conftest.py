import pytest
from selenium import webdriver
from tests.data import Data


@pytest.fixture
def driver():
    return webdriver.Chrome()


@pytest.fixture
def data():
    return Data()
