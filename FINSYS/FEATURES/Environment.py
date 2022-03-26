from behave import fixture,use_fixture, model
from selenium import webdriver
import os

import logging as L

def log(level,message,file):
	L.basicConfig(level=L.INFO,filename=file,filemode="a",
				  format="%(asctime)-12s %(levelname)s %(message)s",
				  datefmt="%d-%m-%Y %H:%M:%S")
	if level == "INFO": L.info(message)
	if level == "WARNNG": L.warning(message)
	if level == "ERROR": L.error(message)
	if level == "CRITICAL": L.critical(message)

"""
def before_all(context):
    print(context)
    browsername=context.config.userdata['browser']
    print(browsername)
    if browsername=="ch":
       driver=webdriver.Chrome(context.config.userdata["ch_webdriver_exe"])
       context.driver=driver
    if browsername=="ie":
       driver=webdriver.Ie(context.config.userdata["ie_webdriver_exe"])
       context.driver=driver
"""

def after_all(context):
	context.browser.close()

