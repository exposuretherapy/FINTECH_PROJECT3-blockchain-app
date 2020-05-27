from main import convertDataToJSON, pinJSONtoIPFS, initContract, w3
import sys
from pprint import pprint
import requests as r
import ipfshttpclient

medicalhistory = initContract()

def createPatient():
    time = input("Date of Birth"), input("Time of Birth")
    description = {"Patient Name :":input("Patient Name"),
                    "Patient Gender :": input("Patient Gender"),
                    "Doctor Name :": input("Doctor Name"),
                    "Hospital Name :": input("Hospital Name")}

    json_data = convertDataToJSON(time, description)
    uri = pinJSONtoIPFS(json_data)

    tx_hash=medicalhistory.functions.createPatient(uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    return uri, receipt

def getPatientData(patient_id):
    uri=medicalhistory.functions.getPatientData(patient_id).call()
    return uri

def get_uri(uri):
    client = ipfshttpclient.connect('/dns/ipfs.io/tcp/443/https')
    return client.cat(uri.split('/')[-1])

#def getAccidentReports(token_id):
#    accident_filter = medicalhistory.events.Accident.createFilter(
#        fromBlock='0x0', 
#        argument_filters = {"token_id":token_id}
#    )
#    return accident_filter.get_all_entries()

def get_all_patient_ids():
    event_filter = medicalhistory.events.newPatient.createFilter(
        fromBlock='0x0'
        )
    events = event_filter.get_all_entries()
    return _extract_arg_from_event(events, 'patient_id')

def _extract_arg_from_event(events, arg):
    return [event['args'][arg] for event in events]

if __name__ == "__main__":
    if sys.argv[1] == 'report':
 
        uri, receipt = createPatient()
        print("Report IPFS Hash", uri)

    elif sys.argv[1] == 'get':

       pprint(get_all_patient_ids())

       patient_id = int(input('patient_id'))
       uri = getPatientData(patient_id)
       
       print(get_uri(uri))

