from web3.auto import w3
import json
import sys

if __name__ == "__main__":

    pr_key = "e741ff3c7e156539712526cd00d8a7fec35c335e0d2eb87278c0dd5649cbf4c9"
    my_address = "0x18d5c1c16bbDAc4b55Efe5A1c0a6bF04e11FcE26"

    try: 
        (sys.argv[1])
    except IndexError:
        # Для отладки через IDE
        eth_amount = 0.1
        ds_address = "0xB64fE1236f7D72c15Bffc6C529f750A8ACa4f8A2"
    else:
        eth_amount = float(sys.argv[1][1:])
        ds_address = sys.argv[2][1:]

    gas_limit = 40000
    gas_price = 15

    transaction = {
        'from': my_address,
        'nonce': 1,
        'gasPrice': int(gas_price*(10**9)),
        'gas': gas_limit,
        'to': ds_address,
        'value': int(eth_amount*(10**18)),  # ETH  
        'data': my_address,  # комментарий к сдаче
        'chainId': 4,  # rinkeby
    }

    signed = w3.eth.account.sign_transaction(transaction, pr_key)  # подписывание транзакции

    # --- Добавление подписи к транзакции
    new_raw = signed.rawTransaction.hex()
    new_hash = signed.hash.hex()
    transaction['rawTransaction'] = new_raw
    transaction['hash'] = new_hash
    transaction['r'] = signed.r
    transaction['s'] = signed.s
    transaction['v'] = signed.v

    # --- Создание JSON файла подписанной транзакции
    with open ('transaction.json', 'w') as raw_transaction:
        json.dump(transaction, raw_transaction, indent=2)

    # --- Вывод подписанной JSON транзакции в консоль
    json_transaction = json.dumps(transaction, indent=2)
    print(json_transaction)
