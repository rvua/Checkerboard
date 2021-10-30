from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', num = 4, num2 = 4, color1="red", color2="black")

@app.route('/test/<int:num>')
def index_2(num):
    return render_template('index.html', num=num, num2 = num, color1="red", color2="black")

@app.route('/<int:num>/<int:num2>')
def index_3(num, num2):
    return render_template('index.html', num = num, num2 = num2, color1="red", color2="black")

@app.route('/<int:num>/<int:num2>/<string:color1>/<string:color2>')
def index_4(num, num2, color1, color2):
    return render_template('index.html', num = num, num2 = num2, color1=color1, color2=color2)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 

if __name__ == "__main__":
    app.run(debug=True) 