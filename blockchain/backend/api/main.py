from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from backend.merkle.merkle_tree import MerkleTree
from backend.certificates.issuer import CertificateIssuer
from backend.certificates.verifier import CertificateVerifier

app = FastAPI(title="ZeroID Backend")

# -----------------------------------
# GLOBAL Merkle Tree (in-memory)
# -----------------------------------
tree = MerkleTree([])

issuer = CertificateIssuer(tree)
verifier = CertificateVerifier(tree)


# -----------------------------------
# Request Models
# -----------------------------------

class IssueRequest(BaseModel):
    issuer_did: str
    student_name: str
    course: str
    university: str


class VerifyRequest(BaseModel):
    cid: str
    proof: List[str]
    index: int


class RevokeRequest(BaseModel):
    cid: str


# -----------------------------------
# Issue Certificate
# -----------------------------------

@app.post("/issue-certificate")
def issue_certificate(req: IssueRequest):

    return issuer.issue_certificate(
        student_name=req.student_name,
        course=req.course,
        university=req.university,
        issuer_did=req.issuer_did
    )


# -----------------------------------
# Verify Certificate
# -----------------------------------

@app.post("/verify-certificate")
def verify_certificate(req: VerifyRequest):

    return verifier.verify_certificate(
        cid=req.cid,
        proof=req.proof,
        index=req.index
    )


# -----------------------------------
# 🔴 Revoke Certificate
# -----------------------------------

@app.post("/revoke-certificate")
def revoke_certificate(req: RevokeRequest):

    return issuer.revoke_certificate(
        cid=req.cid
    )