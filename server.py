from flask import Flask, Markup, render_template, session, request,redirect
import random
import datetime

app = Flask(__name__)

app.secret_key = "ThisAppIsGoingToBeTheOne"

def initializeGold():
	try:
		session['gold']
	except KeyError:
		session['gold'] = 0
		session['activity'] = [Markup('<p class="green">Woke up</p>')]


@app.route('/')
def home():
	initializeGold()
	return render_template('index.html', gold=session['gold'], activity=session['activity'])

@app.route('/process_money', methods=['POST'])
def process():
	dateNow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	if (request.form['action'] == "farm"):
		goldEarned = random.randint(10,20)
		session['gold'] += goldEarned
		session['activity'].insert(0,Markup('<p class="green">Farmed ' + str(goldEarned) + ' gold, for a total of: ' + str(session['gold']) + ' gold.(' + dateNow +')</p>'))
	elif (request.form['action'] == "cave"):
		goldEarned = random.randint(5,10)
		session['gold'] += goldEarned
		session['activity'].insert(0,Markup('<p class="green">Found ' + str(goldEarned) + ' gold in a cave, for a total of: ' + str(session['gold']) + ' gold.(' + dateNow +')</p>'))
	elif (request.form['action'] == "house"):
		goldEarned = random.randint(2,5)
		session['gold'] += goldEarned
		session['activity'].insert(0,Markup('<p class="green">Found ' + str(goldEarned) + ' gold under the couch cushions, for a total of: ' + str(session['gold']) + ' gold.(' + dateNow +')</p>'))
	elif (request.form['action'] == "casino"):
		goldEarned = random.randint(-50,50)
		if goldEarned < 0:
			session['gold'] += goldEarned
			session['activity'].insert(0,Markup('<p class="red">LOST ' + str(goldEarned) + ' gold at the Casino, for a total of: ' + str(session['gold']) + ' gold.(' + dateNow +')</p>'))
		elif goldEarned > 0:
			session['gold'] += goldEarned
			session['activity'].insert(0,Markup('<p class="green">WON ' + str(goldEarned) + ' gold at the Casino, for a total of: ' + str(session['gold']) + ' gold.(' + dateNow +')</p>'))
		else:
			session['activity'].insert(0,Markup('<p class="yellow">No gold was won at the Casino, you have a total of: ' + str(session['gold']) + ' gold.(' + dateNow +')</p>'))

	return redirect('/')


app.run(debug=True)