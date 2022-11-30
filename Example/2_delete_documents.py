# --------------
# Prerequisite
# --------------
# If you have not already installed the requests package and/or the json package 
# a. pip install requests

import requests
import json
import random

# --------------
# Step 1
# --------------
os_url = '<os_domain_endpoint_url>'
os_url = os_url.rstrip("/")

# --------------
# Step 2
# --------------

print('------ Deleting documents ------')

number_of_log_messages_to_delete = 1000
counter = 0

while counter < number_of_log_messages_to_delete:

    doc_id_to_delete = random.randint(1,999)
    
    delete_document_r = requests.delete(os_url + '/log-data-1/_doc/' + str(doc_id_to_delete), auth=('OSMasterUser', 'AwS#OpenSearch1'), headers= {'Content-type': 'application/json'})
    
    print('Delete document id #' + str(doc_id_to_delete) + ' | ' + delete_document_r.text)
    
    # print(json.dumps(delete_document_r))
    
    counter = counter + 1

print('------')