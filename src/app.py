from flask import Flask, render_template, request
from blockchain import BlockChain

app = Flask(__name__)

bc = BlockChain()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view_blockchain', methods=["GET"])
def view_blockchain():
    return render_template("view_blockchain.html")

@app.route('/mine_block', methods=["GET", "POST"])
def mine_block():
    if(request.method == "POST"):
        print(request.form)
    return render_template("mine_block.html")

@app.route('/validate_blockchain', methods=["GET"])
def validate_blockchain():
    return render_template("validate_blockchain.html")

if __name__ == "__main__":
    app.run(debug=True)