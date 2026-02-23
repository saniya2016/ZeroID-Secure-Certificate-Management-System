// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract DIDRegistry {

    struct DID {
        address owner;
        string publicKey;
        bool exists;
    }

    mapping(string => DID) private dids;

    event DIDRegistered(string did, address owner);
    event DIDUpdated(string did);

    function registerDID(string memory _did, string memory _publicKey) public {
        require(!dids[_did].exists, "DID already registered");

        dids[_did] = DID({
            owner: msg.sender,
            publicKey: _publicKey,
            exists: true
        });

        emit DIDRegistered(_did, msg.sender);
    }

    function updatePublicKey(string memory _did, string memory _newKey) public {
        require(dids[_did].exists, "DID not found");
        require(dids[_did].owner == msg.sender, "Not DID owner");

        dids[_did].publicKey = _newKey;

        emit DIDUpdated(_did);
    }

    function getPublicKey(string memory _did)
        public
        view
        returns (string memory)
    {
        require(dids[_did].exists, "DID not found");
        return dids[_did].publicKey;
    }
}