from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'
#Reminder Replace username, password, locla host and db_name with my SQL credentials

db= SQLAlchemy(app)

#Create a sample model for the database
class User(db.model):
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
#Create tables based on the models
db.create_all()

#Create API endpoint to get all users
@app.route('/users',methods=['GET'])
def get_users():
    users=User.query.all()
    user_list=[]
    for user in users:
        user_list.append({'id':user.id, 'username':user.username})
    return jsonify({'users':user_list})

if __name__=='__main__':
    app.run(debug=True)

 #This connects Flask to MySQL database
 # To run this save the code in a python file and execute using: python flask.py   