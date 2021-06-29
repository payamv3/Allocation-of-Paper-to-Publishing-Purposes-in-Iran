install beautifulsoup4
import streamlit as st
import numpy as np
import pandas as pd
import os
import requests
import csv
import sys
import time
from bs4 import BeautifulSoup

paper = pd.DataFrame()

for page_no in range(1, 253):
    
    data = {
        'page': page_no,
        'size': 50
    }
    page = requests.get('https://paperds.ir/book-publisher-report?', params=data)
    soup = BeautifulSoup(page.text, 'html.parser')   
    table = soup.find_all('table')
    df = pd.read_html(str(table))[0]
    paper = paper.append(df)
    
st.write("""
# Allocation of Paper to Publishers in Iran
A Transparency Project
*Payam Saeedi!*""")
