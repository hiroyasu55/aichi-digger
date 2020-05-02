from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators, ValidationError
import logging
import re


logger = logging.getLogger('aichi-digger').getChild(__name__)


class ContactForm(FlaskForm):
    name = StringField(
        'name',
        validators=[
            validators.DataRequired(message='お名前を入力してください。')
        ],
    )
    email = StringField(
        'email',
    )
    content = TextAreaField(
        'content',
        validators=[
            validators.DataRequired(message='内容をご入力ください。')
        ],
    )

    def validate_email(self, email):
        if len(email.data) > 0 and not re.match(r'^[^\s]+@[^\s]+$', email.data):
            raise ValidationError('メールアドレスを正しく入力してください。')
