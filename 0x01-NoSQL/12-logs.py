#!/usr/bin/env python3
from pymongo import MongoClient

def get_nginx_logs_stats(mongo_collection):
    # Get the total number of documents in the collection
    total_logs = mongo_collection.count_documents({})

    # Get the number of documents for each method: GET, POST, PUT, PATCH, DELETE
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = [mongo_collection.count_documents({"method": method}) for method in methods]

    # Get the number of documents with method=GET and path=/status
    get_status_logs = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    # Display the stats
    print(f"first line: {total_logs} logs where {total_logs} is the number of documents in this collection")
    print("second line: Methods:")
    for method, count in zip(methods, method_counts):
        print(f"\t{count} lines with the number of documents with the method={method}")
    print(f"one line with the number of documents with:\nmethod=GET\npath=/status\n{get_status_logs}")

if __name__ == "__main__":
    # Connect to the MongoDB server
    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Get and display the stats
    get_nginx_logs_stats(nginx_collection)

    # Close the MongoDB connection
    client.close()

