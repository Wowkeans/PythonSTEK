import pytest


@pytest.fixture()
def set_up():
    print('\nStart Test')
    yield
    print('\nFinish Test')

@pytest.fixture(scope="module")
def set_group():
    print('\nEnter System')
    yield
    print('\nExit System')