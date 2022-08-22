from flask import Flask, request, render_template, flash
from blockchain import BlockChain

app = Flask(__name__)
app.secret_key = "password"
bc = BlockChain()

@app.route('/', methods=["GET", "POST"])
def home():
    if(request.method == "POST"):
        data = request.form['data_input']
        bc.mine_block(data=data)
        data=''
    is_chain_valid = bc.validate_chain()
    if is_chain_valid:
        validity_status = 'The chain is VALID'
    else:
        validity_status = 'The chain is INVALID'
    return render_template('home.html', blockchain=bc.blockchain, validity_status=validity_status)


if __name__ == "__main__":
    app.run(debug=True)