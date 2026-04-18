from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arushi100@",
    database="login_system"
)

cursor = db.cursor()

@app.route('/', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        confirm = request.form['confirm_password']

        if password != confirm:
            return "Passwords do not match"

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()

        if user:
            if user[2] == password:
                return redirect(url_for('home'))
            else:
                return "Wrong Password"
        else:
            cursor.execute(
                "INSERT INTO users (email,password) VALUES (%s,%s)",
                (email,password)
            )
            db.commit()

            return redirect(url_for('home'))

    return render_template("login.html")


@app.route('/home')
def home():
    return render_template("home.html")

# --- ADD THESE NEW ROUTES ---

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/treatment')
def treatment():
    return render_template("treatment.html")

@app.route('/doctor')
def doctor():
    return render_template("doctor.html")

@app.route('/testimonial')
def testimonial():
    return render_template("testimonial.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

# ----------------------------

if __name__ == "__main__":
    app.run(debug=True)