import requests
requests.packages.urllib3.disable_warnings() #if we are facing any security issues we can use this 

def get_endpoint(url):
    data = {
        "subscriptions": [
            "a24d81d4-940f-4503-95d7-46748219b4d8"
        ],
        "regions": [
            "centralindia",
            "CENTRALINDIA"
        ],
        "tags": [
            "ms-resource-usage_@_azure-cloud-shell"
              ],
        "rproviders": [
            "Microsoft.Compute",
            "Microsoft.Storage",
            "microsoft.compute",
            "Microsoft.Network",
            "Bastion Scale Units",
            "Microsoft.AAD",
            "microsoft.network",
            "Microsoft.RecoveryServices"
        ],
        "date": [
            "2023-7-24T00:00:00.0000000Z",
            "2023-7-31T00:00:00.0000000Z"
        ],
        "filter": [],
        "flag": [],
        "userid": 48,
        "cust_id": 11,
        "domains": [
            "Zenworx.in"
        ]
    }

    response = requests.post(url, json=data,verify= False)


    if response.status_code == 200:
        res_dict = {}
        result = response.json()
        val = result.get('tdata')
        date = result.get( 'txkeys')
        all_dates = date[2:]
        #print(all_dates)
        for i in val:
            cost,cost_p = i.get('data_rows')
            sub_id = i.get('s1')
            if 'Total' in sub_id:
                pass
            else:
                for date,cost,cost_p in zip(all_dates,cost,cost_p):
                    res_dict[(date,sub_id)] = [cost, cost_p]
        print(res_dict)
    else:
        print(f"Request failed with status code: {response.status_code}")



if __name__ =='__main__':
    url = 'http://4.246.189.243/customers/subscription'
    get_endpoint(url)

#___________________________________________________________________________
# basic structure of request module
import requests

requests.get(url)
requests.get(url, json=payload, verify=False)
requests.get(url,  json=payload, headers={‘key’:’value’}, verify=False)
response = requests.get(url)
response.status_code()
response.content
response.text



