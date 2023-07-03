import boto3
from datetime import datetime as dt

today = dt.today()
todaydate= today.strftime("%Y%m%d")

def lambda_handler(event,context):

    s3_client = boto3.client('s3')

    bucket_name = "adaobi-organize-s3-object"
    list_objects_response = s3_client.list_objects_v2(Bucket=bucket_name)

    #using the get method to target only the key contents from the api call response
    get_contents = list_objects_response.get("Contents")
    get_all_s3_objects_and_foldernames = []

    for item in get_contents:
        s3_object_name = item.get("Key")

        get_all_s3_objects_and_foldernames.append(s3_object_name)

    directory_name = todaydate + "/"

    if directory_name not in get_all_s3_objects_and_foldernames:
        s3_client.put_object(Bucket=bucket_name, Key= (directory_name))

    for item in get_contents:
        object_creation_date = item.get("LastModified").strftime("%Y%m%d") + "/"
        object_name = item.get("Key")

    #condition to check if file creation date matches a folder in the s3 bucket. This will be the folder the object is pushed into 
        if object_creation_date == directory_name and "/" not in object_name:
            s3_client.copy_object(Bucket=bucket_name, CopySource=bucket_name+"/"+object_name, Key=directory_name+object_name)
            s3_client.delete_object(Bucket=bucket_name, Key=object_name)


