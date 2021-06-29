import streamlit as st
import numpy as np
import pandas as pd
import os
import requests
import csv
import xlrd
import sys
import time
from bs4 import BeautifulSoup

paper = pd.read_excel('PaperSystem.xlsx')
    
st.write("""
# Allocation of Paper to Publishers in Iran
A Transparency Project
*Payam Saeedi!*""")
