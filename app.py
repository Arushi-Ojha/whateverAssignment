from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
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


if __name__ == "__main__":
    app.run(debug=True)