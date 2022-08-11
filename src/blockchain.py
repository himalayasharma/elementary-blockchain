import datetime

class BlockChain:

    def __init__(self) -> None:
        self.blockchain = []
        genesis_block = self.create_block(
            index=1,
            data="Genesis block",
            proof=1,
            prev_hash="0"
        )
        self.blockchain.append(genesis_block)
        
    def create_block(self, index:int, data:str, proof:int, prev_hash:str) -> dict:
        block = {
            "index":index,
            "timestamp":str(datetime.datetime.now()),
            "proof":proof,
            "data":data,
            "prev_hash":prev_hash
        }
        return block

    def mine_block(self, data:str) -> dict:
        new_index = self.blockchain[-1]["index"]+1
        new_data = data
        new_proof = None
        prev_hash = None

        new_block = {
            "index":new_index,
            "timestamp":str(datetime.datetime.now()),
            "proof":new_proof,
            "data":new_data,
            "prev_hash":prev_hash
        }
        
        self.blockchain.append(new_block)
