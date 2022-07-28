from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    number = StringField("Enter the number: ")
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])

def index():
    number = False
    form = InfoForm()
    if form.validate_on_submit():
        number = form.number.data
        form.number.data = ''

    return render_template('index.html', form=form, number=number)

if __name__ == '__main__':
    app.run(debug=True)


