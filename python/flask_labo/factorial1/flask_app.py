from flask import Flask, render_template
from functions import factorial

app = Flask(__name__)

@app.route('/')
def index():
    f5 = factorial(5)
    f6 = factorial(6)
    #lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render_template('index.html', f5=f5, f6=f6, factorial=factorial)

if __name__ == '__main__':
    app.run()