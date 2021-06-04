# -*- coding: utf-8 -*-
"""
Created on Mon May 31 21:46:32 2021

@author: 1821086
"""

import requests

url = 'http://localhost/卒研/connect_DB1.php'
res = requests.get(url)

time_elapsed = res.elapsed.total_seconds()
print('time_elapsed_DB1:', time_elapsed)

url = 'http://localhost/卒研/connect_DB2.php'
res = requests.get(url)

time_elapsed = res.elapsed.total_seconds()
print('time_elapsed_DB2:', time_elapsed)

url = 'http://localhost/卒研/connect_DB3.php'
res = requests.get(url)

time_elapsed = res.elapsed.total_seconds()
print('time_elapsed_DB3:', time_elapsed)


