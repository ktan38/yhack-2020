import requests

import json

@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == "GET":
		return "wrong request"
	if request.method == "POST":
		data = request.get_json(force = True)
		email = data['email']
		password = data['password']
		print("inside post req ")
		db = MySQLdb.connect("localhost","root","password", "python_api")
		cursor = db.cursor()
		sql = "SELECT * FROM `users` WHERE email=%s and password=%s and external_type='email'"
		# print(sql)
		# respi = ""
		resp = {'result': False, 'user': None}
		try:
			cursor.execute(sql, (email, password))
			results = cursor.fetchall()

			for row in results:
				print(row[1])
				userr = row[1]
				token = row[4]
				break
			if len(results) == 1:
				resp['result'] = True
				resp['comments'] = "one user found"
				resp['user'] = userr
				resp['token'] = token
			elif len(results) == 0:
				resp['comments'] = "No users"
			else:
				resp['comments'] = "multiple users!!"
		except:
			# respi = "exception"
		   print("Error: unable to fecth data")
		db.close()
		return json.dumps(resp)