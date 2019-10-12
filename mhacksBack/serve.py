from parse import parse
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/<text>')
def example(text):
    exam = jsonify(parse(text))
    print(exam)
    return exam


'''
www\.cbc\.ca\/news\/(.*)
www\.foxnews\.com\/\w+\/(.*)

'''


if __name__ == '__main__':
    app.run(debug=True)
