from web3 import Web3
import os
from dotenv import load_dotenv
from pathlib import Path

# Load root .env
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)


class BlockchainService:

    def __init__(self):

        self.w3 = Web3(Web3.HTTPProvider(os.getenv("SEPOLIA_RPC_URL")))

        if not self.w3.is_connected():
            raise Exception("Failed to connect to Sepolia RPC")

        self.private_key = os.getenv("PRIVATE_KEY")

        if not self.private_key:
            raise Exception("PRIVATE_KEY not found in .env")

        self.account = self.w3.eth.account.from_key(self.private_key)

        # -------------------------
        # ZeroID Merkle Contract
        # -------------------------
        self.merkle_contract_address = Web3.to_checksum_address(
            "0xe1F7728A4D735C76d868E798ea109733a3D96316"
        )

        self.merkle_abi = [
            {
                "inputs": [{"internalType": "bytes32", "name": "_newRoot", "type": "bytes32"}],
                "name": "updateMerkleRoot",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "inputs": [],
                "name": "merkleRoot",
                "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
                "stateMutability": "view",
                "type": "function",
            },
            {
                "inputs": [
                    {"internalType": "bytes32[]", "name": "proof", "type": "bytes32[]"},
                    {"internalType": "bytes32", "name": "leaf", "type": "bytes32"},
                ],
                "name": "verifyProof",
                "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
                "stateMutability": "view",
                "type": "function",
            },
        ]

        self.merkle_contract = self.w3.eth.contract(
            address=self.merkle_contract_address,
            abi=self.merkle_abi
        )

        # -------------------------
        # DID Registry Contract
        # -------------------------
        self.did_contract_address = Web3.to_checksum_address(
            "0xA95b1C2623f2e7564a35E7726330f3BF5C9C8851"
        )

        self.did_abi = [
            {
                "inputs": [{"internalType": "string", "name": "_did", "type": "string"}],
                "name": "getPublicKey",
                "outputs": [{"internalType": "address", "name": "", "type": "address"}],
                "stateMutability": "view",
                "type": "function",
            }
        ]

        self.did_contract = self.w3.eth.contract(
            address=self.did_contract_address,
            abi=self.did_abi
        )

    # --------------------------------
    # Update Merkle Root On Chain
    # --------------------------------
    def update_root_on_chain(self, new_root_hex: str):

        nonce = self.w3.eth.get_transaction_count(self.account.address)

        txn = self.merkle_contract.functions.updateMerkleRoot(
            Web3.to_bytes(hexstr=new_root_hex)
        ).build_transaction({
            "from": self.account.address,
            "nonce": nonce,
            "gas": 200000,
            "gasPrice": self.w3.eth.gas_price
        })

        signed_txn = self.w3.eth.account.sign_transaction(txn, self.private_key)

        tx_hash = self.w3.eth.send_raw_transaction(signed_txn.raw_transaction)

        return self.w3.to_hex(tx_hash)

    # --------------------------------
    # Get On-Chain Merkle Root
    # --------------------------------
    def get_onchain_root(self):
        return self.merkle_contract.functions.merkleRoot().call()

    # --------------------------------
    # Verify Proof On-Chain
    # --------------------------------
    def verify_onchain(self, proof: list, leaf_hex: str):

        proof_bytes = [Web3.to_bytes(hexstr="0x" + p) for p in proof]
        leaf_bytes = Web3.to_bytes(hexstr=leaf_hex)

        return self.merkle_contract.functions.verifyProof(
            proof_bytes,
            leaf_bytes
        ).call()

    # --------------------------------
    # Resolve DID
    # --------------------------------
    def resolve_did(self, did: str):
        return self.did_contract.functions.getPublicKey(did).call()