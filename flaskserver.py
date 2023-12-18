from flask import Flask, jsonify, url_for, request, redirect, abort

app=Flask(__name__, static_url_path='', static_folder='staticpages')

books=[
    {"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000}, 
    {"id": 2, "Title": "Cook Book", "Author": "SC", "Price": 900}, 
    {"id": 3, "Title": "Other Book", "Author": "LM", "Price": 1100}
]

nextId=4

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
    if len(foundBooks) == 0:
        return jsonify({}), 204
    return jsonify(foundBooks[0])

#Create
# curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\", \"Author\":\"Mr Test\", \"Price\":123}" http://127.0.0.1:5000/books

@app.route('/books', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)

    book = {
        "id":nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"]
    }
    books.append(book)
    nextId += 1
    return jsonify(book)

#Update
# curl -X PUT -d "{\"Title\":\"New Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']
    
    return jsonify(currentBook)

#Delete
# curl -X DELETE http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])

    return jsonify({"done":True})

if __name__=="__main__":
    app.run(debug=True) 