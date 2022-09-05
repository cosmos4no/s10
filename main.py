import requests
import json
from config import *
import time


def create_sms_send(store_name, token, variant_id, phone):
    headers = {
        'X-Shopify-Access-Token': token,
        'Content-Type': 'application/json',
    }

    data = {
        "order": {
            "phone": phone,
            "send_receipt": True,
            "fulfillment_status": "fulfilled",
            "send_fulfillment_receipt": True,
            "line_items": [
                {
                    "variant_id": variant_id,
                    "quantity": 1
                }
            ]
        }
    }

    rsp = requests.post(
        'https://'+store_name+'.myshopify.com/admin/api/2021-10/orders.json', headers=headers, data=json.dumps(data)
    )
    print(rsp.content)


def mass_create_orders():
    contacts = open('contacts.txt', 'r').readlines()
    print('Loaded '+str(len(contacts))+' Contacts ')
    print('Preparing to send ......')
    c = 1
    for each in contacts:
        print('Sending sms ' + str(c) + '/'+str(len(contacts)))
        print("Phone number : " + each.strip())
        create_sms_send(STORE_NAME, TOKEN, VARIANT_ID, each.strip())
        print("Sending sucessful ")
        time.sleep(1)
        c = c + 1
    print('############### Job Done !')


if __name__ == '__main__':
    mass_create_orders()
