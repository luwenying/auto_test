#coding:utf-8
import pytest

@pytest.fixture(scope="function")
def func_fixture():
    print("这个是前置方法")
    yield
    print("这个是后置方法")