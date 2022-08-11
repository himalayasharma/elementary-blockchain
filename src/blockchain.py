import datetime
from venv import create

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
        pass