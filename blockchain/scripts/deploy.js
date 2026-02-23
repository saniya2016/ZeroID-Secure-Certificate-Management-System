const hre = require("hardhat");

async function main() {

  // -----------------------------
  // 1️⃣ Deploy ZeroIDMerkle
  // -----------------------------

  const initialRoot =
    "0x0000000000000000000000000000000000000000000000000000000000000000";

  const ZeroIDMerkle = await hre.ethers.getContractFactory("ZeroIDMerkle");
  const merkleContract = await ZeroIDMerkle.deploy(initialRoot);
  await merkleContract.deployed();

  console.log("✅ ZeroIDMerkle Deployed!");
  console.log("📍 Merkle Contract Address:", merkleContract.address);


  // -----------------------------
  // 2️⃣ Deploy DIDRegistry
  // -----------------------------

  const DIDRegistry = await hre.ethers.getContractFactory("DIDRegistry");
  const didRegistry = await DIDRegistry.deploy();
  await didRegistry.deployed();

  console.log("✅ DIDRegistry Deployed!");
  console.log("📍 DID Registry Address:", didRegistry.address);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});