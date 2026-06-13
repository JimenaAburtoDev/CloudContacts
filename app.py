from flask import Flask, render_template, request, redirect, flash
from database import get_connection

app = Flask(__name__)
app.secret_key = "cloudcontacts"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():

    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    try:

        conn = get_connection()

        with conn.cursor() as cursor:

            sql = """
            INSERT INTO contacts(fullname,email,phone)
            VALUES(%s,%s,%s)
            """

            cursor.execute(
                sql,
                (fullname,email,phone)
            )

        conn.commit()
        conn.close()

        flash("Contacto registrado correctamente")

    except Exception as e:

        flash(f"Error: {str(e)}")

    return redirect("/")

@app.route("/contacts")
def contacts():

    conn = get_connection()

    with conn.cursor() as cursor:

        cursor.execute("""
        SELECT *
        FROM contacts
        ORDER BY created_at DESC
        """)

        contacts = cursor.fetchall()

    conn.close()

    return render_template(
        "contacts.html",
        contacts=contacts
    )

if __name__ == "__main__":
    app.run(debug=True)