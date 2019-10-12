from parse import retMag
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getMag')
def example():
    test = request.json

    return exam




'''
www\.cbc\.ca\/news\/(.*)
www\.foxnews\.com\/\w+\/(.*)
cnn\.com/\S+
www\.usatoday\.com\/story\/\w+\/\S+
www\.nbcnews.com\/\S+
www\.forbes\.com\/sites\/\w+\/(\d+\/){3}\S+

'''


if __name__ == '__main__':
    app.run(debug=True)
