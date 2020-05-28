from main import convertDataToJSON, pinJSONtoIPFS, initContract, w3
import sys
from pprint import pprint
import requests as r
import ipfshttpclient

medicalhistory = initContract()

def createProcedure():
    # time = input("Date of Birth"), input("Time of Birth")
    description = {"Procedure Name :":input("Procedure Name"),
                    "Procedure Description :": input("Procuedure Description")}

    json_data = convertDataToJSON(time, description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createProcedure(uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getProcedurData(procedure_id):
    uri=medicalhistory.functions.getProcedureData(procedure_id).call()
    return uri

def get_uri(uri):
    client = ipfshttpclient.connect('/dns/ipfs.io/tcp/443/https')
    return client.cat(uri.split('/')[-1])

def get_all_procedure_ids():
    event_filter = medicalhistory.events.newProcedure.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'procedure_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

if __name__ == "__main__":
    if sys.argv[1] == 'report':
 
        uri, receipt = createProcedure()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'get':

       pprint(get_all_procedure_ids())

       procedure_id = int(input('procedure_id'))
       uri = getProcedureData(procedure_id)
       
       print(get_uri(uri))

# Doctor
def createDoctor():
    # time = input("Date of Birth"), input("Time of Birth")
    description = {"Doctor Name :":input("Doctor Name"),
                    "Doctor Gender :": input("Doctor Gender"),
                    "Hospital Name :": input("Hospital Name")}

    json_data = convertDataToJSON(time, description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createDoctor(uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getDoctorData(doctor_id):
    uri=medicalhistory.functions.getDoctorData(doctor_id).call()
    return uri

def get_uri(uri):
    client = ipfshttpclient.connect('/dns/ipfs.io/tcp/443/https')
    return client.cat(uri.split('/')[-1])

def get_all_Doctor_ids():
    event_filter = medicalhistory.events.newDoctor.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'doctor_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

if __name__ == "__main__":
    if sys.argv[1] == 'report':
 
        uri, receipt = createDoctor()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'get':

       pprint(get_all_Doctor_ids())

       patient_id = int(input('patient_id'))
       uri = getDoctorData(doctor_id)
       
       print(get_uri(uri))


# Hospital
def createHospital():
    # time = input("Date of Birth"), input("Time of Birth")
    description = {"Hospital Name :":input("Hospital Name"),
                    "State :": input("State"),
                    "City :": input("City")}

    json_data = convertDataToJSON(time, description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createHospital(uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getHospitalData(doctor_id):
    uri=medicalhistory.functions.getHospitalData(hospital_id).call()
    return uri

def get_uri(uri):
    client = ipfshttpclient.connect('/dns/ipfs.io/tcp/443/https')
    return client.cat(uri.split('/')[-1])

def get_all_Hospital_ids():
    event_filter = medicalhistory.events.newHospital.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'doctor_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

if __name__ == "__main__":
    if sys.argv[1] == 'report':
 
        uri, receipt = createHospital()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'get':

       pprint(get_all_Hospital_ids())

       hospital_id = int(input('hospital_id'))
       uri = getHospitalData(hospital_id)
       
       print(get_uri(uri))



# Patients
def createPatient():
    # time = input("Date of Birth"), input("Time of Birth")
    description = {"Hospital Name :":input("Hospital Name"),
                    "State :": input("State"),
                    "City :": input("City")}

    json_data = convertDataToJSON(time, description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createHospital(uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getHospitalData(doctor_id):
    uri=medicalhistory.functions.getHospitalData(hospital_id).call()
    return uri

def get_uri(uri):
    client = ipfshttpclient.connect('/dns/ipfs.io/tcp/443/https')
    return client.cat(uri.split('/')[-1])

def get_all_Hospital_ids():
    event_filter = medicalhistory.events.newHospital.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'doctor_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

if __name__ == "__main__":
    if sys.argv[1] == 'report':
 
        uri, receipt = createHospital()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'get':

       pprint(get_all_Hospital_ids())

       hospital_id = int(input('hospital_id'))
       uri = getHospitalData(hospital_id)
       
       print(get_uri(uri))


# DoctorVisit
def createDoctorVisit():
    # time = input("Date of Birth"), input("Time of Birth")
    description = {"Date :":input("Date"),
                    "Reason for visit :": input("Reason for visit"),
                    "Assessment :": input("Assessment")
                    "Notes :": input("Notes") }

    json_data = convertDataToJSON(time, description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createDoctorVisit(uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getDoctorVisitData(doctorVisit_id):
    uri=medicalhistory.functions.getDoctorVisitData(doctorVisit_id).call()
    return uri

def get_uri(uri):
    client = ipfshttpclient.connect('/dns/ipfs.io/tcp/443/https')
    return client.cat(uri.split('/')[-1])

def get_all_doctorVisit_ids():
    event_filter = medicalhistory.events.newDoctorVisit.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'doctorVisit_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

if __name__ == "__main__":
    if sys.argv[1] == 'report':
 
        uri, receipt = createDoctorVisit()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'get':

       pprint(get_all_doctorVisit_ids())

       doctorVisit_id = int(input('doctorVisit_id'))
       uri = getdoctorVisitData(doctorVisit_id)
       
       print(get_uri(uri))


