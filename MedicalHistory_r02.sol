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
    Counters.Counter doctorVisit_ids;
//    address payable private Admin;
    
// EVENTS
    event newDoctorVisit (uint visitTime, uint doctorVisit_id, uint patient_id, uint doctor_id, uint hospital_id, uint procedure_id, string uri );
    event newProcedure (uint procedure_id, string name, string uri);
    event newDoctor (uint doctor_id, string uri);
    // event death (uint patient_id, uint doctor_id, uint hospital_id, uint procedure_id, string uri);
    event newPatient(uint patient_id, string uri);
    event newHospital(uint hospital_id, string uri);
    
// MAPPING
    mapping (uint => string) Doctors;
    mapping (uint => string) Hospitals;
    mapping (uint => string) Patients;
    mapping (uint => string) Procedures;
    mapping (uint => string) DoctorVisits;
    // mapping (uint => string) Deaths;

    
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
    function createHospital (string memory uri) public returns(uint) {
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
    function createPatient (string memory uri) public returns(uint) {
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
    function createProcedures(string memory name, string memory uri) public returns(uint) {
        //generate procedure id, name
        procedure_ids.increment();
        uint procedure_id = procedure_ids.current();
        Procedures[procedure_id] = uri;
        emit newProcedure (procedure_id, name, uri);
    }        
    function getProcedures(uint procedure_id) public view returns (string memory){
        return Procedures[procedure_id];
    }
    
    // DOCTORVISITS
    function createnewDoctorVisit(uint patient_id, uint doctor_id, uint hospital_id, uint procedure_id, string memory uri) public returns(uint) {
        doctorVisit_ids.increment();
        uint doctorVisit_id = doctorVisit_ids.current();
        DoctorVisits[doctorVisit_id] = uri;
        uint visitTime = now;
        emit newDoctorVisit(visitTime, doctorVisit_id, patient_id, doctor_id, hospital_id, procedure_id, uri);
    }

    function getnewDoctorVisit(uint doctorVisit_id) public view returns (string memory){
        return DoctorVisits[doctorVisit_id];
    }
}

