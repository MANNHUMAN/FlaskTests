#RUN IN VIRTUAL ENVIRONMENT!
#cd myproject
#py -3 -m venv .venv
#.venv\Scripts\activate
#Done!
from flask import Flask, render_template, url_for
from markupsafe import escape
app=Flask(__name__)
@app.route("/")
def home():
	return render_template('index.html')
#FUCK I NEED TO LEARN HTML DON'T I GOD FUCKING DAMN IT I AM KILLING MYSELF POSTHASTE
if __name__=='__main__':
	app.run(debug=True)