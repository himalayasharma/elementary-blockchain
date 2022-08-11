import datetime

class BlockChain:

    def __init__(self) -> None:
        self.blockchain = []
        pass
        
    def create_block(self, index:int, data:str, proof:int, prev_hash:str) -> dict:
        pass

    def mine_block(self, data:str) -> dict:
        pass