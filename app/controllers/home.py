from flask import Blueprint, render_template, request, current_app
import pprint  # noqa: F401
import app.lib.log as log
import app.lib.mail as mail
from app.models.forms import ContactForm

app_home = Blueprint('home', __name__)
logger = log.getLogger(__name__)


def send_mail(msg):
    logger.info('Send message name=%s', msg['name'])

    subject = '[Contact] from {}'.format(msg['name'])
    body = '[Contact]\n\n'
    body += 'name: {}\n'.format(msg['name'])
    body += 'email: {}\n'.format(msg['email'])
    body += 'content:\n{}\n'.format(msg['content'])
    recipient = current_app.config.get('CONTACT_SENDER')

    mail.send(recipients=[recipient], subject=subject, body=body)


@app_home.route("/")
def index():
    param = {
        'title': 'AICHI-DIGGER',
    }
    return render_template('home/index.html', **param)


@app_home.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    param = {
        'title': 'AICHI-DIGGER | お問い合わせ',
        'form': form,
    }

    if request.method == 'POST':
        if form.validate_on_submit():
            msg = {
                'name': form.name.data,
                'email': form.email.data,
                'content': form.content.data,
            }
            logger.info(msg)
            send_mail(msg)
            return render_template('home/contact_success.html', **param)

    return render_template('home/contact.html', **param)
