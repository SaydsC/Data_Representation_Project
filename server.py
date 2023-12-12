from flask import Flask, url_for, redirect

app = Flask(__name__, static_url_path='', static_folder='staticpages')
@app.route('/')
def index():
    return "<a href="+url_for('getuser')+">getusers</a>"

@app.route('/user/<username>', methods=['GET'])
def getuser():
    return "hi there"

@app.route('/user', methods=['POST'])
def postuser():
    print ("in post")
    return "in post"

@app.route('/invalid', methods=['GET'])
def invalid():
    return redirect(url_for('index'))

if __name__=="__main__":
    app.run(debug=True)

