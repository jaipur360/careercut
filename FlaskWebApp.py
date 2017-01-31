from flask import Flask, render_template, flash, request, make_response, jsonify, session
# cd ~ && cd development\seleniumapi && clear && python3 FlaskWebApp.py
import requests
import simplejson as json
import logging
import psycopg2
logging.basicConfig(filename='FlaskWebApp.log',level=logging.INFO)

app = Flask(__name__,static_folder='static', static_url_path='')
#from config import CONFIG
conn = None
metaData = None


@app.route('/')
def index():
	try:
		return render_template('index.html')
	except Exception as e:
		logging.error(str(e))
 


@app.route('/local_Authenticate',methods=['POST'])
def local_Authenticate():
	try:
		emailid = request.form['emailid']
		password = request.form['password']

		returnObj = {}
		returnObj['success'] = False

		if(emailid=='sayan.iit@gmail.com' and password=='sayan'):
			returnObj['success'] = True
			returnObj['fname'] = 'Sayan'
			returnObj['emailid'] = 'sayan.iit@gmail.com'
			session['info'] = returnObj
			#print(session['info'])
			return render_template('dashboard.html', session=session)

		return render_template('index.html', session=session)
	except Exception as e:
		logging.error(str(e))

@app.route('/dashboard',methods=['GET'])
def dashboard():
	try:
		if('info' in session):
			return render_template('dashboard.html',session=session)
		else:
			return render_template('index.html',session=session)
	except Exception as e:
		logging.error(str(e))

@app.route('/profilebuilder',methods=['GET'])
def profile_builder():
	try:
		if('info' in session):
			logging.info('profile_builder.html')
			return render_template('profilebuilder.html',session=session)
		else:
			return render_template('index.html',session=session)
	except Exception as e:
		logging.error(str(e))

@app.route('/goalpursuit',methods=['GET'])
def goal_pursuit():
	try:
		if('info' in session):
			logging.info('goal_pursuit.html')
			return render_template('goalpursuit.html',session=session)
		else:
			return render_template('index.html',session=session)
	except Exception as e:
		logging.error(str(e))

@app.route('/experthelper',methods=['GET'])
def expert_helper():
	try:
		if('info' in session):
			logging.info('experthelper.html')
			return render_template('experthelper.html',session=session)
		else:
			return render_template('index.html',session=session)
	except Exception as e:
		logging.error(str(e))

@app.route('/extra',methods=['GET'])
def extra():
	try:
		if('info' in session):
			logging.info('extra.html')
			return render_template('extra.html',session=session)
		else:
			return render_template('index.html',session=session)
	except Exception as e:
		logging.error(str(e))

@app.route('/submitprofile',methods=['GET','POST'])
def submitprofile():
	try:
		logging.info('submitprofile.html')
		error = None
		conn = psycopg2.connect(database='postgres', user='postgres', password='Postgres@32', host="127.0.0.1", port="5432")
		conn.autocommit = True
		cur = conn.cursor()
		if request.method == "GET":
			return render_template('submitprofile.html')
		if request.method == "POST":
			if request.form['firstname'] is not None and request.form['lastname'] is not None:

				firstname = request.form['firstname']
				lastname = request.form['lastname']
				address = request.form['address']
				city = request.form['city']
				state = request.form['state']
				zipcode = request.form['zipcode']

				designation = request.form['designation']
				phone = request.form['phone']
				email = request.form['email']
				tenthoverall = request.form['tenthoverall']
				tenthmath = request.form['tenthmath']
				tenthscience = request.form['tenthscience']

				twelthoverall = request.form['twelthoverall']
				twelthphysics = request.form['twelthphysics']
				twelthchemistry = request.form['twelthchemistry']
				twelthmath = request.form['twelthmath']

				graduation = request.form['graduation']
				graduationoverall = request.form['graduationoverall']

				interest1 = request.form['interest1']
				interest2 = request.form['interest2']
				interest3 = request.form['interest3']

				cur.execute("INSERT INTO student_profile\
				(firstname ,lastname ,address ,city ,state ,zipcode ,designation ,phone ,email,tenthoverall ,tenthmath ,tenthscience ,twelthoverall ,twelthphysics ,twelthchemistry ,twelthmath ,graduation ,graduationoverall ,interest1 ,interest2,interest3) \
				VALUES (%s, %s,%s, %s, %s, %s,%s, %s,%s, %s, %s, %s,%s, %s,%s, %s, %s, %s,%s, %s,%s)", \
				(firstname ,lastname ,address ,city ,state ,zipcode ,designation ,phone ,email,tenthoverall ,tenthmath ,tenthscience ,twelthoverall ,twelthphysics ,twelthchemistry ,twelthmath ,graduation ,graduationoverall ,interest1 ,interest2,interest3))

				conn.commit()
				cur.close()
				
		return render_template('submitprofilesucess.html')
	except Exception as e:
		logging.error(str(e))

@app.route('/institutional',methods=['GET'])
def corporate():
	try:
		logging.info('institutional.html')
		return render_template('institutional.html',session=session)
	except Exception as e:
		logging.error(str(e))
# @app.route('/searchtopic',methods=['GET'])
# def searchtopic():
# 	if request.method == 'GET':
# 		param_result = request.args.get('search')
# 		#payload = {'searchTerm': result}
# 		mystr = 'http://localhost:5000/gd_worker_task_insert?searchTerm='
# 		mystr = mystr + param_result
# 		r = requests.get(mystr)
# 		return render_template('searchresults.html',results = r.json())

# @app.route('/item',methods=['GET'])
# def item():
# 	if request.method == 'GET':
# 		param_sno = request.args.get('sno')
# 		#payload = {'searchTerm': result}
# 		mystr = 'http://localhost:5000/gd_worker_task_single?sno='
# 		mystr = mystr + param_sno
# 		r = requests.get(mystr)
# 		return render_template('item.html',results = r.json())

if __name__ == '__main__':
	app.static_folder = 'static'
	app.secret_key = 'Secret!'
	###### Very Imp (DEBUG)
	app.run(debug=True, port=3000,host='0.0.0.0')
	###### Production
	#app.run(debug=False, port=80,host='0.0.0.0')