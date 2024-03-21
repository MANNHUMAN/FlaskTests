from flask import Flask,render_template,url_for,request,redirect,session,flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import random

import threading
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members=True

client = discord.Client(intents=intents)

app=Flask(__name__)
app.secret_key=
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class data(db.Model):
    _id=db.Column("id",db.Integer,primary_key=True)
    blasted_user=db.Column("blasted_user",db.String(100))
    blasting_user=db.Column("blasting_user",db.String(100))
    message=db.Column("message",db.String(300))
    log=db.Column("log",db.String(50))
    message_id=db.Column("message_id",db.String(100))

    def __init__(self,blasted_user,blasting_user,message,log,message_id):
        self.blasted_user=blasted_user
        self.blasting_user=blasting_user
        self.message=message
        self.log=log
        self.message_id=message_id



'''DISCORD SECTION'''

@client.event
async def on_ready():
    print(f'{client.user} is online.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'MODS':
        with app.app_context():
            for swags in data.query.all():
                await message.channel.send(swags.message)

@client.event
async def on_raw_reaction_add(payload):
    print('React called.')
    if str(payload.emoji)=='🫃':
        channel = client.get_channel(payload.channel_id)
        message_get = await channel.fetch_message(payload.message_id)
        
        blasted_user: str = message_get.author.display_name
        blasting_user: str = payload.member.display_name
        log: str = datetime.now().strftime("%H:%M")
        message_id: str = payload.message_id
        message: str = message_get.content
        
        with app.app_context():
            db.session.add(data(blasted_user, blasting_user, message, log, message_id))
            db.session.commit()
            print('Data committed.')

@client.event
async def on_raw_reaction_remove(payload):
    print('Unreact called.')
    if '🫃' in str(payload.emoji):
        print('Emoji detected.')
        with app.app_context():
            for x in data.query.all():
                print(x.message_id, payload.message_id)
                if int(x.message_id) == int(payload.message_id):
                    print('Message found.')
                    db.session.delete(x)
                    db.session.commit()
                    print('Data deleted.')


'''SITE SECTION'''

@app.route("/")
def home():
    return render_template('site.html')

@app.route("/message", methods=['POST','GET'])
def message():
    '''if request.method=="POST":
        if 'delete' in request.values:
            session['delete']=request.form['delete']
            data.query.filter_by(_id=session['delete']).delete()
            
    db.session.commit()
    '''
    return render_template('message.html',values=data.query.all())



'''INITIALIZATION'''

if __name__=='__main__':
    with app.app_context():
        def discrun():
            'the key'
        discthread = threading.Thread(target=discrun)
        discthread.start()
        db.drop_all()
        db.create_all()
        app.run(debug=False)