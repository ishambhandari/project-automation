import sys
from selenium import webdriver
import os

path_to_project = "/home/isham/Documents/"
browser = webdriver.Firefox()
browser.get('https://github.com/login')
username = "ishambhandari"
def launch():
    projectName = str(sys.argv[1])
    os.makedirs(path_to_project + str(projectName))
    browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(username)
    browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys(#github password here)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    browser.get('https://github.com/new')
    browser.find_elements_by_xpath("//*[@id='repository_name']")[0].send_keys(projectName)
    browser.find_element_by_css_selector('button.btn btn-primary first-in-line').click()
    
    
   
launch()
 # 
    # browser.get('https://github.com/ishambhandari/' + projectName + '/settings')
    # browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0].click()
    # browser.find_elements_by_xpath(
    #     '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(reponame)
    # browser.find_elements_by_xpath(
    #     '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    # browser.get("https://github.com/" + username)
