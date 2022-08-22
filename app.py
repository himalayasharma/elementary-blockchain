from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if(request.method == "POST"):
        pass
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)