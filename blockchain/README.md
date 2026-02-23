# 🔐 ZeroID – Secure Certificate Management System

ZeroID is a blockchain-powered certificate issuance and verification platform that ensures tamper-proof academic credentials using:

- 📦 IPFS (Decentralized Storage)
- 🌳 Merkle Tree (Batch Integrity)
- ⛓ Ethereum (Sepolia Testnet)
- 🆔 DID Registry (Issuer Identity Verification)
- ⚛ React Frontend
- 🚀 FastAPI Backend

---

# 📚 Project Overview

ZeroID allows:

👩‍💼 University Admin to:
- Issue digital certificates
- Verify certificates
- Revoke certificates
- View DID registry

👨‍🎓 Students to:
- View their certificates
- See status (Valid / Revoked)
- Confirm digital authenticity

🌍 Public Users to:
- Verify certificate authenticity using CID

All certificates are:
- Stored on IPFS
- Hashed into a Merkle Tree
- Root stored on Ethereum (Sepolia)
- Cryptographically verifiable

---

# 🏗 Architecture

Frontend (React)
        ↓
FastAPI Backend
        ↓
IPFS (Pinata)
        ↓
Merkle Tree (Python)
        ↓
Ethereum Smart Contracts (Sepolia)

---

# 💻 SYSTEM REQUIREMENTS (Windows)

Install the following:

## 1️⃣ Python 3.11+
Download:
https://www.python.org/downloads/

During installation:
✔ Add Python to PATH

Verify:
```bash
python --version
```

---

## 2️⃣ Node.js (LTS)
Download:
https://nodejs.org/

Verify:
```bash
node -v
npm -v
```

---

## 3️⃣ Git
Download:
https://git-scm.com/downloads

Verify:
```bash
git --version
```

---

# 🚀 PROJECT SETUP

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ZeroID-Secure-Certificate-Management-System.git
cd ZeroID-Secure-Certificate-Management-System/blockchain
```

---

# 🔑 ENVIRONMENT VARIABLES

Create a `.env` file inside:

```
blockchain/backend/blockchain/
```

Add:

```
SEPOLIA_PRIVATE_KEY=YOUR_PRIVATE_KEY
SEPOLIA_RPC_URL=YOUR_ALCHEMY_RPC
```

⚠ Do NOT share private key publicly.

---

# 📦 BACKEND SETUP

Navigate:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn web3 requests python-dotenv
```

Start backend:

```bash
uvicorn api.main:app --reload
```

Open Swagger:

```
http://127.0.0.1:8000/docs
```

---

# ⛓ SMART CONTRACT DEPLOYMENT (If Needed)

Go to root blockchain folder:

```bash
cd ..
npm install
npx hardhat compile
npx hardhat run scripts/deploy.js --network sepolia
```

---

# ⚛ FRONTEND SETUP

Navigate:

```bash
cd frontend
npm install
npm run dev
```

Open:

```
http://localhost:5173
```

---

# 🧪 HOW TO DEMONSTRATE TO PROFESSOR

## 1️⃣ Issue Certificate
- Go to Issue Certificate
- Enter:
  - issuer_did
  - student_name
  - course
  - university
- Submit

Shows:
- CID
- Merkle proof
- Root
- Blockchain tx hash

---

## 2️⃣ Verify Certificate
- Copy CID
- Paste into Verify page
- Shows:
  ✅ Digitally Verified (Green Tick)
  OR
  ❌ Revoked

---

## 3️⃣ Revoke Certificate
- Enter CID
- Submit
- New Merkle root pushed on-chain

Verify again → Status becomes REVOKED

---

# 🔍 Blockchain Verification

Go to:
https://sepolia.etherscan.io/

Paste transaction hash to show:
- Root update
- On-chain proof

---

# 🔐 Security Model

- Certificates immutable (IPFS CID)
- Integrity guaranteed via Merkle Tree
- Root anchored on Ethereum
- Revocation updates root
- DID ensures trusted issuers

---

# 📌 Features Implemented

✔ Certificate Issuance  
✔ On-chain Merkle Root Storage  
✔ Certificate Verification  
✔ Revocation Mechanism  
✔ DID Registry  
✔ React UI  
✔ Role-based access  

---

# 🎓 Academic Relevance

ZeroID demonstrates:

- Blockchain for credential security
- Decentralized storage
- Cryptographic verification
- Smart contract integration
- Real-world revocation logic

---

# 👩‍💻 Developed By

Saniya Mhatre  
ZeroID – 2026

---

# 📄 License

Academic Project – Educational Use
