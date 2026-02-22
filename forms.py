from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TelField, EmailField
from wtforms.validators import DataRequired, Length, Email


class Expense(FlaskForm):
    company = StringField('Company Name', validators=[DataRequired(message='Please enter company name.'), Length(max=40)])
    submit = SubmitField('Send')
    employee_first = StringField('First Name', validators=[DataRequired(message='Please enter employee\'s first name'), Length(max=20)])
    employee_last = StringField('Last Name', validators=[DataRequired(message='Please enter employee\'s last name'), Length(max=20)])
    job_title = StringField('Job Title', validators=[DataRequired(message='Enter job title'), Length(max=30)])
    department = StringField('Department', validators=[DataRequired(message='Please enter dept.'), Length(max=20)])
    phone_number = TelField('Phone Number', validators=[DataRequired(message='Please Enter phone number.')])
    email = EmailField('E-Mail', validators=[DataRequired(message='Please enter your email.'), Email(message='Please enter valid email')])