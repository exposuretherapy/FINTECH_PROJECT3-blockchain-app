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
    
    event Procedure (uint patient_id, uint doctor_id, uint hospital_id, uint procedure_id, string uri );
    event NewProcedure (uint Procedure_id, string name, string uri);
    event NewDoctor (uint doctor_id, string uri);
    event Death (uint patient_id, uint doctor_id, uint hospital_id, uint procedure_id, string uri);
    event NewHospital(uint hospital_id, string uri);
    event NewPatient(uint patient_id, string uri);
    // events for doctor_id, patient_id, hospital_id 
    
    //mapping
    mapping (uint => string ) Doctors;
    mapping (uint => string) Hospitals;
    mapping (uint => sting) Patients;
    //access levels 1-4
    mapping(doctor_id => uint) accessLevels;
    
    constructor(
        address payable "_Admin") private {
            Admin = _Admin;
        }
        
        
        
        function createProcedure( string memory uri) public {
            uint procedure_id,  string name 
        }
        
        function createDoctor( string memory uri) public { 
           // generate id, name, sex, licens, specialty,status
            doctor_ids.increment();
            doctor_id = doctor_ids.current();
            _setUri(doctorid.current, string memory uri);
            
            emit NewDoctor( uint doctor_id, string uri);
            
        }
        function updateDoctor( uint doctor_id,string memory uri) public {
             name, sex, licens, specialty, status
        }
        
        function createHospital ( string memory uri) public{
            //generate Id, name, address,status
            hospital_id.increment();
            hospital_id = hospital_id.current();
            _setUri( hospital_id, uri);
            
            emit NewHospital( hospital_id, uri);
            
        }
        
        function updateHospital( uint hospital_id, string memory uri) public {
            name, address, status
        }
        
        function createPatient ( string memory uri) public {
            //generate id, name, DOB, Blood type, Insurance, sex, status
            patient_id.increment();
            patient_id = patient_id.current();
            _setUri ( patient_id, uri);
            
            emit NewPatient ( patient_id, uri);
        }
        
        function doctorVisit (uint patient_id, uint doctor_id, uint hospital_id,  uint procedure_ids, string memory uri) public {
            
        }
        
        function updateInsurance (uint patient_id, string memory uri) public {
            
        }
        
        function updatePatient (uint patient_id, string memory uri) public {
            name, insurance, sex, status, blood type, DOB
        }
        
        function createERdata ( uint patient_id, string memory uri) public {
            //allergies, HRF, prescriptions, height, weight, emergency contact
            
        }
        
        function UpdateErdata (uint patient_id, string memory uri) public {
            allergies, HRF, prescriptions, height, weight
        }
        
        function CreateProcedures( string memory uri) public {
            //generate procedure id, name
            procedure_id.increment();
            procedure_id = procedure_id.current();
            _setUri(procedure_id , uri)
            
            emit NewProcedure( uint procedure_id, string uri);
            }
            
      
}