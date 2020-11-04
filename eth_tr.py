from web3.auto import w3

if __name__ == "__main__":
    pr_key = "e741ff3c7e156539712526cd00d8a7fec35c335e0d2eb87278c0dd5649cbf4c9"
    my_address = "0x18d5c1c16bbDAc4b55Efe5A1c0a6bF04e11FcE26"

    eth_amount = 0.1
    ds_address = "0xB64fE1236f7D72c15Bffc6C529f750A8ACa4f8A2"
    gas_limit = 21000
    gas_price = 24

    transaction = {
        'to': ds_address,
        'value': int(eth_amount*(10**18)),  # 0.1 ETH 
        'gas': gas_limit, 
        'gasPrice': int(gas_price*(10**9)),
        'nonce': 0,
        'chainId': 1
    }

    signed = w3.eth.account.sign_transaction(transaction, pr_key)

    print(transaction)
    print(signed)