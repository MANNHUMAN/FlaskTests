'''
RUN IN VIRTUAL ENVIRONMENT!
cd myproject
py -3 -m venv .venv
.venv\Scripts\activate
Done!
Dad was talking about "PRIMARY AND FOREIGN KEYS"
https://www.youtube.com/watch?v=mqhxxeeTbu0&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=1
^Tutorial used for most of this shit, reference it when needed!^
'''
from flask import Flask, render_template, url_for, request, redirect, session, flash
from pathlib import Path
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from admin.second import second

app=Flask(__name__)
app.register_blueprint(second,url_prefix="/admin")
app.secret_key="ToTheSkies"#required for idfk
app.permanent_session_lifetime=timedelta(hours=1)#sets session.permanent time
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class users(db.Model):
	_id=db.Column("id",db.Integer,primary_key=True)
	name=db.Column("name",db.String(100))
	email=db.Column("email",db.String(100))

	def __init__(self,name,email):
		self.name=name
		self.email=email

#home page with gifs and shit on it
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/view")
def view():
	return render_template("view.html",values=users.query.all())

#login page with just 1 box
@app.route("/login",methods=["POST","GET"])
def login():
	'''
	On login.html, there is a POST request that asks for user input, this is a request.
	request.form is what they typed, and in the html file it is a variable named "nm".
	user is set to request.form["nm"], and then session["user"] is set to that.
	After that it just redirects to /user which takes session["user"] and uses that.
	The else statement just redirects to user if they've already got a session.
	'''
	if request.method=="POST":
		session.permanent=True
		user=request.form["nm"]
		session["user"]=user

		#To delete a db item, it would be users.query.filter_by(name/email/w/e=user).delete()
		#and obv db.session.commit()
		found_user=users.query.filter_by(name=user).first()
		if found_user:
			session["email"]=found_user.email
		else:
			usr=users(user,"")
			db.session.add(usr)
			db.session.commit()#Every time  you change the database, it must be committed.

		flash('Login Successful!')
		return redirect(url_for("user",))
	else:
		if "user" in session:
			flash('Already logged in!')
			return redirect(url_for("user"))
		return render_template("login.html")

@app.route("/user",methods=["POST","GET"])
def user():
	email=None
	if "user" in session:
		user=session["user"]
		if request.method=="POST":
			email=request.form["email"]
			session["email"]=email
			found_user=users.query.filter_by(name=user).first()
			found_user.email=email
			db.session.commit()
			flash('Email is saved!')
		else:
			if "email" in session:
				email=session["email"]
		return render_template("user.html",email=email)
	else:
		flash('You are not logged in!')
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	if "user" in session:
		user=session["user"]
		flash(f"You have been logged out, {user}.","info")
		#info is a category, shows an icon next to it.
	session.pop("user",None)
	session.pop("email",None)
	return redirect(url_for("login"))
#FUCK I NEED TO LEARN HTML DON'T I GOD FUCKING DAMN IT I AM KILLING MYSELF POSTHASTE
if __name__=='__main__':
	with app.app_context():
		db.create_all()
	app.run(debug=True)