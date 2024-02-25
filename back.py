from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

contract_address = "" #CONTRACT_ADDRESS
contract_abi = "" #CONTRACT_ABI

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def notarize_document(document_hash):
    tx_hash = contract.functions.notarizeDocument(document_hash).transact()
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

def is_document_notarized(document_hash):
    return contract.functions.isDocumentNotarized(document_hash).call()

document_hash = "" #HASH_OF_YOUR_DOCUMENT
notarize_document(document_hash)
print(is_document_notarized(document_hash))
