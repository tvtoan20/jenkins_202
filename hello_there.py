#!/usr/bin/env python3

import requests

x = requests.get('https://www.google.com')

if x.status_code == 200:
  print('Okay!')
else:
  print('NOT Okay!')
