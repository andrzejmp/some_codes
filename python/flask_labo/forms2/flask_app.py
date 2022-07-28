from flask import Flask, render_template, session,  redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField,
                    BooleanField, DateTimeField, 
                    RadioField, SelectField, TextAreaField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    student = StringField("What is your name?", validators=[DataRequired()])
    finished = BooleanField("Have you finished studies?")
    year = RadioField('Please choose your year of study:',
                      choices=[('year_one', '1'),('year_two', '2'), ('year_three', '3')])
    field = SelectField(u'Choose your field of studies:', 
                    choices=[('cs', 'computer science'), ('math', 'mathematics'), ('chemistry', 'chemistry') ])

    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])

def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['student'] = form.student.data
        session['finished'] = form.finished.data
        session['year'] = form.year.data
        session['field'] = form.field.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('summary'))

    return render_template('index.html', form=form)


@app.route('/summary')
def summary():
    return render_template('summary.html')

if __name__ == '__main__':
    app.run(debug=True)


