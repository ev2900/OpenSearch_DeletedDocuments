# OpenSearch DeletedDocuments

<img width="85" alt="map-user" src="https://img.shields.io/badge/views-2010-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-1041-green">

When a document is deleted in OpenSearch it is marked for deletion. It is not physically removed from storage until a merge removes the document(s) from the segments underlying the index shards.

This only applies when documents are being deleted from an index. If an entire index is deleted the delete is immediate. Deleting an index doesn't create any delete markers.

To determine the number of documents marked for deletion in indices you can either

* Run the ```GET _cat/indices?v``` API looking at the *docs.deleted* field

OR

* Look at the **DeletedDocuments** metric in CloudWatch

If you have indices with document marked for deletion you can expunge the deleted documents using the force merge API with the *only_expunge_deletes* parameter.

Run the ```POST /<index-name>/_forcemerge?only_expunge_deletes=true``` API to expunge the deleted documents.

*Note* the force merge operation triggers an **I/O intensive process** and **blocks all new requests** to your cluster until the merge is complete. Only call the force merge operation against read-only indices, **when no additional data is being written to the index**.

## Example
Go to the [Example](https://github.com/ev2900/OpenSearch_DeletedDocuments/tree/main/Example) section of this repository for instructions on how to run an example that will demonstrate these concepts
