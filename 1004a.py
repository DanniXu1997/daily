<<<<<<< HEAD
from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello Napier"

@app.route('/force404')
def force404():
  abort(404)

@app.errorhandler(404)
def page_not_found(error):
  return"Couldn't find the page you requested.", 404
=======
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name=None):
  user = {'name':name}
  return render_template('hello.html', user=user)
>>>>>>> e2317951c8f17d81491d45cc5d27f1af080068a3

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

<<<<<<< HEAD
=======

>>>>>>> e2317951c8f17d81491d45cc5d27f1af080068a3
