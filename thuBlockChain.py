from time import time
import json
import hashlib
from uuid import uuid4
from textwrap import dedent

from flask import Flask, request
from flask.json import jsonify
from urllib.parse import urlparse



class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()

        #create the genesis block
        self.new_block(previous_hash=1, proof=100)
    

    def new_block(self, proof , previous_hash=None):
        #create new block and adds it to the chain
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }
        #reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block
        

    def new_transaction(self, sender, recipient, amount):
        #adds new transaction to the list of transations
        '''
        creates a new transaction to go into the next mined block
        the return <int> the index of the block that will hold this transaction
        '''
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        #create a SHA-256 hash a block
        blockString = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(blockString).hexdigest()

    @property
    def last_block(self):
        #returns the last block in the chain
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        '''
        simple proof of work algorithm:
        find a  number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        p is the previous proof, and p' is the new proof
        param last_proof: <int>
        '''
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof
    
    @staticmethod
    def valid_proof(last_proof, proof):
        '''
        validates the proof: dows hash(last_proof, proof) contain 4 leading zeroes?
        param: <int> proof and last proof
        return boolean True if correct, False if not
        '''
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def register_node(self, address):
        ''' add new node to the list of nodes.
        param: <str> address of node http://192.3.45.0:5000
        return none
        '''
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)




'''our blockchain as an API
create three methods:
    /mine               to tell our server to mine a new block
    /transactions/new   to create a new transaction to a block
    /chain               to return the full blockchain
'''

app = Flask(__name__)

#generate a globally unique address for this node
node_identifier = str(uuid4()).replace("-","")

#instantiate the blockchain
blockchain = BlockChain()
'''
calculate the proof of wook
reward the miner 1 coin
forge the new block by adding it to the chain
'''
@app.route('/mine', methods=['GET'])
def mine():
    #run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    #we must receive a reward for finding the proof
    #the sender is "0" to signify that this node has mined a new coin
    blockchain.new_transaction(sender="0", recipient=node_identifier, amount=1)

    #forge the new block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    response = {
        'message': "New block forge",
        'index': block['index'],
        'transaction': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=["POST"])
def new_transaction():
    values = request.get_json()

    #check that the required fields are in the post'ed data
    required = ['sender', 'recipient', 'amount']
    if not all (k in values for k in required):
        return 'Missing values', 400
    
    #create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    response = {'message': f'Transaction will be added to Block {index}'}

    return jsonify(response), 201

@app.route("/chain", methods=["GET"])
def full_chain():
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain)
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
