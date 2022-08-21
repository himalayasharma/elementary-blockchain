from flask import Flask, render_template, request
from blockchain import BlockChain

app = Flask(__name__)

bc = BlockChain()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view_blockchain', methods=["GET"])
def view_blockchain():
    return render_template("view_blockchain.html", entries=bc.blockchain)

@app.route('/mine_block', methods=["GET", "POST"])
def mine_block():
    if(request.method == "POST"):
        data = request.form
        bc.mine_block(data.to_dict()["data"])
    return render_template("mine_block.html")

@app.route('/validate_blockchain', methods=["GET"])
def validate_blockchain():
    if bc.validate_chain() == True:
        validity_statement = "The chain in VALID"
    else:
        validity_statement = "The chain is INVALID"
    return render_template("validate_blockchain.html", entries=validity_statement)

if __name__ == "__main__":
    app.run(debug=True)