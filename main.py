# main.py

from flask import Flask, request, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# =========================
# DATABASE CONFIG
# =========================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# =========================
# MAIL CONFIG
# =========================

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True

# CHANGE THIS
app.config['MAIL_USERNAME'] = 'hacktechspy1@gmail.com'

# CHANGE THIS TO YOUR GMAIL APP PASSWORD
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

# =========================
# DATABASE MODEL
# =========================

class Case(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100))

    message = db.Column(db.Text)

# CREATE DATABASE
with app.app_context():
    db.create_all()

# =========================
# HTML PAGE
# =========================

html_page = """

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>HackTech Blockchain Investigations</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
        }

        body{
            font-family:Arial, sans-serif;
            background:#0f172a;
            color:white;
        }

        nav{
            display:flex;
            justify-content:space-between;
            align-items:center;
            padding:20px 60px;
            background:#020617;
            position:sticky;
            top:0;
            z-index:1000;
        }

        nav h2{
            color:#22c55e;
        }

        nav a{
            color:white;
            text-decoration:none;
            margin-left:20px;
        }

        nav a:hover{
            color:#22c55e;
        }

        .hero{
            height:90vh;
            display:flex;
            justify-content:center;
            align-items:center;
            text-align:center;
            padding:40px;
            background:linear-gradient(to right,#0f172a,#1e293b);
        }

        .hero-content{
            max-width:800px;
        }

        .hero h1{
            font-size:60px;
            margin-bottom:20px;
            color:#22c55e;
        }

        .hero p{
            font-size:20px;
            line-height:1.7;
            margin-bottom:30px;
        }

        .hero button{
            padding:15px 30px;
            border:none;
            background:#22c55e;
            color:white;
            font-size:18px;
            border-radius:5px;
            cursor:pointer;
        }

        .hero button:hover{
            background:#16a34a;
        }

        .services{
            padding:80px 50px;
            text-align:center;
        }

        .services h2{
            font-size:40px;
            margin-bottom:50px;
            color:#22c55e;
        }

        .service-boxes{
            display:flex;
            justify-content:center;
            flex-wrap:wrap;
            gap:30px;
        }

        .box{
            background:#1e293b;
            padding:30px;
            width:300px;
            border-radius:10px;
            transition:0.3s;
        }

        .box:hover{
            transform:translateY(-10px);
        }

        .box h3{
            margin-bottom:15px;
            color:#22c55e;
        }

        .contact{
            padding:80px 20px;
            text-align:center;
            background:#020617;
        }

        .contact h2{
            margin-bottom:30px;
            color:#22c55e;
        }

        form{
            max-width:500px;
            margin:auto;
        }

        input, textarea{
            width:100%;
            padding:15px;
            margin:10px 0;
            border:none;
            border-radius:5px;
        }

        textarea{
            height:150px;
        }

        button{
            padding:15px 30px;
            background:#22c55e;
            color:white;
            border:none;
            border-radius:5px;
            cursor:pointer;
        }

        button:hover{
            background:#16a34a;
        }

        .warning{
            color:#f87171;
            margin-top:20px;
            line-height:1.6;
        }

        footer{
            text-align:center;
            padding:20px;
            background:#0f172a;
        }

        @media(max-width:768px){

            nav{
                flex-direction:column;
            }

            .hero h1{
                font-size:40px;
            }

            .service-boxes{
                flex-direction:column;
                align-items:center;
            }

        }

    </style>

</head>

<body>

    <nav>

        <h2>HackTech Investigations</h2>

        <div>
            <a href="#">Home</a>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
        </div>

    </nav>

    <section class="hero">

        <div class="hero-content">

            <h1>Blockchain Investigation & Asset Tracing</h1>

            <p>
                We assist clients with blockchain transaction analysis,
                scam investigations, wallet tracing, and digital asset
                consultation services.
            </p>

            <a href="#contact">
                <button>
                    Start Consultation
                </button>
            </a>

        </div>

    </section>

    <section class="services" id="services">

        <h2>Our Services</h2>

        <div class="service-boxes">

            <div class="box">

                <h3>Blockchain Analysis</h3>

                <p>
                    Investigating wallet activity and transaction history
                    across public blockchain networks.
                </p>

            </div>

            <div class="box">

                <h3>Scam Investigation</h3>

                <p>
                    Assisting victims in documenting suspicious activity
                    and organizing evidence for reporting purposes.
                </p>

            </div>

            <div class="box">

                <h3>Consultation</h3>

                <p>
                    Professional guidance regarding digital asset
                    investigations and security awareness.
                </p>

            </div>

        </div>

    </section>

    <section class="contact" id="contact">

        <h2>Submit Your Case</h2>

        <form action="/send" method="POST">

            <input
                type="text"
                name="name"
                placeholder="Your Name"
                required
            >

            <input
                type="email"
                name="email"
                placeholder="Your Email"
                required
            >

            <textarea
                name="message"
                placeholder="Describe your issue..."
                required
            ></textarea>

            <button type="submit">
                Submit Case
            </button>

        </form>

        <p class="warning">    
            Services are limited to investigation, tracing, documentation, recovery of funds/asset
            and consultation support.
        </p>

        <p style="margin-top:20px;">
            Contact: hacktechspy1@gmail.com
        </p>

    </section>

    <footer>
        © 2026 HackTech Blockchain Investigations
    </footer>

</body>
</html>

"""

# =========================
# HOME ROUTE
# =========================

@app.route('/')
def home():

    return render_template_string(html_page)

# =========================
# SEND FORM
# =========================

@app.route('/send', methods=['POST'])
def send():

    name = request.form['name']

    email = request.form['email']

    message = request.form['message']

    # SAVE TO DATABASE
    new_case = Case(
        name=name,
        email=email,
        message=message
    )

    db.session.add(new_case)

    db.session.commit()

    # SEND EMAIL
    msg = Message(
        subject=f"New Consultation Request From {name}",
        sender=app.config['MAIL_USERNAME'],
        recipients=[app.config['MAIL_USERNAME']]
    )

    msg.body = f"""

New Consultation Request

Name: {name}

Email: {email}

Message:
{message}

"""

    try:
        mail.send(msg)

    except Exception as e:
        print(e)

    return """

    <body style='
        background:#0f172a;
        color:white;
        text-align:center;
        font-family:Arial;
        padding-top:100px;
    '>

        <h1>
            Consultation Submitted Successfully
        </h1>

        <p>
            We will review your request and contact you shortly.
        </p>

        <br>

        <a href='/'
           style='
                color:#22c55e;
                text-decoration:none;
                font-size:20px;
           '>

            Return Home

        </a>

    </body>

    """

# =========================
# RUN APP
# =========================

if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))

    app.run(
        host='0.0.0.0',
        port=port,
        debug=False
    )

