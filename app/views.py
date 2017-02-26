from flask import render_template, flash, redirect, session, url_for, request, g, current_app
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from app import app, db, lm
from .forms import LoginForm
from .models import User
from .oauth import OAuthSignIn

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ed'}  # fake user
    posts = [
        {
            'author': {'nickname':'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname':'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)

@app.before_request
def before_request():
    g.user = current_user

@app.route('/login', methods=['GET', 'POST'])
#@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # if form.validate_on_submit():
    #     session['remember_me'] = form.remember_me.data
    #     return True
        #return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OAUTH_CREDENTIALS'])

@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()

@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, nickname=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
