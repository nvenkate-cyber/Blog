import os
from flask import Flask, request, render_template, send_from_directory, Response
from werkzeug.security import check_password_hash, generate_password_hash
# from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# load_dotenv()
app = Flask(__name__)
# app.config['DATABASE'] = os.path.join(os.getcwd(), 'flask.sqlite')
# db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{table}'.format(
    user=os.getenv('POSTGRES_USER'),
    passwd=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=5432,
    table=os.getenv('POSTGRES_DB'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class UserModel(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(), primary_key=True)
    password = db.Column(db.String())

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User {self.username}>"

@app.route('/')
def index():
    index_list = ["We are", "R2T2", "MLH Orientation Week Hackathon Submission", "description here"]
    return render_template('index.html', title=index_list[0], title2=index_list[1], page_header=index_list[1], top_page_title=index_list[2], desc=index_list[3], url=os.getenv("URL"))

@app.route('/team_profiles')
def team_profiles():
    return render_template('team_profiles.html', page_header="Meet the team", top_page_title="MLH Orientation Week Hackathon Submission")

@app.route('/reem')
def reem():
    return render_template('reem.html')

@app.route('/nandini')
def nandini():
    return render_template('nandini.html')

@app.route('/jose')
def jose():
    return render_template('jose.html')

@app.route('/health')
def health():
    return Response(status=200)

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif UserModel.query.filter_by(username=username).first() is not None:
            error = f"User {username} is already registered."
        
        if error is None:
            new_user = UserModel(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            return f"User {username} created successfully"
        else:
            return error, 418

    ## TODO: Return a restister page
    return render_template('register.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        error = None
        user = UserModel.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password.'

        if error is None:
            return "Login Successful", 200
        else:
            return error, 418
    
    ## TODO: Return a login page
    return render_template('login.html')
