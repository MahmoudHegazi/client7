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
def lyricsJSON():
    bakeries = session.query(BakeryLinks).all()
    return jsonify(bakeries=[r.serialize for r in bakeries])

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
            time.sleep(300)

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
                time.sleep(300)
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


@app.route('/target')
def targeter():
    # we call proudcts_collecter to get proudct links which accept list of pagination and give it category url
    print('Welcome To API scaner We going to Start soon...')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('3 Go..')

    # bakery category
    mylinks = proudcts_collecter(get_pagination('https://eshop.tesco.com.my/groceries/en-GB/shop/fresh-food/bakery/all'))
    #next step for category_link in category links call proudcts_collecter(get_pagination(category_link))
    for proudct_link in mylinks:
        print('API scaner saving : ' + str(proudct_link))
        newproudct_link = BakeryLinks(url=proudct_link)
        session.add(newproudct_link)
        session.commit()
    return 'Good Job This APP Made By Python King.'





if __name__ == '__main__':
    app.secret_key = 'AS&S^1234Aoshsheo152h23h5j7ks9-1---3*-s,#k>s'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
