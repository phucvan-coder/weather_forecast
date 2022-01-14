import os.path
from email.mime.text import MIMEText

import numpy
from flask import *
from flask_wtf import FlaskForm, CSRFProtect
from numpy._distributor_init import basedir
from wtforms import *
from wtforms.validators import DataRequired, EqualTo, Length
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.widgets import TextArea
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf.csrf import CSRFProtect
import numpy as np
import pandas as pd
from sklearn import preprocessing
import requests
import smtplib
from flask_ckeditor import *

# Create a Flask Instance
app = Flask(__name__)
# Add CKEditor
ckeditor = CKEditor(app)

# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# key sec
app.config['SECRET_KEY'] = "keysec"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'myemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'helloworld'
app.config['MAIL_USE_SSL'] = True
app.config['authentication'] = True
# initialize
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# flask log in stuffed

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


# Pass Stuff to Navbar
@app.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

# Create Search Function
@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    posts = Posts.query
    if form.validate_on_submit():
        # Get data from submitted form
        post.searched = form.searched.data
        # Query the Database
        posts = posts.filter(Posts.content.like('%' + post.searched + '%'))
        posts = posts.order_by(Posts.title).all()

        return render_template("search.html", form=form, searched=post.searched, posts=posts)

# Create Search Function
@app.route('/search2', methods=["POST"])
def search2():
    form = SearchForm()
    posts = Posts.query
    if form.validate_on_submit():
        # Get data from submitted form
        post.searched = form.searched.data
        # Query the Database
        posts = posts.filter(Posts.content.like('%' + post.searched + '%'))
        posts = posts.order_by(Posts.title).all()

        return render_template("search_2.html", form=form, searched=post.searched, posts=posts)


# Create A Search Form
class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")


# create model
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow())
    password_hash = db.Column(db.String(200))

    @property
    def password(self):
        raise AttributeError('Password invalid')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # create Strings
    def __repr__(self):
        return '<Name %r>' % self.name


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password_hash = PasswordField('Password', validators=[DataRequired(),
                                                          EqualTo('password_hash2', message='Password must match!!!')])
    password_hash2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Submit")


# create form class
class NameForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Submit")


# index
@app.route('/')
@app.route('/index')
def index():  # put application's code here
    return render_template('index.html')


# about
@app.route('/about')
def about():
    return render_template('about.html')


# services
@app.route('/services')
def services():
    return render_template('services.html')

# services
@app.route('/blog_single')
def blog_sìngle():
    return render_template('blog_single.html')

@app.route('/blog_single_2')
def blog_sìngle_2():
    return render_template('blog_single_2.html')

@app.route('/blog_single_3')
def blog_sìngle_3():
    return render_template('blog_single_3.html')

# news
@app.route('/news')
@app.route('/blog')
def news():
    return render_template('news.html')


# Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')


# base
@app.route('/base')
def baseing():
    return render_template('base.html')


# base
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


# adding user
@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(username=form.username.data, name=form.name.data, email=form.email.data,
                         password_hash=form.password_hash.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.username.data = ''
        form.email.data = ''
        form.password_hash.data = ''
        flash("Added Successfully")
    our_users = Users.query.order_by(Users.date_added)
    return render_template('add_user.html', form=form, name=name, our_users=our_users)


# update user
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    form = UserForm()
    name_to_update = Users.query.get_or_404(id)
    if request.method == "POST":
        name_to_update.name = request.form['name']
        name_to_update.email = request.form['email']
        name_to_update.username = request.form['username']
        try:
            db.session.commit()
            flash("Updated Successfully!")
            return render_template("update.html", form=form, name_to_update=name_to_update)
        except:
            flash("Error!")
            return render_template("update.html", form=form, name_to_update=name_to_update)
    else:
        return render_template("update.html", form=form, name_to_update=name_to_update)


# del user
@app.route('/delete/<int:id>')
def delete(id):
    name = None
    form = UserForm()
    user_to_delete = Users.query.get_or_404(id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("Delete Successfully")
        our_users = Users.query.order_by(Users.date_added)
        return render_template('add_user.html', form=form, name=name, our_users=our_users)
    except:
        flash("Delete Failed!!!")
        return render_template('add_user.html', form=form, name=name, our_users=our_users)


# base
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    # validate
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ' '
        flash("Submitter Successfully!")
    return render_template('name.html', name=name, form=form)


# create vblog model
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    content = db.Column(db.Text)
    author = db.Column(db.String(256))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow())
    slug = db.Column(db.String(256))


# post form
class postForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    # content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    content = CKEditorField('Content', validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Submit")


# adding posted blog page ok ?????
@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
    form = postForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data, author=form.author.data, slug=form.slug.data)
        # clear the form
        form.title.data = ''
        form.content.data = ''
        form.author.data = ''
        form.slug.data = ''

        # add post to database base base base base base base base base base
        db.session.add(post)
        db.session.commit()

        # return some message
        flash("Add blog successfully")

        # redirect to web page page page page page page page page page page
    return render_template("add_post.html", form=form)

# adding posted blog page ok ?????
@app.route('/add-post-2', methods=['GET', 'POST'])
def add_post_2():
    form = postForm()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, content=form.content.data, author=form.author.data, slug=form.slug.data)
        # clear the form
        form.title.data = ''
        form.content.data = ''
        form.author.data = ''
        form.slug.data = ''

        # add post to database base base base base base base base base base
        db.session.add(post)
        db.session.commit()

        # return some message
        flash("Add blog successfully")

        # redirect to web page page page page page page page page page page
    return render_template("add_post_2.html", form=form)

# show the post
@app.route('/posts/')
def posts():
    posts = Posts.query.order_by(Posts.id.desc())
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    pages = posts.paginate(page=page, per_page=5)
    return render_template("posts.html", posts=posts, pages=pages)
    # return render_template("posts.html", posts=posts)

    # posts = Posts.query.order_by(Posts.id.desc())
    # page = request.args.get('page')
    # if page and page.isdigit():
    #     page = int(page)
    # else:
    #     page = 1
    # pages = posts.paginate(page=page, per_page=1)
    # return render_template("posts2.html", posts=posts, pages=pages)


@app.route('/posts/<int:id>')
def post(id):
    post = Posts.query.get_or_404(id)
    return render_template('post.html', post=post)

@app.route('/posts3/<int:id>')
def post3(id):
    post = Posts.query.get_or_404(id)
    return render_template('post2.html', post=post)

# edit post
@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Posts.query.get_or_404(id)
    form = postForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.author = form.author.data
        post.slug = form.slug.data
        post.content = form.content.data
        # Update from db
        db.session.add(post)
        db.session.commit()
        flash("Updated successfully")
        return redirect(url_for('post', id=post.id))
    form.title.data = post.title
    form.author.data = post.author
    form.slug.data = post.slug
    form.content.data = post.content
    return render_template('edit_post.html', form=form)

# edit post
@app.route('/posts3/edit/<int:id>', methods=['GET', 'POST'])
def edit_post3(id):
    post = Posts.query.get_or_404(id)
    form = postForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.author = form.author.data
        post.slug = form.slug.data
        post.content = form.content.data
        # Update from db
        db.session.add(post)
        db.session.commit()
        flash("Updated successfully")
        # return redirect(url_for('post', id=post.id))
        return posts3()
    form.title.data = post.title
    form.author.data = post.author
    form.slug.data = post.slug
    form.content.data = post.content
    return render_template('edit_post_2.html', form=form)


# del post here
@app.route('/posts/delete/<int:id>')
def delete_post(id):
    post_to_delete = Posts.query.get_or_404(id)

    try:
        db.session.delete(post_to_delete)
        db.session.commit()
        # shot the message
        flash("Deleted successfully")
        # show all post after del
        posts = Posts.query.order_by(Posts.date_posted)
        return render_template("posts.html", posts=posts)
    except:
        # catch the except ok
        flash("Error while delete!!!")


@app.route('/posts2/')
def posts2():
    posts = Posts.query.order_by(Posts.id.desc())
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    pages = posts.paginate(page=page, per_page=5)
    return render_template("posts2.html", posts=posts, pages=pages)

@app.route('/posts3/')
def posts3():
    posts = Posts.query.order_by(Posts.id.desc())
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    pages = posts.paginate(page=page, per_page=5)
    return render_template("posts3.html", posts=posts, pages=pages)



# create the log in
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


# login here
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user and user.name == 'admin':
            # check hash
            if user.password_hash == form.password.data:
                login_user(user)
                flash("Login successfully")
                # return redirect(url_for('dashboard'))
                usrname = user.username
                return render_template('dashboard.html', name=usrname)
            else:
                flash("Incorrect password!!!!")
        elif user:
            # check hash
            if user.password_hash == form.password.data:
                login_user(user)
                flash("Login successfully")
                b = user.username
                b2 = user.name
                return render_template('dashboard_2.html', name=b, name2=b2)
            else:
                flash("Incorrect password!!!!")
        else:
            flash("User doesn't exist!!!!")
    return render_template('login.html', form=form)


# dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


# model testing heere
@app.route('/runmodel', methods=['GET', 'POST'])
def runmodel():
    if request.method == 'POST':
        file = request.files['csvfile']
        if not os.path.isdir('static'):
            os.mkdir('static')
        filepath = os.path.join('static', file.filename)
        file.save(filepath)

        df = pd.read_csv(filepath)
        df.drop(['YEAR', 'MONTH', 'DAY', 'HOUR'], axis=1, inplace=True)
        X = df.values
        X = preprocessing.scale(X)
        X = X.tolist()

        # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
        API_KEY = "3yJs0dfq8sweZcE9-HD02-U0BUXdFerPqonhRXH6Q-1H"
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token',
                                       data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ['Temperature at 2 meters (C)',
                                                      'Specific Humidity at 2 meters (g/kg)', 'Surface pressure (kPa)',
                                                      'Wind speed at 10 meters (m/s)',
                                                      'Wind direction at 10 meters (Degrees)  '], "values": X}]}

        response_scoring = requests.post(
            'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5af3653a-64b8-4212-97fd-390e08592b00/predictions?version=2021-12-04',
            json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
        pred = response_scoring.json()
        # return render_template('prediction.html', predictions = pred['predictions'][0]['values'])
        arr = []
        for x in pred['predictions'][0]['values']:
            for y in x:
                arr.append(y)
        print("Raw array: ", pred['predictions'][0]['values'])
        print("Type of array: ", type(pred['predictions'][0]['values']))
        print("Elements: ", end=' ')
        for e in arr:
            print(e, end=' ')
        print()
        return render_template('prediction.html', a=arr)
        # return render_template('prediction.html', predictions)
        # return predictions['predictions'][0]['values']
    return render_template('upload.html')

# model admin
@app.route('/runmodel2', methods=['GET', 'POST'])
def runmodel2():
    if request.method == 'POST':
        file = request.files['csvfile']
        if not os.path.isdir('static'):
            os.mkdir('static')
        filepath = os.path.join('static', file.filename)
        file.save(filepath)

        df = pd.read_csv(filepath)
        df.drop(['YEAR', 'MONTH', 'DAY', 'HOUR'], axis=1, inplace=True)
        X = df.values
        X = preprocessing.scale(X)
        X = X.tolist()

        # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
        API_KEY = "3yJs0dfq8sweZcE9-HD02-U0BUXdFerPqonhRXH6Q-1H"
        token_response = requests.post('https://iam.cloud.ibm.com/identity/token',
                                       data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
        mltoken = token_response.json()["access_token"]

        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ['Temperature at 2 meters (C)',
                                                      'Specific Humidity at 2 meters (g/kg)', 'Surface pressure (kPa)',
                                                      'Wind speed at 10 meters (m/s)',
                                                      'Wind direction at 10 meters (Degrees)  '], "values": X}]}

        response_scoring = requests.post(
            'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/5af3653a-64b8-4212-97fd-390e08592b00/predictions?version=2021-12-04',
            json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
        pred = response_scoring.json()
        # return render_template('prediction.html', predictions = pred['predictions'][0]['values'])
        arr = []
        for x in pred['predictions'][0]['values']:
            for y in x:
                arr.append(y)
        print("Raw array: ", pred['predictions'][0]['values'])
        print("Type of array: ", type(pred['predictions'][0]['values']))
        print("Elements: ", end=' ')
        for e in arr:
            print(e, end=' ')
        print()
        return render_template('prediction_2.html', a=arr)
        # return render_template('prediction.html', predictions)
        # return predictions['predictions'][0]['values']
    return render_template('upload_2.html')

@app.route('/form', methods=['POST'])
def sendForm():
    name = request.form['fullname']
    email = request.form['email']
    message = request.form['msg']
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        # region Login
        smtp.login('kimlong101020@gmail.com', 'KimLong10102030')
        # endregion
        subject = name + " " + "question"
        body = "Guess name: " + name + "\nEmail: " + email + "\n" + "Message: " + message
        # body = u' '.join((name, email, message)).encode('utf-8').strip()
        # body = r.join((name, '\n', email, '\n', message)).encode('utf-8').strip()
        msg = f'Subject: {subject}\n\n{body}'.encode('utf-8').strip()
        smtp.sendmail('kimlong101020@gmail.com', 'longdnk18@uef.edu.vn', msg)
    return redirect(url_for('index'))

@app.route('/formContact', methods=['POST'])
def sendContactForm():
    name = request.form['fullname']
    email = request.form['email']
    message = request.form['msg']
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        # region Login
        smtp.login('kimlong101020@gmail.com', 'KimLong10102030')
        # endregion
        subject = name + " " + "question"
        body = "Guess name: " + name + "\nEmail: " + email + "\n" + "Message: " + message
        # body = u' '.join((name, email, message)).encode('utf-8').strip()
        # body = r.join((name, '\n', email, '\n', message)).encode('utf-8').strip()
        msg = f'Subject: {subject}\n\n{body}'.encode('utf-8').strip()
        smtp.sendmail('kimlong101020@gmail.com', 'longdnk18@uef.edu.vn', msg)
    return redirect(url_for('contact'))

@app.route('/userview')
def userview():
    return render_template('userview.html')

if __name__ == '__main__':
    app.run(debug=True)
