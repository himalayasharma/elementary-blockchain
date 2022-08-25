import numpy as np
from flask import Flask, request, render_template
from blockchain import BlockChain

# Create app
app = Flask(__name__)
# Specify secret key (optional)
app.secret_key = "password"
# Instantiate blockchain
bc = BlockChain()

def get_validity_status(blockchain):
    is_chain_valid, error = blockchain.validate_chain()
    if is_chain_valid:
        validity_status = f'The chain is VALID. {error["reason"]}'
    else:
        validity_status = f'The chain is INVALID. {error["reason"]}'
    return validity_status

# Base url for app is '/'
@app.route('/', methods=["GET", "POST"])
def home():
    # `request_type` tells about the request made by MODIFY BLOCK
    # By default it is set ""
    request_type = ""
    if(request.method == "POST"):
        # CASE 1: MINE BLOCK
        if(request.form["action"] == "Create block"):
            data = request.form['data_input']
            bc.mine_block(data=data)
        # CASE 2: MODIFY BLOCK
        elif(request.form["action"] == "Update block"):
            index = request.form['index_input']
            # INVALID REQUEST - if index is not a digit
            if index.isnumeric() == False:
                request_type = f"Invalid request! Please enter a number and try again. Valid indices are: {np.arange(2, len(bc.blockchain)+1)}"
            # if index is a digit
            else:
                # VALID REQUEST - if index > 1 and < length of blockchain
                # Cast index str into int
                index = int(request.form['index_input'])
                # Modify data in block with required index
                if(index>1 and index<=len(bc.blockchain)):
                    modified_data = request.form['modified_data_input']
                    bc.blockchain[index-1]["data"] = modified_data
                # INVALID REQUEST - genesis block i.e. the first block created in the blockchain by default is immutable
                elif(index == 1):
                    request_type = f"Invalid request! Genesis block cannot be altered. Try again with some other index. Valid indices are: {np.arange(2, len(bc.blockchain)+1)}"
                # INVALID REQUEST - index specified is more than length of the chain
                else:
                    request_type = f"Invalid request! Valid indices are: {np.arange(2, len(bc.blockchain)+1)}"        
        # CASE 3: RESET BLOCKCHAIN
        else:
            bc.blockchain = BlockChain().blockchain

    return render_template('home.html', blockchain=bc.blockchain, validity_status=get_validity_status(bc), request_type=request_type)


if __name__ == "__main__":
    app.run(debug=True)