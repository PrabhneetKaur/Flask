from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')#this is the first end point#
def home():
   return render_template('index.html')

@app.route('/extend')#This is the second end point#
def ext():
   return render_template('extend.html')


if __name__ == '__main__':
   app.run() 