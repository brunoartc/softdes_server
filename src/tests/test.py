import pytest
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import softdes

lambda_handler = softdes.lambda_handler


teste1 = {'ndes': '1', 'code': '''
def desafio1(a):
    return 0
''', 'args': [[1]], 'resp': [0], 'diag': []}

teste2 = {'ndes': '2', 'code': '''
def desafio2(a):
    return a
''', 'args': [[1]], 'resp': [0], 'diag': ['a']}


teste3 = {'ndes': '1', 'code': '''
def desafio2(a):
    return a
''', 'args': [[1]], 'resp': [0], 'diag': []}

driver = webdriver.Firefox(executable_path="./geckodriver")


def test_01():
    assert (lambda_handler(teste1, '')) == ''

def test_02():
    driver.get("http://online:online@localhost:8080/?ID=2")
    assert "SoftDes" in driver.title

def test_03():
    assert (lambda_handler(teste2, '')) == 'a'

def test_04():
    driver.find_element_by_id("resposta").send_keys(os.getcwd() + "/res.py")
    btn = driver.find_elements_by_xpath('//button[@type="submit"]')
    btn[1].click()
    message = [i.text for i in driver.find_elements_by_xpath('//td')]
    assert "Erro" in message

def test_05():
    driver.find_element_by_id("resposta").send_keys(os.getcwd() + "/res.py")
    btn = driver.find_element_by_xpath('//button[@type="submit"]')
    btn.click()
    message = driver.find_element_by_xpath('//div[@role="alert"]')
    assert "sucesso" in message.text



def test_06():
    assert (lambda_handler(teste3, '')) == "Nome da função inválido. Usar 'def desafio1(...)'"