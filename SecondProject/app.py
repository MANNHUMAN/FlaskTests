from flask import Flask,render_template,url_for,request,redirect,session,flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

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



@app.route("/", methods=['POST', 'GET'])
def front():
    if request.method=="POST":
        session["message"]=request.form["message"]
        db.session.add(data(session['message'],''))
        db.session.commit()
        point=data.query.filter_by(message=session["message"]).first()
        point.log=datetime.now().strftime("%D:%H:%M")
        db.session.commit()
        flash('Data committed.')

        #session["message"]=request.form["message"]
        #session["log"]=datetime.now.strftime("%D:%H:%M")
        #swag=data(session[message],'')
        #db.session.add(swag)
        #db.session.commit()
        #x=datal.query.filter_by(message=session["message"]).first()
        #x.log=session['log']
        #db.session.commit()
    return render_template('site.html',values=data.query.all())



if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)