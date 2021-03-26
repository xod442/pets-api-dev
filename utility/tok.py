import requests
import json

# URL to create an organization
org_url = 'http://localhost/apps/'

app_id = 'mobile'
app_secret = 'test'

headers = {"Content-Type":"application/json"}
payload = {"app_id":app_id,"app_secret":app_secret}

# Convert to json
payload=json.dumps(payload)

# r = requests.post(org_url, headers=headers, data=payload)

# URL for requesting token
tok_url = 'http://localhost/apps/access_token/'

r = requests.post(tok_url, headers=headers, data=payload)

r = json.loads(r.text)

token = r['token']
print('-------------------------------------------------------------------')
print(token)
print(app_id)

# Now get the list of stores
store_url = 'http://localhost/stores/'
headers = {"X-APP-ID":app_id,"X-APP-TOKEN":token,"Content-Type":"application/json"}

print(store_url)
print(headers)

r = requests.get(store_url, headers=headers)
r = json.loads(r.text)
print(r)

for store in r['stores']:
    print('=========================================')
    print(store['id'])
    print('=========================================')

# print(r.headers)
# print(r.content)

count = 0
cr = '\n'
# Get number of lines from file
num_lines = sum(1 for line in open("stores.csv"))

fi = open("stores.csv", 'r')

# print (num_lines)
line = fi.readline()
count = count + 1
line=line.strip("\n")

while count <= num_lines:

    # print ('..............read line')


    element = line.split(",")
    # print ('this is the regular element %s' % (element))

    name = element[0]
    street_address = element[1]
    city = element[2]
    state = element[3]
    zip = element[4]
    phone = element[5]
    neighborhood = element[6]

    out = [name,street_address,city,state,zip,phone,neighborhood]

    print(out)

    # Create new store
    store = {
      "neighborhood":element[6],
      "name":element[0],
      "street_address":element[1],
      "city":element[2],
      "state":element[3],
      "zip":element[4],
      "phone":element[5]
    }

    # Convert to json
    store=json.dumps(store)

    print('--------------------posting store---------------------')
    r = requests.post(store_url, headers=headers, data=store)

    line = fi.readline()
    count = count + 1
    line=line.strip("\n")



# print('--------------------printing all stores---------------------')
# r = requests.get(store_url, headers=headers)
# r = json.loads(r.text)
# print(r.text)
