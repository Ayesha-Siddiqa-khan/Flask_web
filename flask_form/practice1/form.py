from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    DateField,
    PasswordField,
    
)

from wtforms.validators import(
    DataRequired, 
    Length,
    Email,
    Optional,
    EqualTo,
)





class Signup_form(FlaskForm):
   username = StringField(
       "Username",
       validators=[DataRequired(),Length(2,30)]
   )
   email = StringField(
       "Email",
       validators=[DataRequired(),Email()]
   )
   gender = SelectField(
       "Gender",
       choices=["Male","Female","Other"],
       validators=[Optional()]
   )
   
   dob = DateField(
       "Date of birth",
       validators=[Optional()]
   )
   password  = PasswordField(
       "Password",
       validators=[DataRequired(),Length(4,25)]
   )
   confrim_password = PasswordField(
       "Confirm_password",
       validators=[DataRequired(),Length(4,25),EqualTo ("password")]
   )
   























































































































































class login_form(FlaskForm):
    pass