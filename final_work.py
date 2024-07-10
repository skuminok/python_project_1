from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'
db = SQLAlchemy(app)

class Travel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    travel_date = db.Column(db.Date, nullable=False)
    budget = db.Column(db.Integer)
    services = db.Column(db.String(200))

class TravelForm(FlaskForm):
    destination = StringField('Место назначения', validators=[DataRequired()])
    travel_date = DateField('Дата поездки', validators=[DataRequired()])
    budget = IntegerField('Бюджет')
    services = StringField('Желаемые услуги')

@app.route('/')
def index():
    travels = Travel.query.all()
    return render_template('travels.html', travels=travels)

@app.route('/add_travel', methods=['GET', 'POST'])
def add_travel():
    form = TravelForm()
    if form.validate_on_submit():
        new_travel = Travel(destination=form.destination.data, travel_date=form.travel_date.data, 
                            budget=form.budget.data, services=form.services.data)
        db.session.add(new_travel)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_travel.html', form=form)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
