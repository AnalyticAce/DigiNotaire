pragma solidity ^0.8.0;

contract DigitalNotary {
    mapping(string => bool) private documents;

    function notarizeDocument(string memory documentHash) public {
        documents[documentHash] = true;
    }

    function isDocumentNotarized(string memory documentHash) public view returns (bool) {
        return documents[documentHash];
    }
}

