from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/mypage/me")
def me():
    return render_template("aboutme.html")


@app.route("/mypage/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == "POST":
        print(request.form)
        return redirect("/mypage/contact")
        