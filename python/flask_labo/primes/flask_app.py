from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from functions import check_primes, get_edge

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    number = StringField("a = ")
    number2 = StringField("b = ")
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])

def index():
    number = False
    number2 = False
    form = InfoForm()
    if form.validate_on_submit():
        number = form.number.data
        form.number.data = ''
        number2 = form.number2.data
        form.number2.data = ''

       
    return render_template('index.html', form=form, number=number, number2=number2, check_primes=check_primes, get_edge=get_edge)

if __name__ == '__main__':
    app.run(debug=True)


