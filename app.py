from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def submit():
    email = request.form["email"]
    password = request.form["password"]
    print("Phishing Data Captured:")
    print("Email:", email)
    print("Password:", password)
    return '''
        <h2>This was a phishing simulation!</h2>
        <p>Never share your passwords on suspicious sites. Always verify the sender and URL.</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
