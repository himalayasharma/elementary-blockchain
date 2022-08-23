import datetime
import json
import hashlib

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
        prev_block = self.blockchain[-1]
        prev_proof = prev_block["proof"]
        new_index = prev_block["index"]+1
        new_data = data
        new_proof = self._calculate_proof(
            index=new_index,
            prev_proof=prev_proof,
            data=new_data
        )
        prev_hash = self._get_hash(prev_block)

        new_block = {
            "index":new_index,
            "timestamp":str(datetime.datetime.now()),
            "proof":new_proof,
            "data":new_data,
            "prev_hash":prev_hash
        }
        
        self.blockchain.append(new_block)

    def _calculate_proof(self, index:int, prev_proof:int, data:str):
        new_proof = 1
        check_proof = False

        while not check_proof:
            to_digest = self._to_digest(
                index=index,
                data=data,
                prev_proof=prev_proof,
                new_proof=new_proof
            )

            hash = hashlib.sha256(to_digest).hexdigest()
            if(hash[:4] == "0000"):
                check_proof = True
            else:
                new_proof += 1
        return new_proof
    
    def _to_digest(self, index:int, data:str, prev_proof:int, new_proof:int) -> bytes:
        to_digest = str(prev_proof**3 + new_proof**2 + index) + data
        return to_digest.encode()

    def _get_hash(self, block:dict) -> str:
        json_str = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(json_str).hexdigest()

    def validate_chain(self) -> bool:
        
        current_idx = 0

        while(current_idx < len(self.blockchain)-1):
            
            next_idx = current_idx+1
            current_block = self.blockchain[current_idx]
            next_block = self.blockchain[next_idx]

            current_block_hash = self._get_hash(current_block)
            print(current_idx, next_idx)
            print(current_block_hash, next_block["prev_hash"])
            if(current_block_hash != next_block["prev_hash"]):
                error = {
                    'error_code':1,
                    'reason':f"Mismatch between hash value of block at index {current_idx} & previous hash value stored in the next block at index {next_idx}."
                }
                return False, error

            to_digest = self._to_digest(
                index=next_block["index"],
                data=next_block["data"],
                prev_proof=current_block["proof"],
                new_proof=next_block["proof"]
            )

            hash = hashlib.sha256(to_digest).hexdigest()
            if(hash[:4] != "0000"):
                error = {
                    'error_code':2,
                    'reason':f"Hash value of block at index {next_idx} does not have first 4 hex digits as '0000'."
                }
                return False, error
            current_idx += 1

        error = {
            'error_code':0,
            'reason':"Hash values for all blocks are okay."
        }
        return True, error


def main():
    pass

if __name__ == "__main__":
    main()