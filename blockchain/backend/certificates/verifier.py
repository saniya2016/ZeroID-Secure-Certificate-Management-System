import requests
from backend.merkle.merkle_tree import sha256
from backend.blockchain.blockchain_service import BlockchainService


class CertificateVerifier:

    def __init__(self, merkle_tree):
        self.tree = merkle_tree
        self.blockchain = BlockchainService()

    # -----------------------------
    # Fetch certificate from IPFS
    # -----------------------------
    def fetch_certificate(self, cid: str):
        url = f"https://gateway.pinata.cloud/ipfs/{cid}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Unable to fetch certificate from IPFS")

        return response.json()

    # -----------------------------
    # Verify Certificate (ON-CHAIN)
    # -----------------------------
    def verify_certificate(self, cid: str, proof: list, index: int):

        certificate = self.fetch_certificate(cid)

        # Validate issuer DID exists
        issuer_did = certificate.get("issuer_did")
        issuer_address = self.blockchain.resolve_did(issuer_did)

        if issuer_address == "0x0000000000000000000000000000000000000000":
            return {
                "status": "INVALID - Unknown Issuer",
                "certificate": certificate
            }

        # Recompute leaf hash
        leaf_hash = sha256(cid)

        # Verify proof on-chain
        is_valid = self.blockchain.verify_onchain(
            proof,
            "0x" + leaf_hash
        )

        # Get on-chain root
        onchain_root = self.blockchain.get_onchain_root()

        return {
            "status": "VALID" if is_valid else "REVOKED",
            "onchain_root": onchain_root.hex(),
            "certificate": certificate
        }