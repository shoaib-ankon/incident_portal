# importing libraries 
from flask import Flask,render_template, request, redirect, url_for 
from flask_mysqldb import MySQL


app = Flask(__name__) 

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'incidentlog'

mysql = MySQL(app)

 
@app.route("/") 
def read():

	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM incident")
	data = cur.fetchall()
	cur.close()

	return render_template('index.html', incident=data) 




@app.route('/insert', methods=["GET", "POST"])
def insert():

	if request.method == "POST":
		issue = request.form['issue']
		impact = request.form['impact']
		status = request.form['status']
		startt = request.form['startt']
		endt = request.form['endt']
		reason = request.form['reason']
		solution = request.form['solution']
		ticket = request.form['ticket']
		remarks = request.form['remarks']

		cur = mysql.connection.cursor()
		cur.execute(" INSERT INTO incident (issue,impact,status,startt,endt,reason,solution,ticket,remarks) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)", (issue,impact,status,startt,endt,reason,solution,ticket,remarks))
		mysql.connection.commit()
	return redirect(url_for('read'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):    
    cur = mysql.connection.cursor()
    cur.execute(" DELETE FROM incident WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('read'))


@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
    	id_data = request.form['id']	
    	issue = request.form['issue']
    	impact = request.form['impact']
    	status = request.form['status']
    	startt = request.form['startt']
    	endt = request.form['endt']
    	reason = request.form['reason']
    	solution = request.form['solution']
    	ticket = request.form['ticket']
    	remarks = request.form['remarks']
    	cur = mysql.connection.cursor()
    	cur.execute("""
               UPDATE incident 
               SET issue=%s, impact=%s, status=%s, startt=%s, endt=%s, reason=%s, solution=%s, ticket=%s, remarks=%s 
               WHERE id=%s
            """,(issue,impact,status,startt,endt,reason,solution,ticket,remarks,id_data))

    	mysql.connection.commit()
    return redirect(url_for('read'))




if __name__ == '__main__': 
	app.run(debug = True) 
