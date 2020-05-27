pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";

//contract MedicalHistory {
//    contract MedicalHistory is ERC721Full {
contract MedicalHistory is ERC721Full {
    constructor() ERC721Full("MedicalHistory", "MDH") public{}
    
// COUNTERS
    using Counters for Counters.Counter;
    Counters.Counter patient_ids;
    Counters.Counter doctor_ids;
    Counters.Counter hospital_ids;
    Counters.Counter procedure_ids;
//    address payable private Admin;
    
// EVENTS
    event procedure (uint patient_id, uint doctor_id, uint hospital_id, uint procedure_id, string uri );
    event newProcedure (uint Procedure_id, string name, string uri);
    event newDoctor (uint doctor_id, string uri);
    event death (uint patient_id, uint doctor_id, uint hospital_id, uint procedure_id, string uri);
    event newPatient(uint patient_id, string uri);
    event newHospital(uint hospital_id, string uri);
    
// MAPPING
    mapping (uint => string) Doctors;
    mapping (uint => string) Hospitals;
    mapping (uint => string) Patients;

    
// CREATE AND GETTER FUNCTIONS
    //DOCTOR
    function createDoctor(string memory uri) public returns(uint) { 
       // generate id, name, sex, licens, specialty,status
        doctor_ids.increment();
        uint doctor_id = doctor_ids.current();
        Doctors[doctor_id] = uri;
        emit newDoctor(doctor_id, uri);
    }
    
    function getDoctorData(uint doctor_id) public view returns(string memory){
        return Doctors[doctor_id];
    }
    
    //HOSPITALS    
    function createHospital ( string memory uri) public returns(uint) {
        //generate Id, name, address,status
        hospital_ids.increment();
        uint hospital_id = hospital_ids.current();
        Hospitals[hospital_id] = uri;
        emit newHospital(hospital_id, uri);
    }
    
    function getHospitalData(uint hospital_id) public view returns(string memory){
        return Hospitals[hospital_id];
    }
    
    //PATIENTS    
    function createPatient ( string memory uri) public returns(uint) {
        //generate id, name, DOB, Blood type, Insurance, sex, status
        patient_ids.increment();
        uint patient_id = patient_ids.current();
        Patients[patient_id] = uri;
        emit newPatient (patient_id, uri);
    }
    
    function getPatientData(uint patient_id) public view returns(string memory){
        return Patients[patient_id];
    }
        

    //PROCEDURES
    function createProcedures( string memory uri) public returns(uint) {
    //generate procedure id, name
    procedure_ids.increment();
    uint procedure_id = procedure_ids.current();
    _setTokenURI (procedure_id, uri);
    string memory procedureName;
    
    emit newProcedure(procedure_id, procedureName, uri);
    }
}



//FUNCTIONS WE'RE WORKING ON OR DISCARDING


// function updateInsurance (uint patient_id, string memory uri) public returns(uint) {
    
// }
       
       
    // function doctorVisit (uint patient_id, uint doctor_id, uint hospital_id,  uint procedure_id, string memory uri) public {
        
    // }
    
    // function updatePatient (uint patient_id, string memory uri) public returns(uint) {
    //         name; insurance; sex; status, blood type, DOB
    // }
        
//         function createERdata ( uint patient_id, string memory uri) public returns(uint) {
//             //allergies, HRF, prescriptions, height, weight, emergency contact
            
//         }
        
//         function UpdateErdata (uint patient_id, string memory uri) public returns(uint) {
//  //           allergies, HRF, prescriptions, height, weight
//         }

//         function updateHospital( uint hospital_id, string memory uri) public returns(uint) {
// //            name; address; status;
//         }
        
// function createProcedure(string memory uri) public returns(uint) {
//   uint procedure_id;  
//   string memory name; 
// }
     
     
    // function updateDoctor( uint doctor_id,string memory uri) public returns(uint) {
    //     // name, sex, licens, specialty, status
    // }    
