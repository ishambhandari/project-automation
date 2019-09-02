import sys
from selenium import webdriver
import os

path_to_project = "/home/isham/Documents/projects"
browser = webdriver.Firefox()
browser.get('https://github.com/')