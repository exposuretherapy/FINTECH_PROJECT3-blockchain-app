from main import convertDataToJSON, pinJSONtoIPFS, initContract, w3
import sys
from pprint import pprint

medicalhistory = initContract()

def createPatient():
    time = input("Date of Birth"), input("Time of Birth")
    description = {"Patient Name :":input("Patient Name"),
                    "Patient Gender :": input("Patient Gender"),
                    "Doctor Name :": input("Doctor Name"),
                    "Hospital Name :": input("Hospital Name")}
    patient_id = int(input("patient_id"))

    json_data = convertDataToJSON(time, description)
    uri = pinJSONtoIPFS(json_data)

    return patient_id, uri

def reportBirth(patient_id, uri):
    tx_hash=medicalhistory.functions.reportBirth(patient_id,uri).transact(
        {"from":w3.eth.accounts[0]}
    )

    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

#def getAccidentReports(token_id):
#    accident_filter = medicalhistory.events.Accident.createFilter(
#        fromBlock='0x0', 
#        argument_filters = {"token_id":token_id}
#    )
#    return accident_filter.get_all_entries()

if __name__ == "__main__":
    if sys.argv[1] == 'report':
        patient_id, uri = createPatient()

        receipt = reportBirth(
            patient_id,
            uri)

        pprint(dict(receipt))
        print("Report IPFS Hash", uri)

#    elif sys.argv[1] == 'get':
#        token_id = int(sys.argv[2])
#        car = medicalhistory.functions.cars(token_id).call()
#        reports = getAccidentReports(token_id)
#
#        pprint(reports)
#        print("VIN", car[0], "has been in", car[1], "accidents.")
