import json
import os
import requests
from pathlib import Path
from web3.auto import w3
from dotenv import load_dotenv

load_dotenv()

print('crypto.py',__name__)

headers = {
    "Content-Type":"application/json",
    "pinata_api_key": os.getenv('PINATA_API_KEY'),
    "pinata_secret_api_key": os.getenv('PINATA_SECRET_API_KEY')
}

def pinJSONtoIPFS(json):
    r = requests.post("https://api.pinata.cloud/pinning/pinJSONToIPFS",
                    data=json,
                    headers=headers)

    ipfs_hash = r.json()["IpfsHash"]
    return f"ipfs://{ipfs_hash}"

def convertDataToJSON(time, description):
    data = {
        'pinataOptions':{"cidVersion":1},
        'pinataContent': {
            "name":"Birth Certificate",
            "description":description,
            #"image": "ipfs://bafybeihsecbomd7gbu6qjnvs7jinlxeufujqzuz3ccazmhvkszdjpzzrsu",
            "time": time
        }
    }

    return json.dumps(data)

def initContract():
    with open(Path('MedicalHistory.json')) as json_file:
        abi = json.load(json_file)

    return w3.eth.contract(address=os.getenv("MEDHIST_ADDRESS"), abi=abi)

