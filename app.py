from flask import Flask, request, render_template, flash
from blockchain import BlockChain

app = Flask(__name__)
bc = BlockChain()

@app.route('/', methods=["GET", "POST"])
def home():
    if(request.method == "POST"):
        data = request.form['data_input']
        bc.mine_block(data=data)
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)