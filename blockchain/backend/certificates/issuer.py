from datetime import datetime
from backend.merkle.merkle_tree import sha256
from backend.ipfs.ipfs_service import upload_json_to_ipfs
from backend.blockchain.blockchain_service import BlockchainService


class CertificateIssuer:

    def __init__(self, merkle_tree):
        self.tree = merkle_tree
        self.blockchain = BlockchainService()

    # -----------------------------
    # ISSUE CERTIFICATE
    # -----------------------------
    def issue_certificate(self, student_name, course, university, issuer_did):

        issuer_address = self.blockchain.resolve_did(issuer_did)

        if issuer_address == "0x0000000000000000000000000000000000000000":
            raise Exception("Issuer DID not registered")

        certificate = {
            "issuer_did": issuer_did,
            "student_name": student_name,
            "course": course,
            "university": university,
            "issued_at": datetime.utcnow().isoformat()
        }

        cid = upload_json_to_ipfs(certificate)

        leaf_hash = sha256(cid)

        self.tree.leaves.append(leaf_hash)
        self.tree.build_tree()

        index = len(self.tree.leaves) - 1
        proof = self.tree.get_proof(index)
        root = self.tree.get_root()

        tx_hash = self.blockchain.update_root_on_chain("0x" + root)

        return {
            "cid": cid,
            "certificate": certificate,
            "merkle_proof": proof,
            "index": index,
            "root": root,
            "tx_hash": tx_hash
        }

    # -----------------------------
    # REVOKE CERTIFICATE
    # -----------------------------
    def revoke_certificate(self, cid):

        leaf_hash = sha256(cid)

        removed = self.tree.remove_leaf(leaf_hash)

        if not removed:
            raise Exception("Certificate not found in Merkle tree")

        if self.tree.get_root():
            new_root = self.tree.get_root()
        else:
            new_root = "0" * 64

        tx_hash = self.blockchain.update_root_on_chain("0x" + new_root)

        return {
            "revoked_cid": cid,
            "new_root": new_root,
            "tx_hash": tx_hash
        }