pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";

contract MedicalHistory {
    contract MedicalHistory is ERC721Full {
    using Counters for Counters.Counter;
    Counters.Counter patient_ids;
    // create an admin wallet so only we are able to change data.
    address payable private Admin;
    Counters.Counter Doctor_ids;
    Counters.Counter Hospital_ids;
    Counters.Counter Procedure_ids;

    //create events that will be stored in coressponding URI's
    
    event New Data (uint patient_id, uint doctor_id, uint hospital_id, uint procedure_ids, string uri );
}