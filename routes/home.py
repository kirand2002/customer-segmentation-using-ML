from python.config import app
import simplejson as json
from flask import Flask, request, render_template,session,redirect,url_for
import os
import sqlite3 as sql
from werkzeug.utils import secure_filename
import numpy as np



@app.route('/')
def index():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template("aboutus.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    msg = None
    if (request.method == "POST"):
        if (request.form["uname"] != "" and request.form["uphone"] != "" and request.form["username"] != "" and
                request.form["upassword"] != ""):
            uname = request.form["uname"]
            uphone = request.form["uphone"]
            username = request.form["username"]
            password = request.form["upassword"]

            with sql.connect("soilerosion.db") as con:
                c = con.cursor()
                c.execute(
                    "INSERT INTO  signup VALUES('" + uname + "','" + uphone + "','" + username + "','" + password + "')")
                msg = "Your account is created"

                con.commit()
        else:
            msg = "Something went wrong"

    return render_template("signup.html", msg=msg)


@app.route('/userlogin')
def userlogin():
    return render_template("userlogin.html")


@app.route('/userloginNext', methods=['GET', 'POST'])
def userloginNext():
    msg = None
    if (request.method == "POST"):
        username = request.form['username']

        upassword = request.form['upassword']

        with sql.connect("soilerosion.db") as con:
            c = con.cursor()
            c.execute(
                "SELECT username,upassword  FROM signup WHERE username = '" + username + "' and upassword ='" + upassword + "'")
            r = c.fetchall()
            for i in r:
                if (username == i[0] and upassword == i[1]):
                    session["logedin"] = True
                    session["fusername"] = username
                    return redirect(url_for("userhome"))
                else:
                    msg = "please enter valid username and password"

    return render_template("userlogin.html", msg=msg)


@app.route('/adminlogin')
def adminlogin():
    return render_template("adminlogin.html")


@app.route('/adminloginNext', methods=['GET', 'POST'])
def adminloginNext():
    msg = None
    if (request.method == "POST"):
        ausername = request.form['ausername']

        apassword = request.form['apassword']

        with sql.connect("soilerosion.db") as con:
            c = con.cursor()
            c.execute(
                "SELECT ausername,apassword  FROM adminlogin WHERE ausername = '" + ausername + "' and apassword ='" + apassword + "'")
            r = c.fetchall()
            for i in r:
                if (ausername == i[0] and apassword == i[1]):
                    session["logedin"] = True
                    session["fusername"] = ausername
                    return redirect(url_for("adminhome"))
                else:
                    msg = "please enter valid username and password"

    return render_template("adminlogin.html", msg=msg)


# usercode
@app.route('/userhome')
def userhome():
    return render_template("userhome.html")


@app.route('/usergallery')
def usergallery():
    return render_template("gallery.html")


@app.route("/addfaq", methods=["GET", "POST"])
def addfaq():
    msg = None
    if (request.method == "POST"):
        if (request.form["question"] != "" and request.form["answer"] != ""):
            question = request.form["question"]
            answer = request.form["answer"]

            with sql.connect("soilerosion.db") as con:
                c = con.cursor()
                c.execute("INSERT INTO  faq VALUES('" + question + "','" + answer + "')")
                msg = "Your Query saved successfully "

                con.commit()
        else:
            msg = "Something went wrong"

    return render_template("adminaddfaq.html", msg=msg)


@app.route('/userlogout')
def userlogout():
    # Remove the session variable if present
    session.clear()
    return redirect(url_for('index'))


# admin base
@app.route('/adminhome')
def adminhome():
    return render_template("adminhome.html")


@app.route('/viewusers')
def viewusers():
    con = sql.connect("soilerosion.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select uname,uphone,username from signup")
    rows = cur.fetchall()
    print(rows)
    return render_template("adminviewusers.html", rows=rows)


@app.route('/viewqueries')
def viewqueries():
    con = sql.connect("soilerosion.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select question,answer from faq")
    rows = cur.fetchall()
    print(rows)
    return render_template("userviewfaq.html", rows=rows)


@app.route('/adminviewqueries')
def adminviewqueries():
    con = sql.connect("soilerosion.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select question,answer from faq")
    rows = cur.fetchall()
    print(rows)
    return render_template("adminviewfaq.html", rows=rows)


@app.route('/adminlogout')
def adminlogout():
    # Remove the session variable if present
    session.clear()
    return redirect(url_for('index'))


@app.route('/segmentation')
def predict():
    return render_template('segmentation.html')


