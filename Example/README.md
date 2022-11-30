# Delete Documents Example

1. Run the CloudFormation stack

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=open-search-deleteddocuments&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/opensearch_deleteddocuments.yaml)

The resources created by the CloudFormation stack are documented in the architecture below

<img alt="os-deleted-document-arch" src="https://github.com/ev2900/OpenSearch_DeletedDocuments/blob/main/Example/architecture.png">

2. Create an index and populate it with sample data

via. the Cloud9 enviorment created by the CloudFormation script 

* ```pip install requests``` 
* update the *os_url* variable in the python script *1_create_index_w_data.py* with the domain endpoint url of the OpenSearch domain created by the CloudFormation script
* ```python OpenSearch_DeletedDocuments/Example/1_create_index_w_data.py```

You will see console window print output confirming that documents are being sent to OpenSearch. When the script is finished an index **log-data-1** with 1000 documents was created on your OpenSearch domain

3. Delete documents

To demonstrate how document deletion work. We will run a script to delete random documents
* update the *os_url* variable in the python script *2_delete_documents.py* with the domain endpoint url of the OpenSearch domain created by the CloudFormation script
* ```python OpenSearch_DeletedDocuments/Example/2_delete_documents.py```

You will see console window print output confirming that documents are being deleted. When the script is finished documents will have been deleted from the index **log-data-1**

4. View the number of documents marked for deletion 

* via. API 

```GET _cat/indices?v```

<img width="1000" alt="os-deleted-document-api" src="https://github.com/ev2900/OpenSearch_DeletedDocuments/blob/main/Example/api_number_doc_marked_for_delete.png">

* via. Cloudwatch 

<img width="1000" alt="os-deleted-document-api" src="https://github.com/ev2900/OpenSearch_DeletedDocuments/blob/main/Example/cloudwatch_number_doc_marked_for_delete.png">

5. Force merge to expunge the deleted documents

```POST /log-data-1/_forcemerge?only_expunge_deletes=true```

Notice the force merge causes a spike in CPU 

<img width="1000" alt="os-deleted-document-api" src="https://github.com/ev2900/OpenSearch_DeletedDocuments/blob/main/Example/cpu_spike.png">

6. Re-check the number of documents flagged for delete

* via. API 

```GET _cat/indices?v```

<img width="1000" alt="os-deleted-document-api" src="https://github.com/ev2900/OpenSearch_DeletedDocuments/blob/main/Example/api_number_doc_marked_for_delete_after.png">

* via. Cloudwatch

<img width="1000" alt="os-deleted-document-api" src="https://github.com/ev2900/OpenSearch_DeletedDocuments/blob/main/Example/cloudwatch_number_doc_marked_for_delete_after.png">
