#RUN IN VIRTUAL ENVIRONMENT!
#cd myproject
#py -3 -m venv .venv
#.venv\Scripts\activate
#Done!
#Dad was talking about "PRIMARY AND FOREIGN KEYS"
from flask import Flask, render_template, url_for
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pathlib import Path
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)
if Path('./test.db').exists()==False:
	db.create_all()
class Todo(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	content=db.Column(db.String(200),nullable=False)
	date_created=db.Column(db.DatetTime,default=datetime.utcnow)
	def __repr__(self):
		return '<task %r' % self.id
@app.route("/")
def home():
	return render_template('index.html')
#FUCK I NEED TO LEARN HTML DON'T I GOD FUCKING DAMN IT I AM KILLING MYSELF POSTHASTE
if __name__=='__main__':
	app.run(debug=True)