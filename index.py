from flask import Flask, render_template, request, session
from flask.ext.session import Session
from random import randint

app = Flask(__name__)
app.secret_key = 'superSecretKey'

@app.route('/', methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		num = int(request.form["numero"])
		rand = getRandom()
		if(rand == None):
			generarRandom()

		if(num > rand):
			return render_template('index.html', msg="El numero introducido es mas grande")
		elif(num < rand):
			return render_template('index.html', msg="El numero introducido es mas pequeno")
		else:
			resetRandom()
			return render_template('index.html', msg="Has ganado!!")
	else:
		return render_template('index.html')

def generarRandom():
	session['rand'] = randint(1, 100)

def getRandom():
	return session.get("rand", None)

def removeRandom():
	session['rand'] = None

def resetRandom():
	removeRandom()
	generarRandom()