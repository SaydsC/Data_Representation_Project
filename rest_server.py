from flask import Flask, url_for, request, redirect, abort

app=Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

#get all
@app.route('/books')
def getAll():
    return "served by GET all()"

#find by ID
@app.route('/books/<int:id>')
def findByID(id):
    return "served by find by ID with id"+ str(id)

#Create
@app.route('/books')
def create():
    return "served by Create "

#Update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    return "served by update with id"+ str(id)

#Delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return "served by delete with id"+ str(id)

if __name__=="__main__":
    app.run(debug=True)