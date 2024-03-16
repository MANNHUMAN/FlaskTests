from flask import Flask,render_template,url_for,request,redirect,session,flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import threading

app=Flask(__name__)
app.secret_key="proj"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)



#current_time = datetime.now.strftime("%H:%M:%S")
class data(db.Model):
    _id=db.Column("id",db.Integer,primary_key=True)
    message=db.Column("message",db.String(300))
    log=db.Column("log",db.String(50))

    def __init__(self,message,log):
        self.message=message
        self.log=log


@app.route("/")
def home():
    return render_template('site.html')

@app.route("/numbers",methods=['POST','GET'])
def numbers():

    return render_template('numbers.html')

@app.route("/message", methods=['POST','GET'])
def message():
    if request.method=="POST":
        if 'message' in request.values:
            session["message"]=request.form["message"]
            db.session.add(data(session['message'],''))
            db.session.commit()
            point=data.query.filter_by(message=session["message"]).first()
            point.log=datetime.now().strftime("%D:%H:%M:%S")
        
        elif 'delete' in request.values:
            session['delete']=request.form['delete']
            data.query.filter_by(_id=session['delete']).delete()

    db.session.commit()
    return render_template('message.html',values=data.query.all())



if __name__=='__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        def flaskrun():
            app.run(debug=True)
        