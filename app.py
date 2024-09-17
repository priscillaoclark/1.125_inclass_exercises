from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello World!</h1>'

# add user
@app.route('/addUser', methods=['POST', 'GET'])
def addUser():
    return render_template('form.html')

# return user
@app.route('/getUser', methods=['POST', 'GET'])
def getUser():
    

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)