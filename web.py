#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dchanna
#
# Created:     09/08/2020
# Copyright:   (c) dchanna 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, Dinesh'

app.run(host='localhost', port=80)