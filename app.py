from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Replace with your MySQL database credentials
db_host = "localhost"
db_user = "root"
db_password = "password"
db_name = "mydatabase"

# Function to establish a database connection
def create_connection():
    return mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    
@app.route('/')
def home_page():
    return render_template("paytm.html")

# Route for the form page
@app.route("/registration", methods=["GET", "POST"])
def form_page():
    if request.method == "POST":
        # Get form data
        firstname = request.form["firstname"]
        lastname=request.form["lastname"]
        Account_number=request.form["Accountnumber"]
        dateofbirth=request.form["dateofbirth"]
        gender = request.form["gender"]
        email = request.form["email"]
        mobile = request.form["mobileno"]
        address= request.form["address"]
        state=request.form["state"]
        city=request.form["city"]
        Branch=request.form["Branchaddress"]
        
        # Convert the 'subscribe' checkbox value to BOOLEAN (0 or 1)
        #subscribe = 1 if "subscribe" in request.form else 0

        # Insert form data into the database
        connection = create_connection()
        cursor = connection.cursor()
        sql = "INSERT INTO form_data (firstname, lastname, Account_number, dateofbirth, gender, email, mobile, address, state, city, Branch) VALUES (%s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s)"
        values = (firstname, lastname, Account_number, dateofbirth, gender, email, mobile, address, state, city ,Branch )
        cursor.execute(sql, values)
        connection.commit()
        connection.close()

        return "Form submitted successfully!"

    return render_template("registration.html")



if __name__ == "__main__":
    app.run()

