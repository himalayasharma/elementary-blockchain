from flask import Flask, request, render_template, flash
from blockchain import BlockChain

app = Flask(__name__)
app.secret_key = "password"
bc = BlockChain()

def get_validity_status(blockchain):
    is_chain_valid, error = blockchain.validate_chain()
    if is_chain_valid:
        validity_status = f'The chain is VALID. {error["reason"]}'
    else:
        validity_status = f'The chain is INVALID. {error["reason"]}'
    return validity_status

@app.route('/', methods=["GET", "POST"])
def home():
    request_type = ""
    if(request.method == "POST"):
        if(request.form["action"] == "Create block"):
            # Mine block
            data = request.form['data_input']
            bc.mine_block(data=data)
        elif(request.form["action"] == "Update block"):
            # Modify block
            index = int(request.form['index_input'])
            if(index>1 and index<=len(bc.blockchain)):
                modified_data = request.form['modified_data_input']
                bc.blockchain[index-1]["data"] = modified_data
                request_type = "Request is okay"
            elif(index == 1):
                request_type = "Invalid request! Genesis block cannot be altered. Try again with some other index!"
            else:
                request_type = f"Invalid request. Enter index only between 2 and current length of chain i.e. {len(bc.blockchain)}. Try again!"        
        else:
            # Reset blockchain
            bc.blockchain = BlockChain().blockchain

    return render_template('home.html', blockchain=bc.blockchain, validity_status=get_validity_status(bc), request_type=request_type)


if __name__ == "__main__":
    app.run(debug=True)