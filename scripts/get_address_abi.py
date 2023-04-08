import time
import requests
import csv
import os

os.environ["HTTP_PROXY"] = "http://127.0.0.1:10809"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:10809"

def get_contract_abi(address):
    url = f"http://api.etherscan.io/api?module=contract&action=getabi&address={address}&format=raw"
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Unable to fetch ABI for {address}, status code {response.status_code}"

input_csv_file = r'D:\1.csv' # Replace with the path to your input CSV file
output_csv_file = r'D:\contract_abis.csv' # Replace with the path to your output CSV file

with open(input_csv_file, newline='') as infile, open(output_csv_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer.writerow(['Address', 'ABI'])

    for row in reader:
        address = row[0] # Assuming contract address is in the first column
        abi = get_contract_abi(address)
        time.sleep(15)
        writer.writerow([address, abi])
        print(f"Retrieved ABI for {address}")

print("Done!")
