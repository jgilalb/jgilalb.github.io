#!/bin/ipython3

import fab,sys
from flask import Flask, render_template, abort
from config import FILE
    
app = Flask(__name__)
@app.route('/')

def main():
    tanteo = open(FILE,'r')
    datos = fab.tanper(tanteo)
    tanteo.close()
    return render_template('index.html', datos=datos)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug = True)
