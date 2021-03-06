#!/usr/bin/python
from bs4 import BeautifulSoup
from tablib import Dataset
import numpy as np
import excel
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, BakeryLinks, Bakery
from flask import session as login_session
import string
import excel
# IMPORTS FOR THIS STEP
import httplib2
import json
from flask import make_response
import requests
import pandas as pd
from tablib import Dataset
import numpy as np
import excel
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
# IMPORTS FOR THIS STEP
import pprint
import httplib2
import json
import sqlite3
from flask import make_response
import requests
import time

app = Flask(__name__)

APPLICATION_NAME = "api_scaner"

# Connect to Database and create database session
engine = create_engine('sqlite:///api_scaner.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



# You need install :
# pip install PyPDF2 - > Read and parse your content pdf
# pip install requests - > request for get the pdf
# pip install BeautifulSoup - > for parse the html and find all url hrf with ".pdf" final
from PyPDF2 import PdfFileReader
import requests
import io
from bs4 import BeautifulSoup
import requests
from collections import Counter
import base64


@app.route('/bakery')
def bakery_links():
    bakeries = session.query(BakeryLinks).all()
    return jsonify(bakeries=[r.serialize for r in bakeries])

@app.route('/bakery_data')
def bakery_data():
    bakeries_data = session.query(Bakery).all()
    return jsonify(bakeries=[r.serialize for r in bakeries_data])

#this function generate list of all pagination link for given url or category

def get_pagination(url):
    #url = 'https://eshop.tesco.com.my/groceries/en-GB/shop/fresh-food/bakery/all'
    filters = []
    mylinks = []
    while url not in filters:
        print(url)
        if url not in mylinks:
            mylinks.append(url)
        r = requests.get(url,headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
        soup = BeautifulSoup(r.text ,"lxml")
        url = soup.findAll('a', {'class': 'pagination--button prev-next'})
        if url in filters:
            filters.append(url)
            print(filters)
            print('scaner API got The all pagination Links for The URL')
            return mylinks
        filters.append(url)
        for x in url:
            if x:
                url = 'https://eshop.tesco.com.my' + x.get('href')
            else:
                break



# this function collect the proudcts for each link
def proudcts_collecter(pagination_list):
    projectData = []
    for link in pagination_list:
        # error handle partners
        try:
            print('Scaner API Fetch that URl ' + str(link))
            response = requests.get(link, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
            content = response.content
            soup = BeautifulSoup(response.content, 'html.parser')
            top_domain = 'https://eshop.tesco.com.my'
            proudcts = soup.find_all('a' , class_="product-image-wrapper")
            for proudct in proudcts:
                proudct_link = top_domain + proudct.get('href')
                if proudct_link not in projectData:
                    projectData.append(proudct_link)
                else:
                    continue
        # if no error print error and add exception for that error
        except Exception as e:
            print(e.message, e.args)
            print('we are going to wait 5 minutes until the app solve the error.')
            time.sleep(20)

            # this way app will be imune to stop
            try:
                print('We Solved Error Scaner API Fetch that URl ' + str(link))
                response = requests.get(link, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
                content = response.content
                soup = BeautifulSoup(response.content, 'html.parser')
                top_domain = 'https://eshop.tesco.com.my'
                proudcts = soup.find_all('a' , class_="product-image-wrapper")
                for proudct in proudcts:
                    proudct_link = top_domain + proudct.get('href')
                    if proudct_link not in projectData:
                        projectData.append(proudct_link)
                    else:
                        continue
            # if no error print error and add exception for that error
            except Exception as e:
                print(e.message, e.args)
                time.sleep(20)
                pirnt('We now Have wait 10 minutes now fetching: ' + str(link))
                response = requests.get(link, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
                content = response.content
                soup = BeautifulSoup(response.content, 'html.parser')
                top_domain = 'https://eshop.tesco.com.my'
                proudcts = soup.find_all('a' , class_="product-image-wrapper")
                for proudct in proudcts:
                    proudct_link = top_domain + proudct.get('href')
                    if proudct_link not in projectData:
                        projectData.append(proudct_link)
                    else:
                        continue


    return projectData




# this function accept one paramter which is list of prudcts links
def get_proudct_data(prudcts_links):
    projectData = []
    # start from Carbs and end with Protein

    for link in prudcts_links:
        url_part1 = link
        #url_part1 = 'https://eshop.tesco.com.my/groceries/en-GB/products/7000010766'
        try:
            response = requests.get(url_part1,headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
            content = response.content
            soup = BeautifulSoup(response.content, 'html.parser')
            proudct_image = soup.find('img' , class_="product-image").get('src')
            proudct_name = soup.find('h1' , class_="product-details-tile__title").getText()
            proudct_price = soup.find('span' , class_="value").getText()
            proudct = {"image": proudct_image,"name": proudct_name,"price": proudct_price}
            if proudct not in projectData:
                projectData.append(proudct)
            else:
                continue
        except Exception as e:
            print(e.message, e.args)
            print('API Scanner Blocked For A while Do not Worry We Will override that error Wait 5 minutes...')
            time.sleep(20)
            print('Continue from The Last point..')
            try:
                response = requests.get(url_part1,headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
                content = response.content
                soup = BeautifulSoup(response.content, 'html.parser')
                proudct_image = soup.find('img' , class_="product-image").get('src')
                proudct_name = soup.find('h1' , class_="product-details-tile__title").getText()
                proudct_price = soup.find('span' , class_="value").getText()
                proudct = {"image": proudct_image,"name": proudct_name,"price": proudct_price}
                if proudct not in projectData:
                    projectData.append(proudct)
                else:
                    continue
            except Exception as e:
                print(e.message, e.args)
                print('Again API Scanner Blocked For A while Do not Worry We Will override that error Wait 5 minutes...')
                print('Do not worry Nothing Can stop this API')
                time.sleep(400)
                print('Continue from The Last point..')
                response = requests.get(url_part1,headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
                content = response.content
                soup = BeautifulSoup(response.content, 'html.parser')
                proudct_image = soup.find('img' , class_="product-image").get('src')
                proudct_name = soup.find('h1' , class_="product-details-tile__title").getText()
                proudct_price = soup.find('span' , class_="value").getText()
                proudct = {"image": proudct_image,"name": proudct_name,"price": proudct_price}
                if proudct not in projectData:
                    projectData.append(proudct)
                else:
                    continue


    return projectData

@app.route('/target')
def targeter():
    # we call proudcts_collecter to get proudct links which accept list of pagination and give it category url

    #this list for baker
    the_bakery_list = []
    print('Welcome To API scaner We going to Start soon...')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3 Go..')

    # bakery category
    the_links = proudcts_collecter(get_pagination('https://eshop.tesco.com.my/groceries/en-GB/shop/fresh-food/bakery/all'))
    #next step for category_link in category links call proudcts_collecter(get_pagination(category_link))
    for proudct_link in the_links:
        print('API scaner saving : ' + str(proudct_link))
        newproudct_link = BakeryLinks(url=proudct_link)
        session.add(newproudct_link)
        session.commit()
    print('successfully Saved All Bakeries link..')
    print('Next Step Starting soon Get Proudct data ..')
    bakeries_list = session.query(BakeryLinks).all()
    for proudct_url in bakeries_list:
        if proudct_url not in the_bakery_list:
            the_bakery_list.append(proudct_url.url)
        else:
            continue
    print('scaner API ready To get proudcts Data...')
    print('This will take time max 5 minutes Please wait Until we fetch all project data...')
    all_proudcts = get_proudct_data(the_bakery_list)
    print('We successfully got all proudcts and saved internal..')
    print('API scaner now will save the proudcts data in the Database..')
    print('Please Wait until we Fetch all proudcts data and save it in the Database..')
    for proudct_object in all_proudcts:
        ju_proudct_image = proudct_object['image']
        ju_proudct_name = proudct_object['name']
        ju_proudct_price = proudct_object['price']
        newproudct_data = Bakery(name=ju_proudct_image,price=ju_proudct_name,image=ju_proudct_price)
        session.add(newproudct_data)
        session.commit()

        #for single_data in proudct_object:
    return str('successfully Got All The Bakery Data Please Visit Link localhost:5000/bakery_data to get the all data..')



# this is the main file

"""
for x in thisdict:
    for i in x:
        if x not in mylinks:
            mylinks.append(x[i])
    mylinks.append('new proudct')
"""

if __name__ == '__main__':
    app.secret_key = 'AS&S^1234Aoshsheo152h23h5j7ks9-1---3*-s,#k>s'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
