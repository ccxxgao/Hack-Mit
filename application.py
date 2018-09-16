from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
import requests
from helper import get_news

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#from helpers import apology, login_required
req = requests.get("https://www.quandl.com/api/v3/datatables/ZACKS/AR.json?api_key=sEpgZsqAFy4-iptWfY2V")
print(req.status_code)
#print(req.json())

data = req.json()['datatable']['data']
column1 = [row[1] for row in data]

print(column1)
#req[]

@app.route("/", methods=["GET", "POST"])
def intro1():
 if request.method=="POST":
  return render_template("intro2.html")
 else:
  return render_template("intro1.html")

@app.route("/next", methods=["GET", "POST"])
def intro2():
 if request.method=="POST":
  return render_template("intro2.html")
 else:
  return render_template("options.html")

@app.route("/options", methods=["GET", "POST"])
def options():
 if request.method=="POST":
  return render_template("stocks.html")
 else:
  return render_template("options.html", stocks=column1)

@app.route("/stocks", methods=["GET", "POST"])
def display_chosen():
 if request.method=="POST":
  return null
 else:
  return render_template("stocks.html", stocks=chosen_ones)
'''
r = requests.get(url='https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
print(r.json())
'''
'''
import json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
[u'foo', {u'bar': [u'baz', None, 1.0, 2]}]
>>> json.loads('"\\"foo\\bar"')
u'"foo\x08ar'
>>> from StringIO import StringIO
>>> io = StringIO('["streaming API"]')
>>> json.load(io)
'''
#print(response.status_code)
#print(response)

#with open("response", "r") as read_file:
 #   data = json.load(response)
#data = json.loads(response)

#for (k, v) in data.items():
 #   print("Key: " + k)
  #  print("Value: " + str(v))