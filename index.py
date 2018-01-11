from flask import Flask, render_template, request, session
from random import randint

app = Flask(__name__)
app.secret_key = 'superSecretKey'

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
		num = int(request.form["numero"])
		rand = getRandom()
		if(rand == None):
			generarRandom()
			rand = getRandom()

		if(num > rand):
			return render_template('index.html', msg="<p>El numero introducido es mas grande.</p>")
		elif(num < rand):
			return render_template('index.html', msg="<p>El numero introducido es mas pequeno.</p>")
		else:
			generarRandom()
			return render_template('index.html', msg="<h2>Has ganado!!</h2><p>Se a generado otro numero para que vuelvas a jugar.</p>")
	else:
		return render_template('index.html')

def generarRandom():
	session['rand'] = randint(1, 100)

def getRandom():
	return session.get('rand', None)