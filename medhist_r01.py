from main import convertDataToJSON, pinJSONtoIPFS, initContract, w3
import sys
from pprint import pprint
import requests as r
import ipfshttpclient

medicalhistory = initContract()

##################################################
## DOCTOR
def createDoctor():
    description = {
        "Date & Time :":[input("Date"), input("Time")],
        "Doctor Name :":input("Doctor Name"),
        "Doctor Gender :": input("Doctor Gender"),
        "Hospital Name :": input("Hospital Name")
        }

    json_data = convertDataToJSON(description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createDoctor(uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getDoctorData(doctor_id):
    uri=medicalhistory.functions.getDoctorData(doctor_id).call()
    return uri.split('/')[-1]

def get_uri(uri):
    return r.get(f"https://ipfs.io/ipfs/{uri}").json()

def get_all_doctor_ids():
    event_filter = medicalhistory.events.newDoctor.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'doctor_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

##################################################
# HOSPITAL
def createHospital():
    description = {
        "Date & Time :":[input("Date"), input("Time")],
        "Hospital Name :":input("Hospital Name"),
        "State :": input("State"),
        "City :": input("City")
        }

    json_data = convertDataToJSON(description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createHospital(uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getHospitalData(hospital_id):
    uri=medicalhistory.functions.getHospitalData(hospital_id).call()
    return uri.split('/')[-1]

def get_uri(uri):
    return r.get(f"https://ipfs.io/ipfs/{uri}").json()

def get_all_hospital_ids():
    event_filter = medicalhistory.events.newHospital.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'hospital_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

##################################################
#PATIENT
def createPatient():
    description = {
        "Date & Time :":[input("Date"), input("Time")],
        "Patient Name :":input("Patient Name"),
        "Patient Gender :": input("Patient Gender"),
        "Doctor Name :": input("Doctor Name"),
        "Hospital Name :": input("Hospital Name")
        }

    json_data = convertDataToJSON(description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createPatient(uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getPatientData(patient_id):
    uri=medicalhistory.functions.getPatientData(patient_id).call()
    return uri.split('/')[-1]

def get_uri(uri):
    return r.get(f"https://ipfs.io/ipfs/{uri}").json()

def get_all_patient_ids():
    event_filter = medicalhistory.events.newPatient.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'patient_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

################################################
## PROCEDURE
def createProcedures():
    
    description = {
        "Date & Time :":[input("Date"), input("Time")],
        "Procedure Name :":input("Procedure Name"),
        "Procedure Description :": input("Procuedure Description")
        }

    json_data = convertDataToJSON(description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createProcedures(description["Procedure Name :"],uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getProcedures(procedure_id):
    uri=medicalhistory.functions.getProcedures(procedure_id).call()
    return uri.split('/')[-1]

def get_uri(uri):
    return r.get(f"https://ipfs.io/ipfs/{uri}").json()

def get_all_procedure_ids():
    event_filter = medicalhistory.events.newProcedure.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'procedure_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

###############################################
#DOCTOR VISIT
def newDoctorVisit():
    pprint(f"Patient IDs: {get_all_patient_ids()}")
    pprint(f"Doctor IDs: {get_all_doctor_ids()}")
    pprint(f"Hospital IDs: {get_all_hospital_ids()}")
    pprint(f"Procedure IDs: {get_all_procedure_ids()}")
    description = {
        "Patient ID :": int(input("Patient ID")),
        "Doctor ID :": int(input("Doctor ID")),
        "Hospital ID :": int(input("Hospital ID")),
        "Procedure ID :": int(input("Procedure ID")),
        "Date & Time :":[input("Date"), input("Time")],
        "Reason for visit :": input("Reason for visit"),
        "Assessment :": input("Assessment"),
        "Notes :": input("Notes")
        }

    json_data = convertDataToJSON(description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createnewDoctorVisit(
        int(description['Patient ID :']), 
        int(description['Doctor ID :']), 
        int(description['Hospital ID :']),
        int(description['Procedure ID :']), 
        uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getDoctorVisitData(doctorVisit_id):
    uri=medicalhistory.functions.getnewDoctorVisit(doctorVisit_id).call()
    return uri.split('/')[-1]

def get_uri(uri):
    return r.get(f"https://ipfs.io/ipfs/{uri}").json()

def get_all_doctorVisit_ids():
    event_filter = medicalhistory.events.newDoctorVisit.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'doctorVisit_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

###########################################
###########################################
# MAIN CALLOUT
if __name__ == "__main__":

#DOCTOR
    if sys.argv[1] == 'reportDoctor':
 
        uri, receipt = createDoctor()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'getDoctor':

       pprint(get_all_doctor_ids())

       doctor_id = int(input('doctor_id'))
       uri = getDoctorData(doctor_id)

       data = get_uri(uri)

       print (f"Doctor's name: {data['Doctor Name :']}.")
       print (f"Doctor's gender: {data['Doctor Gender :']}.")
       print (f"Doctor's Associated Hospital: {data['Hospital Name :']}.")

#HOSPITAL
    elif sys.argv[1] == 'reportHospital':
 
        uri, receipt = createHospital()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'getHospital':

       pprint(get_all_hospital_ids())

       hospital_id = int(input('hospital_id'))
       uri = getHospitalData(hospital_id)

       data = get_uri(uri)

       print (f"Input date : {data['Date & Time :'][0]}.")
       print (f"Input time : {data['Date & Time :'][1]}.")
       print (f"Hospital name: {data['Hospital Name :']}.")
       print (f"Hospital Location: {data['City :']}, {data['State :']}.")
       
#PATIENT
    elif sys.argv[1] == 'reportPatient':
 
        uri, receipt = createPatient()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'getPatient':

       pprint(get_all_patient_ids())

       patient_id = int(input('patient_id'))
       uri = getPatientData(patient_id)

       data = get_uri(uri)

       print (f"Input date : {data['Date & Time :'][0]}.")
       print (f"Input time : {data['Date & Time :'][1]}.")
       print (f"Patient's name: {data['Patient Name :']}.")
       print (f"Patient's gender: {data['Patient Gender :']}.")
       print (f"Doctor's name: {data['Doctor Name :']}.")
       print (f"Hospital name: {data['Hospital Name :']}.")

#PROCEDURE
    elif sys.argv[1] == 'reportProcedure':
 
        uri, receipt = createProcedures()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'getProcedure':

       pprint(get_all_procedure_ids())

       procedure_id = int(input('procedure_id'))
       uri = getProcedures(procedure_id)

       data = get_uri(uri)

       print (f"Input date : {data['Date & Time :'][0]}.")
       print (f"Input time : {data['Date & Time :'][1]}.")
       print (f"Procedure name: {data['Procedure Name :']}.")
       print (f"Procedure description: {data['Procedure Description :']}.")

#DOCTOR VISIT
    elif sys.argv[1] == 'reportVisit':

        uri, receipt = newDoctorVisit()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'getVisit':

       pprint(get_all_doctorVisit_ids())

       doctorVisit_id = int(input('doctorVisit_id'))
       uri = getDoctorVisitData(doctorVisit_id)

       data = get_uri(uri)

       print (f"Input date : {data['Date & Time :'][0]}.")
       print (f"Input time : {data['Date & Time :'][1]}.")
       print (f"Reason for visit: {data['Reason for visit :']}.")
       print (f"Assessment: {data['Assessment :']}.")
       print (f"Notes: {data['Notes :']}.")
       