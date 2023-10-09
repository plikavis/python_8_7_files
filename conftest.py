import shutil
import zipfile

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

from examples.utils import TMP_PATH


@pytest.fixture
def our_browser():
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_PATH,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    yield driver

    shutil.rmtree(TMP_PATH)


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    os.mkdir('tmp')
    root = os.path.dirname(__file__)
    path = os.path.join(root, 'resources/')
    file_dir = os.listdir(path)
    with zipfile.ZipFile('tmp/test.zip', mode='w',
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file, arcname=file)

    yield
    pass
    os.remove('tmp/test.zip')
    os.rmdir('tmp')


