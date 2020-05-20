pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";

contract MedicalHistory {
    contract MedicalHistory is ERC721Full {
    using Counters for Counters.Counter;
    Counters.Counter patient_ids;
    address payable private Admin;
    Counters.Counter Doctor_ids;
    Counters.Counter Hospital_ids;
    Counters.Counter Procedure_ids;
    
    event Procedure (uint patient_id, uint doctor_id, uint hospital_id, uint procedure_ids, string uri );
    event NewDoctor (uint patient_id, uint doctor_id, uint hospital_id, unit procedure_ids, string uri);
    event Death (uint patient_id, uint doctor_id, uint hospital_id, uint procedure_ids, string uri);
    event NewHospital(uint hospital_id, string uri);
    event NewPatient(uint patient_id, string uri);
    // events for doctor_id, patient_id, hospital_id 
    
    constructor(
        address payable "_Admin") private {
            Admin = _Admin;
        }
        
        function createDoctor( string memory uri) public { 
            generate id, name, sex, licens, specialty,status
        }
        function updateDoctor( uint doctor_id,string memory uri) public {
             name, sex, licens, specialty, status
        }
        
        function createHospital ( string memory uri) public{
            generate Id, name, address,status
        }
        
        function updateHospital( uint hospital_id, string memory uri) public {
            name, address, status
        }
        
        function createPatient ( string memory uri) public {
            generate id, name, DOB, Blood type, Insurance, sex, status
        }
        
        function doctorVisit (uint patient_id, uint doctor_id, uint hospital_id,  uint procedure_ids, string memory uri) public {
            
        }
        
        function updateInsurance (uint patient_id, string memory uri) public {
            
        }
        
        function updatePatient (uint patient_id, string memory uri) public {
            name, insurance, sex, status, blood type, DOB
        }
        
        function createERdata ( uint patient_id, string memory uri) public {
            allergies, HRF, prescriptions, height, weight
        }
        
        function UpdateErdata (uint patient_id, string memory uri) public {
            allergies, HRF, prescriptions, height, weight
        }
        
        function registerProcedures( string memory uri) public {
            generate procedure id, name
        }
            
        //emits are within a function
        emit 
        emit CheckUp
        emit Death
}