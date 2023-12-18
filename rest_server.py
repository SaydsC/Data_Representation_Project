from flask import Flask, jsonify, url_for, request, redirect, abort

app=Flask(__name__, static_url_path='', static_folder='staticpages')

books=[
    {"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000}, 
    {"id": 2, "Title": "Cook Book", "Author": "SC", "Price": 900}, 
    {"id": 3, "Title": "Other Book", "Author": "LM", "Price": 1100}
]

nextID=4

@app.route('/')
def index():
    return "hello"

#get all
@app.route('/books')
def getAll():
    return jsonify(books)

#find by ID
@app.route('/books/<int:id>')
def findByID(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    if len(foundBooks == 0):
        return jsonify({}), 204
    return jsonify(foundBooks[0])

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