from parse import checkurl, nlp
from flask import Flask, jsonify, request, render_template, send_from_directory
from sqlite3 import dbapi2 as sqlite
from flask_sqlalchemy import SQLAlchemy
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///feelter.db'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<retFile>')
def filer(retFile):
    print(retFile)
    return send_from_directory('./static/',retFile)


@app.route('/getMag')
def example():
    print("HELLO")
    test = request.get_json(force=True)
    print(test)
    a = "0"
    response = []
    for i in test:
        print("HELLO")
        print(i.get("id"))
        a = retMag(i)
        response.append({'id':i.get("id"), 'sentiment':a[0], 'magnitude':a[1]})
    print(test)
    f = open('test.json', 'w')
    f.write(json.dumps(response))

    return jsonify(response)


class Stuff(db.Model):
    id = db.Column(db.String(3), primary_key=True)
    content = db.Column(db.String(255))
    cType = db.Column(db.String(255))
    senti = db.Column(db.String(8))
    magn = db.Column(db.String(8))

def retMag(val):
    check = Stuff.query.filter_by(id=val.get("id")).first()
    if check == None and val.get("type") == "url":
        values = checkurl(val.get("content"))
        print(values)
        print(type(values[0]))
        print(type(values[1]))
        thing = Stuff(id=val.get("id"), content=val.get("content"), cType=val.get("type"), senti="{:2.2f}".format(float(values[0])), magn="{:2.2f}".format(float(values[1])))
        db.session.add(thing)
        db.session.commit()
        return values
    if check == None:
        values = nlp(val.get("content"))
        print(values)
        print(type(values[0]))
        print(type(values[1]))
        thing = Stuff(id=val.get("id"), content=val.get("content"), cType=val.get("type"), senti="{:2.2f}".format(float(values[0])), magn="{:2.2f}".format(float(values[1])))
        db.session.add(thing)
        db.session.commit()
        return values

    return (check.senti, check.magn)

    
if __name__ == '__main__':
    app.run(debug=True, port=8000)
