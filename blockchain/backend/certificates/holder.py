class CertificateHolder:

    def __init__(self):
        self.certificates = []

    # -----------------------------
    # Store issued certificate locally
    # -----------------------------
    def store_certificate(self, issued_data: dict):
        self.certificates.append(issued_data)

    # -----------------------------
    # Get certificate for verification
    # -----------------------------
    def get_certificate(self, index: int):
        if index >= len(self.certificates):
            raise Exception("Certificate not found")

        cert = self.certificates[index]

        return {
            "cid": cert["cid"],
            "proof": cert["merkle_proof"],
            "index": cert["index"]
        }
