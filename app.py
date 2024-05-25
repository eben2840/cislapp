import os
from email.message import EmailMessage
import re
import ssl
import smtplib
import csv
import random
import string
import os
import datetime
from urllib import response
# from datetime import datetime
import urllib.request, urllib.parse
from sqlalchemy import func 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import distinct 
from flask import Flask, redirect, render_template, send_file, url_for,request,jsonify,get_flashed_messages, send_from_directory,make_response
from flask_migrate import Migrate
import json
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SubmitField, SelectField, IntegerField,PasswordField, SearchField
from flask_login import login_required,login_user,logout_user,current_user,UserMixin, LoginManager
from flask import(
Flask,g,redirect,render_template,request,session,url_for,flash,jsonify, send_from_directory
)
from flask_cors import CORS
import json
import time
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import secrets


app=Flask(__name__)
CORS(app)
# 'postgresql://postgres:new_password@45.222.128.55:5432/src'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://eben:eben2840@45.222.128.210:5432/ebendb'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("CENTRAL_MINISTRY_DB_URL","sqlite:///test.db")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:new_password@45.222.128.55:5432/src'
app.config['SECRET_KEY'] ="thisismysecretkey"
app.config['UPLOADED_PHOTOS_DEST'] ='uploads'
app.config['UPLOAD_FOLDER'] = 'uploads/pdfs' 
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = 'uploads' 


# photos=UploadSet('photos', IMAGES)
# configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
migrate = Migrate(app, db)
from forms import *

# mailserver=os.environ.get("presto_mail_server")
# mailport=os.environ.get("presto_mail_port")
# mailpassword=os.environ.get("presto_mail_password")

@login_manager.user_loader
def load_user(user_id):
    return Person.query.get(int(user_id))


# def sendtelegram(params):
#     url = "" + urllib.parse.quote(params)
#     content = urllib.request.urlopen(url).read()
#     print(content)
#     return content




def sendtelegram(params):
    url = "https://api.telegram.org/bot7174034710:AAGMITwp6BvnS6JPO-j2ulYiP3VOgK43LzE/sendMessage?chat_id=-4165806132&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content



class Person(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    clientname= db.Column(db.String())
    name= db.Column(db.String())
    email= db.Column(db.String())
    unique_code = db.Column(db.String(12)) 
    code= db.Column(db.String())
    phone= db.Column(db.String())
    image_file = db.Column(db.String())
    password = db.Column(db.String())
    confirm_password = db.Column(db.String(128))
    role =db.Column(db.String())
    def __repr__(self):
        return f"Person('{self.id}', {self.name}')"

class alumni(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String() )
    name= db.Column(db.String() )
    password= db.Column(db.String() )
    email= db.Column(db.String() )
    indexnumber= db.Column(db.String()  )
    telephone= db.Column(db.String()  )
    def __repr__(self):
        return f"alumni('{self.id}', {self.name}', {self.email})"
    
    
    
class Budget(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.String())
    start_date = db.Column(db.Date)  # Add start_date field
    end_date = db.Column(db.Date) 
    def __repr__(self):
        return f"Studenthalls('{self.id}', {self.budget}', {self.start_date})"


class Logger(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)  # Add start_date field
    activity = db.Column(db.String())
    tag = db.Column(db.String())
    future = db.Column(db.String())
    email = db.Column(db.String())
    implementation = db.Column(db.String())
    challenges = db.Column(db.String())

    def __repr__(self):
        return f"Logger('{self.id}', {self.activity}', {self.date})"

    
    
    
class Studenthalls(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    studentName= db.Column(db.String() )
    regno= db.Column(db.String() )
    gender= db.Column(db.String() )
    program= db.Column(db.String() )
    level= db.Column(db.String()  )
    email= db.Column(db.String()  )
    hallname= db.Column(db.String()  )
    def __repr__(self):
        return f"Studenthalls('{self.id}', {self.studentName}', {self.regno})"

class StudentData(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    studentName= db.Column(db.String() )
    studentID= db.Column(db.String() )
    studentnumber= db.Column(db.String() )
    def __repr__(self):
        return f"Studentdata('{self.id}', {self.studentName}', {self.studentnumber})"
    
    
class User(db.Model,UserMixin):
    clientid = db.Column(db.String())
    clientname = db.Column(db.String())
    staff_id = db.Column(db.String())
    id= db.Column(db.Integer, primary_key=True)
    fullname= db.Column(db.String())
    company= db.Column(db.String())
    dependant_1= db.Column(db.String())
    dependant_2= db.Column(db.String())
    dependant_3= db.Column(db.String())
    dependant_4= db.Column(db.String())
    dependant_5= db.Column(db.String())
    medial_amount= db.Column(db.String())
    position= db.Column(db.String())
    email= db.Column(db.String())
    unique_code = db.Column(db.String(12)) 
    qualities = db.Column(db.String())
    code = db.Column(db.String())
    reason = db.Column(db.String())
    campus= db.Column(db.String())
    image_file = db.Column(db.String(255))
    role =db.Column(db.String())
    def __repr__(self):
        return f"User('{self.id}', {self.fullname}, {self.campus}'"
    
    
    
class Challenge(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    task= db.Column(db.String())
    tag = db.Column(db.String())
    description = db.Column(db.String())
    start_date = db.Column(db.Date)  # Add start_date field
    end_date = db.Column(db.Date) 
   
    def __repr__(self):
        return f"Challenge('{self.id}', {self.name}, {self.tag}'"
    

class Getfunds(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    fullname= db.Column(db.String()  )
    ministry = db.Column(db.String())
    program= db.Column(db.String()   )
    email= db.Column(db.String()     )
    telephone= db.Column(db.String()     )  
    
    campus= db.Column(db.String()     )
    def __repr__(self):
        return f"User('{self.id}', {self.fullname}, {self.email}'"
    

class Faq(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    caption= db.Column(db.String()  )
    answers = db.Column(db.String())
    campus= db.Column(db.String()     )
    start_date = db.Column(db.Date)  # Add start_date field
    end_date = db.Column(db.Date) 
    def __repr__(self):
        return f"User('{self.id}', {self.caption}, {self.answers}'"
    

    
class Createclient(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String()) 
    email = db.Column(db.String()     )
    unique_code = db.Column(db.String(12)) 
    code= db.Column(db.String())
    gender = db.Column(db.String())
    phone= db.Column(db.String()    )
    image_file = db.Column(db.String())  
    def __repr__(self):
        return f"Createclient('{self.id}', {self.name}, {self.email}'"
    
      
class Cisl(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    clientid = db.Column(db.String())
    clientname = db.Column(db.String())
    name= db.Column(db.String())
    status= db.Column(db.String())
    role =db.Column(db.String())
    date = db.Column(db.Date)  
    time= db.Column(db.String()     )
    incident = db.Column(db.String() )  # Add start_date field
    description = db.Column(db.String())
    casualties = db.Column(db.String() )  # Add start_date field
    employees = db.Column(db.String() )  # Add start_date field
    reason = db.Column(db.String() )  # Add start_date field
    police = db.Column(db.String() )  # Add start_date field
    fire_force = db.Column(db.String() )  # Add start_date field
    claim = db.Column(db.String() )  # Add start_date field
    cost = db.Column(db.String() )  # Add start_date field
    name_of_contact = db.Column(db.String() )  # Add start_date field
    contact_number = db.Column(db.String() )  # Add start_date field
    def __repr__(self):
        return f"User('{self.id}', {self.name}, {self.description}'"
    
class Hospital(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String())
    clientid= db.Column(db.String())
    clientname= db.Column(db.String())
    staffname= db.Column(db.String())
    staffunique_code= db.Column(db.String())
    userid= db.Column(db.String())
    idcard= db.Column(db.String())
    name = db.Column(db.String())
    patient_name= db.Column(db.String())
    facility = db.Column(db.String() )  # Add start_date field
    location = db.Column(db.String())
    expense = db.Column(db.String())
    amount = db.Column(db.String())
    # staff_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # staff = db.relationship('User', backref=db.backref('hospitals', lazy=True))
    def __repr__(self):
        return f"User('{self.id}', {self.name}, {self.patient_name}'"
    


class Challenges(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String()  )
    number = db.Column(db.String())
    message= db.Column(db.String()     )
    def __repr__(self):
        return f"User('{self.id}', {self.name}, {self.number}'"
    
    
    
    
class Department(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    school= db.Column(db.String())
    slug= db.Column(db.String())
    def __repr__(self):
        return f"Department('{self.id}', {self.name}'"
    
class School(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    slug =db.Column(db.String)
    departments = db.Column(db.String)
    def __repr__(self):
        return f"School('{self.id}', {self.slug}')"
    
        
class Album(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    image_album=db.Column(db.String)
    def __repr__(self):
        return f"year('{self.id}', {self.image_album}'"


class Message(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    message=db.Column(db.String)
    def __repr__(self):
        return f"Message('{self.id}', {self.message}'"
    
    
class Program(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String) 
    school =db.Column(db.String) 
    department =db.Column(db.String) 
    slug =db.Column(db.String) 
    def __repr__(self):
        return f"Program('{self.id}', {self.name}'"
    
     
class Leaders(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    director=db.Column(db.String)
    directress=db.Column(db.String)
    others=db.Column(db.String)
    ministries =db.Column(db.String)
    total_number = db.Column(db.String)
    timestamp = db.Column(db.Float, default=time.time)
    def __repr__(self):
        return f"School('{self.id}', {self.others}')"

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    level = db.Column(db.String())
    schools = db.Column(db.String())
    course = db.Column(db.String())
    year = db.Column(db.String())
    pdf_filename = db.Column(db.String()) 
       
class Ask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ask = db.Column(db.String())
    
class Committee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())    
    description = db.Column(db.String())
    timestamp = db.Column(db.DateTime, default=datetime.now)
    # timestamp = db.Column(db.DateTime, default=datetime.now)     

class PDFFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    filename = db.Column(db.String(100), unique=True)
    course = db.relationship('Course', backref=db.backref('pdf_files', lazy=True))
    year = db.Column(db.Integer)

class Waitlist(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)

class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer())
    name = db.Column(db.String())
    start_date = db.Column(db.Date)
    items = db.relationship('Item', backref='group', lazy=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    quantity = db.Column(db.String())
    price = db.Column(db.String)
    tag = db.Column(db.String)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id', name='ft_item_group_id'))


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(255), nullable=False)
    hours_worked = db.Column(db.Float, nullable=False)
    date_completed = db.Column(db.Date, nullable=False)
    
    

# @app.route('/weekly-work', methods=['GET'])
# def get_weekly_work():
#     weekly_work = calculate_weekly_work()
#     return jsonify({'weekly_work_hours': weekly_work})

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
# @app.route('/backup_database', methods=['GET'])
# def backup_database():
#     source_db_path = 'test.db'  # Replace with the actual path to your SQLite database file.
#     backup_db_path = 'your_database_backup.db'  # Replace with the desired path for the backup file.

#     try:
#         shutil.copy2(source_db_path, backup_db_path)
#         return jsonify({'message': 'Database backup successful'})
#     except Exception as e:
#         return jsonify({'error': str(e)})



# # Connect to the SQLite database
# conn = sqlite3.connect('test.db')

# # SQL query to select data from your table
# query = "SELECT * FROM Person"

# # Read data into a DataFrame
# df = pd.read_sql_query(query, conn)

# # Close the database connection
# conn.close()

# # Export the data to an Excel file (output.xlsx)
# df.to_excel('output.xlsx', index=False)

# print("Data has been exported to output.xlsx.")


# email_sender = 'pay@prestoghana.com'
 
 
 
# @app.route("/sendsms", methods=["POST"])
# def send_sms():
#     if request.method == "POST":
#         data = [{
#         'name': '',  
#         'sender_id': '',
#         'mesaage': '',
#     }]
#     return jsonify (data)



# @app.route('/send_email', methods=['POST'])
# def send_email():
#     if request.method == 'POST':
#         email_receiver = [request.form['email'],'prestoghana@gmail.com', 'ebenmills200@gmail.com']
        
#         subject = '"Does what i do really matter?"'
#         # html_content = render_template('try.html') 
#         html_content = """
#         <!DOCTYPE html>
# <html>
# <head>
#     <style>
#     @font-face {
#         font-family: 'Plus Jakarta';
#         src: url('PlusJakartaSans-VariableFont_wght.woff2') format('woff2-variations'),
#              url('PlusJakartaSans-Italic-VariableFont_wght.woff2') format('woff2-variations');
#         font-weight: 100 900; /* Adjust font weights based on available weights */
#         font-style: normal;
#     }

#     body {
#         font-family: 'Plus Jakarta', sans-serif;
#     }
# </style>

# </head>
# <body>
#  <div class="container">
 
    
#             <h4 class="h1 hero-title">Central University Campus Ministry</h4>
#     <p>Hello there!. 
#     <br/> We are grateful for your patience, your data has been retreived successfully.
#     <br/> Have an amazing day.</p>

#     <h1>
#     </div>
# </body>
# </html>
#         """


#         em = EmailMessage()
#         em['From'] = f"Presto Mail <{email_sender}>"
#         em['To'] = email_receiver
#         em['Subject'] = subject
#         em.set_content('')  
#         em.add_alternative(html_content, subtype='html')

#         context = ssl.create_default_context()

#         with smtplib.SMTP_SSL(mailserver, 465, context=context, ) as smtp:
#             smtp.login(email_sender, mailpassword)
#             smtp.sendmail(email_sender, email_receiver, em.as_string())
    
# #         return redirect(url_for('userbase'))
# new=Committee(name=form.name.data, 
#                   description=form.description.data,
#                   )

@app.route('/group', methods=['GET', 'POST'])
def group():
    form = GroupForm()

    if form.validate_on_submit():
        group = Groups(
            userId=current_user.id,
            name=form.name.data,
            start_date=form.start_date.data 
        )
        db.session.add(group)
        db.session.commit()

        flash("You just added a new Client")
        return redirect(url_for('homelook'))

    print(form.errors)
    return render_template('groups.html', form=form)



def generate_unique_code():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


# code = generate_unique_code()
# print("new code" + code)



@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    form = AddItemForm()
   
    form.group.choices = [(group.id, group.name) for group in Groups.query.all()]

    if form.validate_on_submit():
        item = Item(
            name=form.item_name.data,
            group_id=form.group.data,
            tag=form.tag.data,
            price=form.price.data,
            quantity=form.quantity.data
        )
        
        db.session.add(item)
        db.session.commit()
        
        # print(form.name.data)
        # print(form.group_id.data)
        
       
            
        flash("Staff added successfully", "Success")

        return redirect(url_for('homelook'))

    print(form.errors)
    return render_template('add_item.html', form=form)

    
radio = 'yboateng057@gmail.com'
email_password = 'hsgtqiervnkabcma'
radio_display_name = 'CISL Team'

# users_data = [
#     {'email': 'user1@example.com', 'date': '2022-01-01', 'activity': 'Activity 1', 'implementation': 'Implementation 1', 'tag': 'Tag 1', 'challenges': 'Challenges 1', 'future': 'Future 1'},
# ]

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        email_receiver = request.form['email']
        subject = 'Welcome to CISL'
        
        
        
        
        user = User.query.first()
       
# users = User.query.order_by(User.id.desc()).all()   
        users=User.query.order_by(User.id.desc()).all()
        html_content = render_template('printout.html',users=users)
        
        # return render_template("emailsender.html",users=users)


        # users = Logger.query.order_by(Logger.id.desc()).all()
        # HTML content of the email
        # html_content = render_template('printout.html',users=users)
        # html_content = """
        # <!DOCTYPE html>
        # <html>
        # <head>
        #     <style>
        #     @font-face {
        #         font-family: 'Plus Jakarta';
        #         src: url('PlusJakartaSans-VariableFont_wght.woff2') format('woff2-variations'),
        #              url('PlusJakartaSans-Italic-VariableFont_wght.woff2') format('woff2-variations');
        #         font-weight: 100 900; /* Adjust font weights based on available weights */
        #         font-style: normal;
        #     }

        #     body {
        #         font-family: 'Plus Jakarta', sans-serif;
        #     }
        #     </style>
        # </head>
        # <body>
        #         <div class="container">
        #             <div style="display:flex; padding:10px; justify-content:space-between;">
        #                 AbiTrack  🚀
        #                   </div>
        #              <h3 style="text-align:center; font-size:40px;">Welcome to AbiTrack Management System
                   
        #         </h3>      
        #             <img src="https://abitu-ce1b6c8eb118.herokuapp.com/static/asets/images/portfolio/Portfolio.jpg" style="width:100%;">
                          
               
                
                
                
              

               
        #     </div>
            
            
        # </body>
        # </html>
        # """

    
        em = EmailMessage()
        em['From'] = f'{radio_display_name} <{radio}>'
        # em['From'] = f'{radio_display_name}'
        # em['From'] = f'{radio_display_name} <{radio}>'  # Use both display name and email address
        # em.replace_header('From', radio_display_name)  
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content('')
        em.add_alternative(html_content, subtype='html')
        context = ssl.create_default_context()

       
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(radio, email_password)
            smtp.sendmail(radio, email_receiver, em.as_string())

        return redirect(url_for('main')) 



@app.route('/invite', methods=['GET', 'POST'])
def invite():
    # print("this is super dope")
    
    form=WaitForm()
    if form.validate_on_submit():
        wait=Waitlist(
            email=form.email.data
            )
        db.session.add(wait)
        db.session.commit()
        # send_email()
        print(form.email.data)
        
        flash("Thanks for Joining Our Waiting List")
        return redirect('/main')
    print(form.errors)
    return render_template('preview.html', form=form)



@app.route('/dashboard')
@login_required
def dashboard():
    total_students = User.query.count()
    users_with_positions = db.session.query(User.fullname, User.position).all()
    total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()

    print(users_with_positions)
    total_male = User.query.filter_by(gender='Male').count()
    total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    print(current_user)
    # flash(f"There was a problem", 'success')
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('dashboard.html', title='dashboard',total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_female=total_female, total_male=total_male,total_students=total_students,users_with_positions=users_with_positions)


@app.route('/ministries', methods=['GET', 'POST'])
def ministries():
    total_media = User.query.filter_by(ministry='Media').count()
    media_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Media').scalar()
    mcc_count = db.session.query(func.count(User.id)).filter(User.ministry == 'MCC').scalar()
    praise_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Praise & Worship').scalar()
    cjc_count = db.session.query(func.count(User.id)).filter(User.ministry == 'CJC').scalar()
    lv_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Levite Generation').scalar()
    communion_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Communion').scalar()
    protocol_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Protocol').scalar()
    dis_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Discipleship').scalar()
    missions_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Missons').scalar()
    coun_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Counselling').scalar()
    prayer_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Prayer Ministry').scalar()
    lord_count = db.session.query(func.count(User.id)).filter(User.ministry == 'Lords Band').scalar()
    return render_template('year.html',title='Ministries',total_media=total_media,mcc_count=mcc_count, lord_count=lord_count,prayer_count=prayer_count,coun_count=coun_count,missions_count=missions_count,lv_count=lv_count,cjc_count=cjc_count, praise_count=praise_count,dis_count=dis_count, communion_count=communion_count, media_count=media_count,protocol_count=protocol_count)


@app.route('/query_pdf', methods=['GET', 'POST'])
def query_pdf():
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        level = request.form.get('level')
        year = request.form.get('year')
        course = Course.query.filter_by(name=course_name, level=level).first()
        if course:
            pdf_files = PDFFile.query.filter_by(course=course, year=year).all()
            return render_template('pdf_results.html', course=course, pdf_files=pdf_files)
        else:
            return "Course not found"
    courses = Course.query.all()
    return render_template('query.html', courses=courses)




@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)




# @app.route('/download_pdf/<filename>')
# def download_pdf(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form.get('course_name')
        level = request.form.get('level')
        year = request.form.get('year')
        pdf_file = request.files.get('pdf_file')  

        existing_course = Course.query.filter_by(name=course_name, level=level, year=year).first()
        if existing_course:
            return "Course already exists"

        new_course = Course(name=course_name, level=level, year=year)
        try:
            db.session.add(new_course)
            db.session.commit()
            
            if pdf_file:
                filename = secure_filename(pdf_file.filename)

                timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                unique_filename = f"{timestamp}_{filename}"

                pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
                pdf = PDFFile(course=new_course, filename=unique_filename)
                db.session.add(pdf)
                db.session.commit()
            return redirect('/levels')
        except Exception as e:
            db.session.rollback()
            return f"Error adding the course: {str(e)}"
    return render_template('add_course.html')




@app.route('/searchcode', methods=['GET', 'POST'])
def searchcode():
    # sendtelegram("New User on Pasco Portal level 100")
    hundred = Course.query.filter_by(level='100').all()
    return render_template('level100.html', hundred=hundred)

@app.route('/level200', methods=['GET', 'POST'])
def level200():
    sendtelegram("New User on Pasco Portal level 200")
    two = Course.query.filter_by(level='200').all()
    return render_template('level200.html', two=two)


@app.route('/emailsender', methods=['GET', 'POST'])
def emailsender():
    return render_template('emailsender.html')

@app.route('/level300', methods=['GET', 'POST'])
def level300():
    sendtelegram("New User on Pasco Portal level 300")
    two = Course.query.filter_by(level='300').all()
    return render_template('level300.html', two=two)

@app.route('/level400', methods=['GET', 'POST'])
def level400():
    sendtelegram("New User on Pasco Portal level 400")
    two = Course.query.filter_by(level='400').all()
    return render_template('level400.html', two=two)



@app.route('/uploaded')
def uploaded():
    sendtelegram("Uploading a new Pasco")
    return render_template('uploaded.html')  


@app.route('/levels')
def levels():
    return render_template('list_levels.html') 



@app.route('/pascoadmin', methods=['GET', 'POST'])
def pascoadmin():
    courses = Course.query.all() 
    return render_template('pascoadmin.html', courses=courses) 


@app.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template('blog.html')

@app.route('/passqo', methods=['GET', 'POST'])
def passqo():
    sendtelegram("New User on Pasco Portal")
    return render_template('passqo.html')


@app.route('/school', methods=['GET', 'POST'])
def school():
    return render_template('school.html')

@app.route('/closed', methods=['GET', 'POST'])
def closed():
    return render_template('closed.html')


@app.route('/message', methods=['GET', 'POST'])
def messages():
    users =Committee.query.order_by(Committee.id.desc()).all()
    return render_template('messages.html',users=users)


@app.route('/analytics', methods=['GET', 'POST'])
def analytics():
    return render_template('analytics.html')


@app.route('/level', methods=['GET', 'POST'])
def level():
    courses = Course.query.all() 
    total_100 = Course.query.filter_by(level='100').count()
    total_200 = Course.query.filter_by(level='200').count()
    total_300 = Course.query.filter_by(level='300').count()
    total_400 = Course.query.filter_by(level='400').count()
    return render_template('level.html', courses=courses, total_100=total_100,total_200=total_200,total_300=total_300,total_400=total_400)



@app.route('/level/<int:userid>', methods=['GET', 'POST'])
def viewlevel(userid):
    print("Fetching one")
    profile=Course.query.get_or_404(userid)
    sendtelegram(profile.name + "" + "New download")
    return render_template("levelid.html", profile=profile, title="list")
 
 



@app.route('/mainquestion', methods=['GET', 'POST'])
def mainquestion():
    return render_template('mainquestion.html')


@app.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template('landing.html')



@app.route('/experience', methods=['GET', 'POST'])
def experience():
    return render_template('experience.html')


@app.route('/pages', methods=['GET', 'POST'])
def pages():
    return render_template('pages.html')

@app.route('/base', methods=['GET', 'POST'])
def base():
    return render_template('base.html')

@app.route('/landingpage', methods=['GET', 'POST'])
@login_required
def landingpage():
    
    current_hour = datetime.now().hour
    greeting = ""
    
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
        
    form=WaitForm()
    if form.validate_on_submit():
        wait=Waitlist(
            email=form.email.data
            )
        db.session.add(wait)
        db.session.commit()
        send_email()
        print(form.email.data)
       
        flash("Invitation Sent to" + ' ' + wait.email)
        return redirect('main')
    print(form.errors)
   
    current_time = datetime.now()
    # all_product= User.query.count()
    # outstock = db.session.query(Item.quantity).filter(Item.quantity < 5).all()
    outstock = db.session.query(Item).filter(Item.quantity < 5).count()
    
    users = Budget.query.order_by(Budget.id.desc()).all()
    total_budget = sum(int(user.budget) for user in users)  # Convert budget to int before summation
    
    weekly_work = calculate_weekly_work()
    workload_limit = 1000  # Assuming a predefined workload limit of 1000 units
    workload_percentage = calculate_workload_percentage(weekly_work, workload_limit)  
    # outstock = db.session.query(Item).filter(Item.quantity < 5).count()
    total_students = User.query.count()
    instock = Item.query.count()
    total_getfundstudents = Getfunds.query.count()
    total_Faq = Faq.query.count()
    total_challenges = Challenge.query.count()
    total_message = Committee.query.count()
    total_stock = Item.query.count()
    total_cat = Groups.query.filter_by(userId=current_user.id).count()
    users_with_positions = db.session.query(User.fullname, User.position).filter(User.position.isnot(None)).all()
    total_people_with_positions = db.session.query(User).filter(User.position != '').count()
   
   
    # total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()
    message = Message.query.count()
    print(users_with_positions)
    user =Committee.query.order_by(Committee.id.desc()).all()
    # total_male = User.query.filter_by(gender='Male').count()
    # total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    challenges=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    online =Person.query.order_by(Person.id.desc()).all()
    print(current_user)
    # flash(f"There was a problem", 'success')
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('landingpage.html',outstock=outstock, instock=instock, title='dashboard',user=user, form=form,
          total_budget=total_budget,   workload_percentage=workload_percentage,        current_time=current_time, total_cat=total_cat,  total_stock=total_stock, greeting=greeting, total_challenges=total_challenges,total_message=total_message,online=online,message=message,total_Faq=total_Faq, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_students=total_students,users_with_positions=users_with_positions, total_getfundstudents=total_getfundstudents,challenges=challenges)



# @app.route('/inventory', methods=['GET', 'POST'])
# def landingpage():
#     return render_template('landingpage.html')


@app.route('/supportunit', methods=['GET', 'POST'])
def supportunit():
    # form=CommitteeForm()
    # if form.validate_on_submit():
    #         new=Committee(name=form.name.data, 
    #                description=form.description.data,  
    #               )
    #         db.session.add(new)
    #         db.session.commit()
    #         # send_email()
    #         return redirect('leadership')
    # print(form.errors)
    return render_template("support.html")





@app.route('/addcommittee', methods=['GET', 'POST'])
def addcommittee():
    form=CommitteeForm()
    if form.validate_on_submit():
            new=Committee(name=form.name.data, 
                   description=form.description.data,  
                  )
            db.session.add(new)
            db.session.commit()
            # send_email()
            return redirect('leadership')
    print(form.errors)
    return render_template("addcommittee.html", form=form)



@app.route('/main', methods=['GET', 'POST'])
@login_required
def main():
    unique_code = current_user.unique_code
    current_hour = datetime.now().hour
    greeting = ""
    
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
        
    form=WaitForm()
    if form.validate_on_submit():
        wait=Waitlist(
            email=form.email.data
            )
        db.session.add(wait)
        db.session.commit()
        send_email()
        print(form.email.data)
       
        flash("Invitation Sent to" + ' ' + wait.email)
        return redirect('main')
    print(form.errors)
   
    current_time = datetime.now()

    message = Message.query.count()

    if current_user.role == 'admin':
        total_claims=Cisl.query.count()
    else:
        total_claims=Cisl.query.filter_by(clientid=str(current_user.id)).count()
    

    if current_user.role == 'admin':
        users = Cisl.query.order_by(Cisl.id.desc()).all()
        print(users)
    else:
        users=Cisl.query.filter_by(clientid=str(current_user.name)).order_by(Cisl.id.desc()).all()
        # users=Cisl.query.filter_by(id=current_user.id).order_by(Cisl.id.desc()).all()

    print(current_user)
 
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('current.html',unique_code=unique_code, instock=instock, title='dashboard',form=form,total_claims=total_claims,
            current_time=current_time, greeting=greeting, message=message, users=users, challenges=challenges)



@app.route('/cisl', methods=['POST','GET'])
def cisl():
    form = CislForm()
    if form.validate_on_submit():
        cisl= Cisl(
            clientid=current_user.name,
                name=form.name.data,        
                   date=form.date.data,
                   time=form.time.data,
                   incident=form.incident.data,
                   description=form.description.data,
               casualties=form.casualties.data,
               employees=form.employees.data, 
               reason=form.reason.data,
               police=form.police.data,
               fire_force=form.fire_force.data,
               cost=form.cost.data,
               claim=form.claim.data,
               name_of_contact=form.name_of_contact.data,
               contact_number=form.contact_number.data
               )
        print(cisl)
        db.session.add(cisl)
        db.session.commit()
        
        # sendtelegram("New User Claim:"
        # )
        sendtelegram("New Claim Notification" + '\n' + 
                     "" + '\n' +
                      "Name = " + cisl.name  + '\n' + 
                    #   "Date = " + cisl.date  + '\n' + 
                      "Time = " + cisl.time  + '\n' + 
                      "Incident = " + cisl.incident  + '\n' + 
                      "Description = " + cisl.description  + '\n' + 
                    "Casualties = " + cisl.casualties  + '\n' + 
                    "Labour Office = " + cisl.employees + '\n' + 
                    "Indicate Reason = " + cisl.reason + '\n' + 
                    "Police = " + cisl.police + '\n' + 
                    "Fire_Force = " + cisl.fire_force + '\n' + 
                    "Cost = " + cisl.cost + '\n' + 
                    "Claim = " + cisl.claim + '\n' + 
                    "Name_Of_Contact = " + cisl.name_of_contact + '\n' + 
                    "Contact_Number = " + cisl.contact_number 
                    )  
        flash("You just sent a new claim", "success")
        return redirect('main')
    print(form.errors) 
    
    return render_template('cisl.html', form=form)



@app.route('/medicals', methods=['GET', 'POST'])
@login_required
def medicals():
    users=Hospital.query.order_by(Hospital.id.desc()).all()
    return render_template("medicals.html",users=users)



@app.route('/staffmedicals/<int:userid>', methods=['GET', 'POST'])
@login_required
def staffmedicals(userid):
    # users=Hospital.query.get_or_404(userid)
    users = Hospital.query.filter_by(id=userid).first() 
    return render_template("staffmedicals.html",users=users)


@app.route('/addstaff', methods=['GET', 'POST'])
@login_required
def addstaff():
    form=Adduser()
    if form.validate_on_submit():
        unique_code = secrets.token_hex(6)  
        medial_amount = 1000
        if len(str(form.code.data)) != 8:
                flash('Unique Code must be exactly 8 digits.', 'danger')
                return redirect(url_for('addstaff'))
        else:
            new=User(
                clientname = current_user.id,
                fullname=form.fullname.data,      
                   company=form.company.data,
                   position=form.position.data,
                   dependant_1=form.dependant_1.data,
                   dependant_2=form.dependant_2.data,
                   dependant_3=form.dependant_3.data,
                   dependant_4=form.dependant_4.data,
                   dependant_5=form.dependant_5.data,
                   email=form.email.data,
                   reason=form.reason.data,
                   unique_code=unique_code,
                   code=form.code.data,
                  medial_amount=medial_amount,
                   campus=form.campus.data,
                   qualities=form.qualities.data,
               image_file=form.image_file.data
                  )
            db.session.add(new)
            db.session.commit()
            send_email()
            flash("Welcome to CISL, " + " " + new.qualities + ". " + " Kindly Check your email for you ID Number","success")
            return redirect('/')
    print(form.errors)
    return render_template("addAlumni.html", form=form)


@app.route('/auth', methods=['POST','GET'])
@login_required
def auth():
      
    if current_user.role == 'admin':
        total_client=User.query.count()
    else:
        total_client=User.query.filter_by(clientname=str(current_user.id)).count()
    

    #Hospital Module
    if current_user.role == 'admin':
        total_medicals=Hospital.query.count()
    else:
        total_medicals=Hospital.query.filter_by(clientname=str(current_user.id)).count()
    
    
    if current_user.role =='admin':
        users=User.query.order_by(User.id.desc()).all()
        print(users)
    else:
        users=User.query.filter_by(clientname=str(current_user.id)).order_by(User.id.desc()).all()
    return render_template("auth.html",users=users, total_client=total_client,total_medicals=total_medicals )




@app.route('/staffid/<int:userid>', methods=['GET', 'POST'])
def staffid(userid):
    users = User.query.filter_by(id=userid).first() 
    return render_template("staffid.html",users=users)




@app.route('/searchstaff', methods=[ 'POST'])
def searchstaff():
    form= Search()
    if request.method == 'POST': 
        posts =User.query
        if form.validate_on_submit():
            postsearched=form.searched.data
            posts =posts.filter(User.unique_code.like('%'+ postsearched + '%') )
            posts =posts.order_by(User.qualities).all()
            # posts =posts.order_by(User.position).all() 
            flash("You searched for "+ postsearched, "success")  
            print(posts)   
    return render_template("searchstaff.html", form=form, searched =postsearched, posts=posts)



@app.route('/hospital/<int:userid>', methods=['POST','GET'])
def hospital(userid):
    
    form = HospitalForm()
    company = Person.query.filter_by(id=userid).first() 
    staff = User.query.filter_by(id=userid).first() 
    if form.validate_on_submit():
        hospital= Hospital(
                userid=userid,
                # companyname=company.name,
                clientid=staff.clientid,
                staffname=staff.qualities,
                staffunique_code=staff.unique_code,
                idcard=form.idcard.data,        
                name=form.name.data,        
                patient_name=form.patient_name.data,
                facility=form.facility.data,
                location=form.location.data,
                expense=form.expense.data,
                amount=form.amount.data)
        print(hospital)
        db.session.add(hospital)
        db.session.commit()
        print(hospital)
        flash("Medical Scheme Utilisation Sent, We will reach out to you soon.", "success")
        return redirect('/homelook')    
    elif not staff:
        flash("Inactive User")
        return redirect(url_for('homelook'))
    print(form.errors) 
    return render_template('hospital.html', form=form, users={'id': userid})



@app.route('/client', methods=['GET', 'POST'])
def client():
    form=CreateclientForm()
    if form.validate_on_submit():
            new=Createclient(name=form.name.data,        
                   email=form.email.data,
                   phone=form.phone.data,
                   gender=form.gender.data,
                   code=form.code.data, 
               image_file=form.image_file.data
                  )
            db.session.add(new)
            db.session.commit()
            # send_email()
            flash("You just added a new product",
                  "success")
            return redirect('auth')
    print(form.errors)
    return render_template("client.html", form=form, title='addalumni')



static_timestamp = datetime.now() 

@app.route('/indox', methods=['GET', 'POST'])
def indox():
    current_time = datetime.now()
    user=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("indox.html", user=user,current_time=current_time)

@app.route('/authmessage', methods=['GET', 'POST'])
def authmessage():
    form=CommitteeForm()
    if form.validate_on_submit():
            new=Committee(name=form.name.data, 
                  description=form.description.data,
                  timestamp=static_timestamp
                  )
            db.session.add(new)
            db.session.commit()
            flash("You just sent a BoardCast",
                  "success")
            return redirect('main')
    print(form.errors)
    return render_template("authmessage.html",title='authmessage',form=form, current_time=static_timestamp)


@app.route('/authtask', methods=['GET', 'POST'])
def authtask():
    form=ChallengesForm()
    if form.validate_on_submit():
            new=Challenge(name=form.name.data, 
                   tag=form.tag.data,
                   task=form.task.data,
                   description=form.description.data,
                   start_date=form.start_date.data,  
                    end_date=form.end_date.data
                  )
            db.session.add(new)
            db.session.commit()
            flash("You just added a New Task",
                  "success")
            return redirect('main')
    print(form.errors)
    return render_template("authtask.html", form=form)

@app.route('/logger', methods=['GET', 'POST'])
def logger():
    form = LogForm()
    print("-----------")
    # print(tag)
    users=Logger.query.order_by(Logger.id.desc()).all()
    if form.validate_on_submit():
        new=Logger(
            activity=form.activity.data,
            date=form.date.data,
            future=form.future.data,
            challenges=form.challenges.data,
            implementation=form.implementation.data,
            tag=form.tag.data,
            email=form.email.data
        )
        db.session.add(new)
        db.session.commit()
        send_email()
        
        sendtelegram("New Log Added" + '\n' + 
                   
                      "Name = " + new.activity  + '\n' + 
                    #   "Date = " + new.date  + '\n' + 
                      "Time = " + new.challenges  + '\n' + 
                      "Incident = " + new.implementation  + '\n' + 
                      "Description = " + new.tag
                    )  
        print(new.tag)
        # print(tag)
        print(new)
        
        flash("You just added a new Log", 'success')
        return redirect("logger")
    print(form.errors)
    return render_template('logger.html',form=form,users=users)


@app.route('/printout', methods=['GET', 'POST'])
def printout():
    users=Logger.query.order_by(Logger.id.desc()).all()
    return render_template('/printout.html',users=users)



@app.route('/authchallenge', methods=['GET', 'POST'])
def authchallenge():
    form=FaqForm()
    if form.validate_on_submit():
        
            new=Faq(
                caption=form.caption.data, 
                answers=form.answers.data, 
                campus=form.campus.data, 
                start_date=form.start_date.data,  
            end_date=form.end_date.data
                  )
            db.session.add(new)
            db.session.commit()
            # send_email()
           
            session['message'] = "You just added a New Challenge."
            session['category'] = "success"
        
            flash("You just added a New Challenge.",
                  "success")
            return redirect('main')
            
    print(form.errors)
    # current_time = datetime.now()
    return render_template("authchallenge.html", form=form)
    # return render_template("authchallenge.html", form=form, current_time=current_time)


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form=AddGetfunds()
    if form.validate_on_submit():
        
            new=Getfunds(fullname=form.fullname.data, 
                   email=form.email.data, 
                   telephone=form.telephone.data,    
                   program=form.program.data, 
                  campus=form.campus.data, 
                  ministry = form.ministry.data
                  )    
            db.session.add(new)
            db.session.commit()
            # send_email() 
            flash("Thank you for filling the feedback form, Someone from our team will contact you shortly.",
                  "success")
            return redirect('/thank')
            
    print(form.errors)
    return render_template("feedback.html", form=form, title='addalumni')



@app.route('/getfunds', methods=['GET', 'POST'])
def getfunds():
    form=AddGetfunds()
    if form.validate_on_submit():
        
            new=Getfunds(fullname=form.fullname.data, 
                   email=form.email.data,  
                   ministry=form.ministry.data,    
                   program=form.program.data,  
                   telephone=form.telephone.data,       
                   campus=form.campus.data,
                  )
       
            db.session.add(new)
            db.session.commit()
            flash("Thank you for filling the Getfund form.", "success")
            return redirect('/')
            
    print(form.errors)
    return render_template("getfunds.html", form=form)




@app.route('/ask', methods=['GET', 'POST'])
def ask():
    form = AskForm()
    if form.validate_on_submit():
        question = Ask(
            ask=form.ask.data,
            
        )
        print(question)
        db.session.add(question)
        db.session.commit()
        flash("Delivered", "success")
        return redirect('/ask')
    ask=Ask.query.order_by(Ask.id.desc()).all()
    return render_template('ask.html',form=form, ask=ask)  

@app.route('/addinfo', methods=['GET', 'POST'])
def leadersadd():
    form = Addinfo()
    if form.validate_on_submit():
        new_course = Course(
            name=form.name.data,
            level=form.level.data,
            schools=form.schools.data,
            year=form.year.data
        )
        if form.pdf_file.data:
            pdf_file = form.pdf_file.data
            filename = secure_filename(pdf_file.filename)
            pdf_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new_course.pdf_filename = filename
        
        print(new_course)
        db.session.add(new_course)
        db.session.commit()
        flash("Thank you for adding a pasco", "success")
        return redirect('/uploaded')
    

    print(form.errors)
    return render_template("leadersadd.html", form=form)

@app.route('/src', methods=['GET', 'POST'])
def src():
    form=ChallengesForm()
    if form.validate_on_submit():
        
            new=Challenges(
                name=form.name.data, 
                number=form.number.data, 
                message=form.message.data, 
                  )
            db.session.add(new)
            db.session.commit()
            # send_email()
        
            flash("Thank you for filling the form, We will response as soon as possible.",
                  "success")
            return redirect('/')
    users=Committee.query.order_by(Committee.id.desc()).all()
    faq=Faq.query.order_by(Faq.id.desc()).all()
    return render_template("blogme.html", users=users,faq=faq,form=form)


    
    
@app.route('/aboutsrc', methods=['GET', 'POST'])
def aboutsrc():
    users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("aboutme.html",users=users)
 

@app.route('/committee', methods=['GET', 'POST'])
def committee():
    users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("committee.html",users=users)
 

   
# @app.route('/leadership/<int:userid>', methods=['GET', 'POST'])
# def leadership(userid):
#     profile=Committee.query.get_or_404(userid)
#     return render_template("leadership.html", profile=profile,)


   
@app.route('/residential', methods=['GET', 'POST'])
def residential():
    return render_template("residential.html")


@app.route('/commercial', methods=['GET', 'POST'])
def commercial():
    return render_template("commercial.html")


@app.route('/support', methods=['GET', 'POST'])
def support():
    return render_template("support.html")



@app.route('/stockmaster', methods=['GET', 'POST'])
def stockmaster():
    return render_template("stockmaster.html")



@app.route('/claims', methods=['POST','GET'])
def claims():
    return render_template("claims.html")

@app.route('/medicaladministration', methods=['POST','GET'])
def medicaladministration():
    return render_template("meds.html")



@app.route('/verify_code', methods=['GET', 'POST'])
def verify_code():  
    if request.method == 'POST':
        unique_code = request.form.get('unique_code').strip()
        code = request.form.get('code').strip()
        user = User.query.filter_by(unique_code=unique_code).first()
        
        if user and user.code == code:
            session['user_id'] = user.id
            return redirect(url_for('makeclaim'))
        else:
            flash('Invalid unique code or code. Please try again.', 'danger')
    return render_template('verify_code.html')




@app.route('/update_claim_status/<int:id>/<string:status>', methods=['POST', 'GET'])
def update_claim_status(id,status):
    print("Update_claim_status")
    print("id:",id)
    print("status:",status)
    try:
        cisl= Cisl.query.get_or_404(id)
        print("cisl:",cisl)
        cisl.status=status
        db.session.commit()
        print("cisl.status:",cisl.status)
    except Exception as e:
        print(e)
        print("status:",cisl.status)
        flash ("Status Successfully Changed")
    return redirect (url_for('main'))




        
    
    





@app.route('/makeclaim', methods=['POST','GET'])
def makeclaim():
    user_id = session.get('user_id')
    if user_id is None:
        flash('Please verify your code first.', 'danger')
        return redirect(url_for('verify_code'))
    user = User.query.get_or_404(user_id)
    form = CislForm()
    if form.validate_on_submit():
        cisl= Cisl(
            clientid=user.id,
            clientname=user.qualities,
                # status=user.status,        
                name=form.name.data,        
                   date=form.date.data,
                   time=form.time.data,
                   incident=form.incident.data,
                   description=form.description.data,
               casualties=form.casualties.data,
               employees=form.employees.data, 
               reason=form.reason.data,
               police=form.police.data,
               fire_force=form.fire_force.data,
               cost=form.cost.data,
               claim=form.claim.data,
               name_of_contact=form.name_of_contact.data,
               contact_number=form.contact_number.data
               )
        print(cisl)
        db.session.add(cisl)
        db.session.commit()
        
        # sendtelegram("New User Claim:"
        # )
        sendtelegram("New Claim Notification" + '\n' + 
                     "" + '\n' +
                      "Name = " + cisl.name  + '\n' + 
                    #   "Date = " + cisl.date  + '\n' + 
                      "Time = " + cisl.time  + '\n' + 
                      "Incident = " + cisl.incident  + '\n' + 
                      "Description = " + cisl.description  + '\n' + 
                    "Casualties = " + cisl.casualties  + '\n' + 
                    "Labour Office = " + cisl.employees + '\n' + 
                    "Indicate Reason = " + cisl.reason + '\n' + 
                    "Police = " + cisl.police + '\n' + 
                    "Fire_Force = " + cisl.fire_force + '\n' + 
                    "Cost = " + cisl.cost + '\n' + 
                    "Claim = " + cisl.claim + '\n' + 
                    "Name_Of_Contact = " + cisl.name_of_contact + '\n' + 
                    "Contact_Number = " + cisl.contact_number 
                    )  
        flash("You just sent a new claim", "success")
        return redirect('/')
    print(form.errors) 
    return render_template('makeclaim.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def homme():
        return render_template("index1.html")


@app.route('/404', methods=['GET', 'POST'])
def working():
        users=User.query.order_by(User.id.desc()).all()
        return render_template("404.html",users=users)

@app.route('/thank', methods=['GET', 'POST'])
def thank():
    return render_template("thank.html")


@app.route('/stock', methods=['GET', 'POST'])
def stock():
    return render_template("stock.html")


@app.route('/showchallenge', methods=['GET', 'POST'])
def showchallenge():
    users=Faq.query.order_by(Faq.id.desc()).all()
    return render_template("showchallenge.html",users=users)


@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template("faq.html")


@app.route('/experience_client', methods=['GET', 'POST'])
def experiencee():
    return render_template("experiencee.html")

@app.route('/coverage', methods=['GET', 'POST'])
def coverage():
    return render_template("coverage.html")

@app.route('/premiums', methods=['GET', 'POST'])
def premiums():
    return render_template("premiums.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")

@app.route('/placements', methods=['GET', 'POST'])
def placements():
    return render_template("placements.html")


@app.route('/task', methods=['GET', 'POST'])
def task():
    users=Challenge.query.order_by(Challenge.id.desc()).all()
    return render_template("task.html",users=users)


 
       
@app.route('/annoucement', methods=['GET', 'POST'])
def annoucement():
    users=Committee.query.order_by(Committee.id.desc()).all()
    user=User.query.order_by(User.id.desc()).all()
    return render_template("annoucement.html",users=users,user=user)

       
@app.route('/constitution', methods=['GET', 'POST'])
def constitution():
    users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("consti.html",users=users)
    
        

       
@app.route('/person', methods=['GET', 'POST'])
@login_required
def person():
    current_hour = datetime.now().hour
    greeting = ""
    
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
        
    form=WaitForm()
    if form.validate_on_submit():
        wait=Waitlist(
            email=form.email.data
            )
        db.session.add(wait)
        db.session.commit()
        send_email()
        print(form.email.data)
       
        flash("Invitation Sent to" + ' ' + wait.email)
        return redirect('main')
    print(form.errors)
   
    current_time = datetime.now()
    # all_product= User.query.count()
    # outstock = db.session.query(Item.quantity).filter(Item.quantity < 5).all()
    # outstock = db.session.query(Item).filter(Item.quantity < 5).count()
    
    users = Budget.query.order_by(Budget.id.desc()).all()
    total_budget = sum(int(user.budget) for user in users)  # Convert budget to int before summation
    
  
    # outstock = db.session.query(Item).filter(Item.quantity < 5).count()
    total_students = User.query.count()
    instock = Item.query.count()
    total_getfundstudents = Getfunds.query.count()
    total_Faq = Faq.query.count()
    total_challenges = Challenge.query.count()
    total_message = Committee.query.count()
    total_stock = Item.query.count()
    total_cat = Groups.query.filter_by(userId=current_user.id).count()
    users_with_positions = db.session.query(User.fullname, User.position).filter(User.position.isnot(None)).all()
    total_people_with_positions = db.session.query(User).filter(User.position != '').count()
   
   
    # total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()
    message = Message.query.count()
    print(users_with_positions)
    user =Committee.query.order_by(Committee.id.desc()).all()
    # total_male = User.query.filter_by(gender='Male').count()
    # total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    challenges=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    online =Person.query.order_by(Person.id.desc()).all()
    print(current_user)
    # flash(f"There was a problem", 'success')
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('person.html', instock=instock, title='dashboard',user=user, form=form,
          total_budget=total_budget,         current_time=current_time, total_cat=total_cat,  total_stock=total_stock, greeting=greeting, total_challenges=total_challenges,total_message=total_message,online=online,message=message,total_Faq=total_Faq, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_students=total_students,users_with_positions=users_with_positions, total_getfundstudents=total_getfundstudents,challenges=challenges)

       
@app.route('/personid', methods=['GET', 'POST'])
def personid():
    # users=Committee.query.order_by(Committee.id.desc()).all()
    return render_template("personid.html")
    
        

 
@app.route('/budget', methods=['GET', 'POST'])
def budget():
    users=Budget.query.order_by(Budget.id.desc()).all()
    
    form=Budgetform()
    if form.validate_on_submit():
            new=Budget(budget=form.budget.data,
                    start_date=form.start_date.data,
                    end_date=form.end_date.data
                
                  )
            db.session.add(new)
            db.session.commit()
            flash("New Budget Added", "success")
            return redirect('budget')
    
    print(form.errors)
    return render_template("budget.html", form=form, title='addalumni',users=users)


 
@app.route('/adminadd', methods=['GET', 'POST'])
def adminadd():
    form=Adduser()
    
    if form.validate_on_submit():
            new=User(fullname=form.fullname.data,
                    ministry=form.ministry.data,
                   email=form.email.data,  
                   gender=form.gender.data,  
                   program=form.program.data,  
                   telephone=form.telephone.data,      
               image_file=form.image_file.data
                  )
            db.session.add(new)
            db.session.commit()
            flash("New Person added", "success")
            return redirect('main')
    print(form.errors)
    return render_template("adminadd.html", form=form, title='addalumni')











@app.route('/adminlogin/<int:userid>', methods=['GET', 'POST'])
def adminlogin(userid):
    user = Person.query.get_or_404(userid)
    login_user(user)
    return redirect(url_for("main"))
    


@app.route('/allclients', methods=['GET', 'POST'])
@login_required
def allclients():
    if current_user.role == 'admin':
        # users = Person.query.order_by(Person.id.desc()).all()
        users = Person.query.filter_by(role="client").order_by(Person.id.desc()).all()
        # staff = User.query.order_by(User.id.desc()).all()
        print(users)
    else:
        # flash("youre not allowed to see this")
        return redirect (url_for("main"))
    return render_template('allclient.html',users=users)


@app.route('/allstaff', methods=['GET', 'POST'])
@login_required
def allstaff():
    if current_user.role == 'admin':
        users = User.query.order_by(User.id.desc()).all()
        # staff = User.query.order_by(User.id.desc()).all()
        print(users)
    else:
        flash("youre not allowed to see this")
        return redirect ('main')
    return render_template('allstaff.html',users=users)





@app.route('/homelook', methods=['GET', 'POST'])
@login_required
def homelook():
    form=WaitForm()
    if form.validate_on_submit():
        wait=Waitlist(
            email=form.email.data
            )
        db.session.add(wait)
        db.session.commit()
        send_email()
        print(form.email.data)
       
        flash("Invitation Sent to" + ' ' + wait.email)
        return redirect('homelook')
    
    print(form.errors)
    
    if current_user.role == 'admin':
        total_claims=Cisl.query.count()
    else:
        total_claims=Cisl.query.filter_by(clientid=str(current_user.id)).count()
    
    
    if current_user.role == 'admin':
        total_client=User.query.count()
    else:
        total_client=User.query.filter_by(clientid=str(current_user.id)).count()
    

    #Hospital Module
    if current_user.role == 'admin':
        total_medicals=Hospital.query.count()
    else:
        total_medicals=Hospital.query.filter_by(id=str(current_user.id)).count()
    
    
    
    medical_client=Groups.query.count()
    medical_staff=Item.query.count()
    
    current_hour = datetime.now().hour
    greeting = ""
    
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    
    # all_product= User.query.count()
    current_time = datetime.now()
    low_quantity_flash = session.pop('low_quantity_flash', None)
    
    total_students = User.query.count()
    total_getfundstudents = Getfunds.query.count()
    total_Faq = Faq.query.count()
    total_challenges = Challenge.query.count()
    total_message = Committee.query.count()
    users_with_positions = db.session.query(User.fullname, User.position).filter(User.position.isnot(None)).all()
    total_people_with_positions = db.session.query(User).filter(User.position != '').count()
    # total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()
    message = Message.query.count()
    print(users_with_positions)
    user =Committee.query.order_by(Committee.id.desc()).all()
    # total_male = User.query.filter_by(gender='Male').count()
    # total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    challenges=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    online =Person.query.order_by(Person.id.desc()).all()
    print(current_user)
    # flash(f"There was a problem", 'success')
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('homelook.html', title='dashboard',user=user,
                           medical_client=medical_client, 
               total_medicals=total_medicals,total_client=total_client,  total_claims=total_claims,    current_time=current_time,   low_quantity_flash=low_quantity_flash, greeting=greeting, 
                 medical_staff=medical_staff,    form=form, total_challenges=total_challenges,total_message=total_message,online=online,message=message,total_Faq=total_Faq, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_students=total_students,users_with_positions=users_with_positions, total_getfundstudents=total_getfundstudents,challenges=challenges)



def get_initials(name):
    # Get the initials of each word in the name
    return ''.join([word[0].upper() for word in name.split()])


@app.route('/app', methods=['GET', 'POST'])
def approute():
    total_students = User.query.count()
    total_getfundstudents = Getfunds.query.count()
    total_message = Committee.query.count()
    total_challenges = Challenges.query.count()
    users_with_positions = db.session.query(User.fullname, User.position).filter(User.position.isnot(None)).all()
    total_people_with_positions = db.session.query(User).filter(User.position != '').count()
    # total_people_with_positions = db.session.query(User).filter(User.position.isnot(None)).count()
    message = Message.query.count()
    print(users_with_positions)
    # total_male = User.query.filter_by(gender='Male').count()
    # total_female = User.query.filter_by(gender='Female').count() 
    users=User.query.order_by(User.id.desc()).all()
    challenges=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    total_leaders = Leaders.query.count()
    print(total_leaders)
    online =Person.query.order_by(Person.id.desc()).all()
    print(current_user)
    # flash(f"There was a problem", 'success')
    if current_user == None:
        flash("Welcome to the Dashboard" + current_user.email, "Success")
        flash(f"There was a problem")
    return render_template('app.html', title='dashboard',online=online,total_message=total_message,message=message,total_challenges=total_challenges, total_leaders=total_leaders,total_people_with_positions=total_people_with_positions, users=users, total_students=total_students,users_with_positions=users_with_positions, total_getfundstudents=total_getfundstudents,challenges=challenges)


@app.route('/newpage', methods=['GET', 'POST'])
def newpage():
    return render_template("newpage.html")

@app.route('/userview', methods=['GET', 'POST'])
def userview():   
    return render_template("userview.html")


@app.route('/newdash', methods=['GET', 'POST'])
def newdash():   
    return render_template("newdash.html")




@app.route('/instock', methods=['GET', 'POST'])
def instock():  
    users=Item.query.order_by(Item.id.desc()).all()
    instock = Item.query.count()
    return render_template("instock.html",users=users,instock = instock)

@app.route('/sms', methods=['GET', 'POST'])
def sms():   
    return render_template("sms.html")


@app.route('/choose', methods=['GET', 'POST'])
def choose():   
    return render_template("choose.html")

@app.route('/message', methods=['GET', 'POST'])
def message():
    form=MessageForm()
    if form.validate_on_submit():
        new=Message(message=form.message.data
                    )
        db.session.add(new)
        db.session.commit()
        flash("Thanks for Sending to Anonymous")
        return redirect("/")
    return render_template('message.html', form=form)






@app.route('/album', methods=['GET', 'POST'])
def album():   
    form=Adduser()
    if form.validate_on_submit():
  
            new=User(fullname=form.fullname.data,
                    ministry=form.ministry.data,
                   email=form.email.data,  
                   gender=form.gender.data,  
                   program=form.program.data,  
                   telephone=form.telephone.data,      
               image_file=form.image_file.data
                  )
       
            db.session.add(new)
            db.session.commit()
            flash("New Person added", "success")
            return redirect('main')
    print(form.errors)
    return render_template("album.html", form=form, title='addalumni')



@app.route('/users_by_position')
def users_by_position():
    users_with_positions = db.session.query(User.fullname, User.position).order_by(User.position.desc()).all()
    print(users_with_positions)
    return render_template('position.html', users_with_positions=users_with_positions)


# catergory by ministry
@app.route('/media', methods=['GET', 'POST'])
@login_required
def media():
    media = User.query.filter_by(ministry='CADET CORPS').all()
    return render_template('media.html', media=media)

def load_data():
    data = []
    with open('data.csv', 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip header row
            index, name, hall = line.strip().split(',')
            data.append({'index': index, 'name': name, 'hall': hall})
    return data


@app.route('/praise', methods=['GET', 'POST'])
def praise():
    index = request.form['index']
    data = load_data()
    
    # Find the user by index
    user = next((item for item in data if item['index'] == index), None)

    if user:
        return render_template('results.html', user=user)
    else:
        return render_template('not_found.html')
    


    
    

@app.route('/ent', methods=['GET', 'POST'])
def ent():
    mcc = User.query.filter_by(ministry='ENTERTAINMENT COMMITTEE').all()
    return render_template('mcc.html', mcc=mcc)

@app.route('/cjc', methods=['GET', 'POST'])
def cjc():
    cjc = User.query.filter_by(ministry='ORGANIZING COMMITTEE').all()
    return render_template('cjc.html', cjc=cjc)

@app.route('/lg', methods=['GET', 'POST'])
@login_required
def lg():
    lg = User.query.filter_by(ministry='Levite Generation').all()
    return render_template('lg.html', lg=lg)

@app.route('/communion', methods=['GET', 'POST'])
@login_required
def communion():
    communion = User.query.filter_by(ministry='Communion').all()
    return render_template('communion.html', communion=communion)

@app.route('/protocol', methods=['GET', 'POST'])
@login_required
def protocol():
    protocol = User.query.filter_by(ministry='Protocol').all()
    return render_template('protocol.html', protocol=protocol)

@app.route('/dis', methods=['GET', 'POST'])
@login_required
def dis():
    dis = User.query.filter_by(ministry='Discipleship').all()
    return render_template('dis.html', dis=dis)

@app.route('/mission', methods=['GET', 'POST'])
def mission():
   
    return render_template('halls.html', mission=mission)

@app.route('/counselling', methods=['GET', 'POST'])
@login_required
def counselling():
    counselling = User.query.filter_by(ministry='Counselling').all()
    return render_template('counselling.html', counselling=counselling)

@app.route('/prayer', methods=['GET', 'POST'])
@login_required
def prayer():
    prayer = User.query.filter_by(ministry='Prayer Ministry').all()
    return render_template('prayer.html', prayer=prayer)

@app.route('/lords', methods=['GET', 'POST'])
@login_required
def lords():
    lords = User.query.filter_by(ministry='Lords Band').all()
    return render_template('lords.html', lords=lords)


#this is a logger for abitrack





# end of ministry

@app.route('/insurance')
def insurance():
    return render_template('insurance.html')

@app.route('/leadership')
def leadership():
    return render_template('leadership1.html')

@app.route('/reinsurance')
def reinsurance():
    return render_template('reinsurance.html')

@app.route('/products')
def products():
    return render_template('products.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/medical')
def medical():
    return render_template('medical.html')




@app.route('/male_users')
def male_users():
    # male_users = User.query.filter_by(gender='Male').all()
    return render_template('male.html', male_users=male_users)

@app.route('/newreport')
@app.route('/addschool' , methods=['GET', 'POST'])
def addschool():    
    form=AddSchool()
    schools=School.query.order_by(School.id.desc()).all()
    if form.validate_on_submit():
        centralschool= School(name=form.name.data)
        db.session.add(centralschool)
        db.session.commit()
        flash("New School Added", "success")
        return redirect('addschool')
    print(form.errors)
    return render_template('addschool.html',form=form, schools=schools)


@app.route('/adddepartment' , methods=['GET', 'POST'])
def adddepartment():    
    form=AddDepartment()
    departments=Department.query.order_by(Department.id.desc()).all()
    if form.validate_on_submit():
        centralschool= Department(name=form.name.data,school=form.school.data)
        db.session.add(centralschool)
        db.session.commit()
        flash("New School Added", "success")
        return redirect('adddepartment')
    print(form.errors)
    return render_template('adddepartment.html',form=form, departments=departments)


@app.context_processor
def base():
    form=Search()
    return dict(form=form)



# @app.route('/search', methods=[ 'POST'])
# def search():
#     form= Search()
#     if request.method == 'POST': 
#         posts =Course.query
#         if form.validate_on_submit():
#             postsearched=form.searched.data
#             posts =posts.filter(Course.name.like('%'+ postsearched + '%') )
#             posts =posts.order_by(Course.schools).all()
             
#             # posts =posts.order_by(User.position).all() 
#             flash("You searched for "+ postsearched, "success")  
#             print(posts)   
#     return render_template("search.html", form=form, searched =postsearched, posts=posts)


@app.route('/list/<int:userid>', methods=['GET', 'POST'])
@login_required
def list(userid):
    print("Fetching one")
    profile=User.query.get_or_404(userid)
    print(current_user)
    return render_template("profileid.html",current_user=current_user, profile=profile, title="list")
 
 
 
@app.route('/list', methods=['GET', 'POST'])
@login_required
def lists():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("list.html", users=users, current_user=current_user, title="list")



 
@app.route('/getlist', methods=['GET', 'POST'])
@login_required
def getlist():
    print("Fetching all")
    users=Getfunds.query.order_by(Getfunds.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("getlist.html", users=users, current_user=current_user, title="list")
 
 
 

@app.route('/leader', methods=['GET', 'POST'])
@login_required
def leader():
    print("Fetching all")
    users=Leaders.query.order_by(Leaders.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("leader.html", users=users, current_user=current_user)
 


@app.route('/logout')
@login_required
def logout():
    if current_user:
        print(current_user.email)
        logout_user()
    else:
        print("Well that didnt work")
    flash('You have been logged out.','danger')
    return redirect(url_for("login"))


@app.route('/report',methods=['GET','POST'])
@login_required
def report():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("report.html", users=users, current_user=current_user, title="report")
 
 
@app.route('/email',methods=['GET','POST'])
@login_required
def email():
    print("Fetching all")
    users=User.query.order_by(User.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("email.html", users=users, current_user=current_user, title="report")


@app.route('/challenges',methods=['GET','POST'])
@login_required
def challenges():
    print("Fetching all")
    users=Challenges.query.order_by(Challenges.id.desc()).all()
    print(users)
    print(current_user)
    return render_template("challenges.html", users=users, current_user=current_user, title="report")
 


@app.route('/allmes')
@login_required
def allmes():
    message = Message.query.count()
    print(message)
    
    users=Message.query.order_by(Message.id.desc()).all()
    return render_template('allmes.html',message=message, users=users)



@app.route('/home',methods=['GET','POST'])
def home():
    persons=Person.query.all()  
    print(persons)
    return render_template('home.html',persons=persons)


@app.route('/members')
@login_required
def members():
    persons=Person.query.all()
    return render_template('members.html', persons=persons)



#CRUD(update and delete routes)
@app.route("/update/<int:id>", methods=['POST', 'GET'])
def update(id):
    form=Addinfo()
    user=Course.query.get_or_404(id)
    if request.method== 'GET':
        form.name.data = user.name
        form.year.data =user.year
        form.schools.data =user.schools
        form.level.data =user.level
         
    if request.method== 'POST':
        new=Course(name=form.name.data,
            level=form.level.data,
            schools=form.schools.data,
            year=form.year.data
                  )
        try:    
            db.session.add(new)
            db.session.commit()
            return redirect(url_for('pascoadmin')) 
        except:
            return"errrrror"
    return render_template("leadersadd.html", form=form)
    
#delete route
@app.route("/delete/<int:id>")
def deleteme(id):
    delete=Getfunds.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('main')) 
    except: 
        return "errrrrorrr"


@app.route("/deleteme/<int:id>")
def deletelist(id):
    delete=User.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect(url_for('lists')) 
    except: 
        return "errrrrorrr"
        
    
#delete route
@app.route("/delete/<int:id>")
def delete(id):
    delete=Course.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            flash ('User deleted succesfully' , 'success')
            return redirect(url_for('pascoadmin')) 
    except: 
        return "errrrrorrr"
    

# @app.route('/login', methods=['POST','GET'])
# def login():
#     form = LoginForm()
#     print ('New User')
#     print(form.email.data)
#     print(form.password.data)
    
#     if form.validate_on_submit():
#         print("form Validated successfully")
#         user = Person.query.filter_by(email = form.email.data).first()
#         if user:
#             print("user:" + user.email + "found")
        
#         if user:
#             print(user.password)
#             if user and form.password.data == user.password:
#                 print(user.email + "validored successfully")
#             # if user == None:
#             #     flash(f"There was a problem")   
#                 login_user(user)
#                 flash (f' ' 'Good day,' + ' '+ 'Welcome to your dashboard,' + ' ' + user.name + '' )
#                 session['logged_in'] = True
                
#                 return redirect(url_for('homelook'))
#             # next = request.args.get('next')
#             else:
#                 flash (f'Wrong Password ', 's/uccess')
#         else:
#             flash("User not found", 'danger') 
#     return render_template('login.html', form=form)
 

@app.context_processor
def inject_status():
    status = 'green' if current_user.is_authenticated else 'red'
    return dict(status=status)



@app.route('/mot', methods=['POST','GET'])
def mot():
    return render_template('signup_step1.html')

    
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(email)  
        user = Person.query.filter_by(email=form.email.data).first()
        print(form.email.data) 
        print(form.password.data) 
        if user and user.password ==form.password.data:
            login_user(user)
            print ("Logged in:" + user.code + " " + user.email)
            print(form.password.data) 
            flash("Welcome to your dashboard " + " "  + user.name ,  'success')
            return redirect(url_for('homme'))
        else:
            flash(f'Incorrect details, please try again', 'danger')
             
    return render_template('login.html', form=form)
 
@app.route('/show', methods=['GET', 'POST'])
def show():
    return render_template('show.html')
    
    




@app.route('/signup', methods=['POST','GET'])
def signup():
    form = Registration()
    if form.validate_on_submit():
        
        # unique_code = str(secrets.randbelow(10**12)).zfill(12)  
        
        
        if len(str(form.code.data)) != 4:
            flash('Unique Code must be exactly 4 digits.', 'danger')
            return redirect(url_for('signup'))

        password = form.password.data
        if len(password) < 6 or not re.search("[A-Z]", password) or not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
            flash('Password must be at least 6 characters long, contain at least one uppercase letter, and include at least one symbol (!@#$%^&*(),.?":{}|<>).', 'danger')
            return redirect(url_for('signup'))
        else:
            user = Person(password=form.password.data,
                        confirm_password=form.confirm_password.data,
                        email=form.email.data,
                        code=form.code.data, 
                        phone=form.phone.data,
                        # unique_code=unique_code,
                        name=form.name.data)
            db.session.add(user)
            db.session.commit()
            send_email()
            # params = "New Account Created for " + new_user.username
            # sendtelegram(params)
            flash("We sent you a confirmation Email, kindly confirm your email.", 'success')
           
            # user = Person.query.filter_by(email = form.email.data).first()
            login_user(user, remember=True)
            return redirect (url_for('login'))
    else:
        print(form.errors)
   
            
    return render_template('signup.html', form=form)


def is_gmail_address(email):
    # Regular expression for a basic check of Gmail email address
    gmail_pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
    return re.match(gmail_pattern, email)



@app.route('/departments/<string:schoolSlug>')
@login_required
def departments(schoolSlug):
    school = School.query.filter_by(slug = schoolSlug).first()
    departments = Department.query.filter_by(school = school.slug).all() 
    print(departments)
    print(school)
    print(session['selectedYear'])
    sendtelegram(current_user.name + " selected Year: " + session['selectedYear'] + " Department " + school.name + ". Found: " + str(len(departments)) + " result(s) ")
    return render_template('userdepartment.html', items=departments, header=school.name, smalltitle="2021", name="", numberofentries="16 entries")


@app.route('/programs/<string:departmentSlug>')
@login_required
def programs(departmentSlug):
    departmentSlug = departmentSlug.lower()
    department = Department.query.filter_by(slug = departmentSlug).first()
    programs = Program.query.filter_by(department = departmentSlug).all()
    # school = department.school
    # print(school)
    print(programs)
    print(department)
    print(session['selectedYear'])
    # sendtelegram(current_user.name + " selected Year: " + session['selectedYear'] + " Department " + school.name + ". Found: " + str(len(departments)) + " result(s) ")
    return render_template('userprograms.html', items=programs, header=department.name, smalltitle="2021", name="", numberofentries="16 entries")


@app.route('/userbase', methods=['POST','GET'])
def userbase():
    print("Fetching all")
    return render_template("userbase.html")
 

@app.route('/logs', methods=['POST','GET'])
def logs():
    return render_template("logs.html")






@app.route('/category', methods=['POST','GET'])
def category():
    return render_template("category.html")
 



@app.route('/authin', methods=['POST','GET'])
def authin():
    form = Registration()
    print(form.phone.data)
    print(form.email.data)
    print(form.name.data)
    if request.method == "POST": 
        if form.validate_on_submit():
            print('Success')
            user =Person(password="central@123", email=form.email.data, phone=form.phone.data, name=form.name.data)
            db.session.add(user)
            db.session.commit()
            
            login_user(user, remember=True)
            print(current_user)
            flash("New User added", "success")
            return redirect(url_for('main'))
        else:
            print(form.errors)
            
    return render_template('authin.html', form=form)
  

@app.route('/authreg', methods=['POST','GET'])
def authreg():
    return render_template("authreg.html")
 
# app.route('/halls', methods=['GET', 'POST'])
# def halls():
#     return render_template('halls.html')


# @app.route('/results', methods=['POST'])
# def results():
#     index = request.form['index']
#     data = load_data()
    
#     # Find the user by index
#     user = next((item for item in data if item['index'] == index), None)

#     if user:
#         return render_template('results.html', user=user)
#     else:
#         return render_template('not_found.html')



#  //ussd   
    
@app.route('/ussd', methods=['GET', 'POST'])
def rancardussd():
    sessionRequest = request.json
    sessionBody = {
    "MSISDN": sessionRequest["msisdn"],
    "USERDATA": sessionRequest["data"],
    # "MSGTYPE": true,
    
    "NETWORK": sessionRequest["mobileNetwork"],
    "SESSIONID": sessionRequest["sessionId"]   
}
    print("---------REQUEST-----------")
    print(sessionRequest)
    print(sessionBody)
    print("--------------------")
    
    message="Hello, Please Enter Your Index Number.\n eg.int/20/01/3356."
    
    # if sessionRequest["message"] != '*844*138': #seconod try?
    if sessionRequest["menu"] != 0: #seconod try?
        userid = sessionRequest["message"]
        print("userid", userid)
        response= findbyid(userid)
        print("response", response)
        indexnumber = sessionRequest["message"]
        if response is not None:
            print(response)
            message = response["studentname"]
           
            hall=response["hallname"]
            response = {
                    "continueSession": False,
                    "message": "Hello" + " " + message  + "\n " + "Your Hall is" + "\n " + hall + "\n\nPowered by PrestoGhana"
                    #Gets and sets by id! 
                     
                }
            try:
                
                newstudent = StudentData( studentName= message,studentID=userid, studentnumber=sessionRequest["msisdn"]  )
                db.session.add(newstudent)
                db.session.commit()
            except Exception as e:
                print(e)
                
            
        else:
            response = {
                    "continueSession": True,
                    # "message": "Hello" + " " + indexnumber + "\n " + "You have been assigned to the following corresponding Hall: " + "\n" + "Integrity - Male." + "\n" +"Faith Hall - Female"
                    "message": "No student found with ID: " + indexnumber + " " + "\n" + "Please check and try again" + "\n\nPowered by PrestoGhana"
                    #Gets and sets by id!  
                }
    else:
        response = {
                "continueSession": True,
                "message": message
                #Gets and sets by id!  
            }
        
    return response


   
@app.route("/readcsv",)
def readcsv():
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        studentbody=[]
        for line in csv_reader:
            studentName=line["StudentName"]
            regno=line["regno"]
            gender=line["gender"]
            program=line["program"]
            level=line["LEVEL"]
            email=line["email"]
            hallname=line['hallname']
            newStudent = Studenthalls(studentName=studentName, regno=regno, gender=gender,
                                      program=program, level=level, email=email,hallname=hallname)
            
            try:
                db.session.add(newStudent)
                db.session.commit()
            except Exception as e:
                print(e)
            
            print(newStudent.id)
            print(newStudent.studentName)
            
            student={
                "studentname":studentName,
                "regno":regno,
                "gender":gender,
                "program":program,
                "level":level,
                "email":email,
                "hallname":hallname
            }
            studentbody.append(student)
            
            # write to db
            
    return studentbod
    
@app.route("/findbyid")
def findbyid(id=None):
    # print("input")
    # input=request.args.get('id')
    # convert to CAPS
    
    print(id)
    id=id.replace('/', '')
    id=id.replace(' ', '')
    student=Studenthalls.query.filter_by(regno=id.upper()).first()   
    print(student) 
    if student == None:
        return None
    student={
        "studentname":student.studentName,
        "regno":student.regno,
        "gender":student.gender,
        "program":student.program,
        "level":student.level,
        "email":student.email,
        "hallname":student.hallname
    }
  
    return student

@app.route('/updateregno', methods=['POST','GET'])
def method_name():
    # for student in Studenthalls.query.order_by(Studenthalls.id.asc()).limit(10).all():
    for student in Studenthalls.query.order_by(Studenthalls.id.asc()).all():
        print(student)
        print(student.regno)
        
        # Replace '/' with an empty string and assign it back to the 'regno' attribute
        student.regno = student.regno.replace('/', '')
        print(student.regno)

        db.session.commit()
        print(student.regno)
    return "Done"


    
    
    

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(host='0.0.0.0', port=4000, debug=True)
    
  