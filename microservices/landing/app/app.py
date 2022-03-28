from flask import Flask, render_template, request, flash, redirect, url_for
from flask_restful import Api

import requests
import os
  
app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def modulus(n1, n2):
    URL = 'http://modservice:'
    port = 5055
    mod_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(mod_url)
    return response.json()['result']

def exponent(n1, n2):
    URL = 'http://exponentservice:'
    port = 5056
    exp_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(exp_url)
    return response.json()['result']

def greater_than(n1, n2):
    URL = 'http://greater-than-service:'
    port = 5057
    div_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(div_url)
    return response.json()['result']


def add(n1, n2):
    URL = 'http://add-service:'
    port = 5051
    add_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(add_url)
    return response.json()['result']

def minus(n1, n2):
    URL = 'http://minus-service:'
    port = 5052
    sub_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(sub_url)
    return response.json()['result']

def multiply(n1, n2):
    URL = 'http://multiply-service:'
    port = 5053
    mul_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(mul_url)
    return response.json()['result']

def divide(n1, n2):
    URL = 'http://division-service:'
    port = 5054
    div_url = URL + str(port) + '/' + str(n1) + '/' + str(n2)
    response = requests.get(div_url)
    return response.json()['result']



@app.route('/', methods=['POST', 'GET'])
def index():
    try: 
        number_1 = request.form.get("first")
        number_2 = request.form.get('second')
        number_2=int(number_2)
        number_1=int(number_1)
        operation = request.form.get('operation')
    except TypeError as typerr:
        number_2=0
        number_1=0
        operation='add'
    
    result = 0
    if operation == 'add':
        result = add(number_1, number_2)
    elif operation == 'minus':
        result =  minus(number_1, number_2)
    elif operation == 'multiply':
        result = multiply(number_1, number_2)
    elif operation == 'divide':
        result = divide(number_1, number_2)
    elif operation == 'modulus':
        result = modulus(number_1, number_2)
    elif operation=='exponent':
        result = exponent(number_1, number_2)
    elif operation=='greater_than':
        result = greater_than(number_1, number_2)

    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
