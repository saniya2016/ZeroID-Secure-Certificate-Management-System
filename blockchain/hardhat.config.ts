import { HardhatUserConfig } from "hardhat/config";
import "@nomiclabs/hardhat-ethers";
import * as dotenv from "dotenv";

dotenv.config();

const config: HardhatUserConfig = {
  solidity: "0.8.20",
  networks: {
    sepolia: {
      url: process.env.SEPOLIA_RPC_URL!,
      accounts: [process.env.PRIVATE_KEY!],
    },
  },
};

export default config;

// await contract.registerDID(
// ...   "did:zeroid:galgotia",
// ...   0x4d014C6deB9F9c9E12F05B20a4680B3A4cF0Fa80
// ... );