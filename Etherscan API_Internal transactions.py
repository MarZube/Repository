import requests
import certifi
import time
import pandas as pd
from datetime import datetime

#Provable main address
address = ["0x3dBDc81a6edc94c720B0B88FB65dBD7e395fDcf6"]

#11 months ago -> no longer time period on Etherscan
start_block = 10677178
end_block = 12844363
# mind the API KEY (end of url)

data = pd.DataFrame()

for k in address:
    time.sleep(0.2)
    for i in range(end_block, start_block, -500):
        time.sleep(0.2)
        #for internal transactions
        url = "https://api.etherscan.io/api?module=account&action=txlistinternal&address=" + k + \
                "&startblock=" + str(i - 500) + "&endblock=" + str(i) + "&sort=desc&apikey=V95KZCDIMQZMB885H5X9H2UD1HG1SJWSNC"

        response = requests.get(url, verify = certifi.where())
        address_content = response.json()
        #print(address_content)

        result = address_content.get("result")

        for transaction in result:
            block_no = transaction.get("blockNumber")

            timestamp = int(transaction.get("timeStamp"))
            new_Date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            hash = transaction.get("hash")
            tx_from = transaction.get("from")
            contract_address = transaction.get("contractAddress")
            tx_to = transaction.get("to")
            value = transaction.get("value")
            trans_type = transaction.get("type")
            error = transaction.get("isError")
            #tokenName = transaction.get("tokenSymbol")
            #token_decimal = transaction.get("tokenDecimal")
            #tansaction_index = transaction.get("transactionIndex")
            gas = transaction.get("gas")
            #LINK_value = Decimal(value) / Decimal("1000000000000000000")  # calculation to LINK
            #gas_price = transaction.get("gasPrice")
            gas_used = transaction.get("gasUsed")
            #transaction_fee = Decimal(gas_price) * Decimal(gas_used) / Decimal("1000000000000000000")
            #cumulativeGasUsed = transaction.get("cumulativeGasUsed")
            #input_trans = transaction.get("Input")

            data_new = pd.DataFrame(
                {
                    'block_no': [block_no],
                    'timestamp': [new_Date],
                    'hash': [hash],
                    'tx_from': [tx_from],
                    'contract_address': [contract_address],
                    'tx_to': [tx_to],
                    'value': [value],
                    'trans_type': [trans_type],
                    #'tokenName': [tokenName],
                    #'token_decimal': [token_decimal],
                    #'tansaction_index': [tansaction_index],
                    'gas': [gas],
                    #'LINK_value': [LINK_value],
                    #'gas_price': [gas_price],
                    'gas_used': [gas_used],
                    'error' : [error]
                    #'transaction_fee': [transaction_fee],
                    #'cumulativeGasUsed': [cumulativeGasUsed],
                    #'input': [input_trans]
                }
            )

            data = pd.concat([data, data_new])

print(data)
print("You are done")

data.to_csv("file directory/title.csv")
