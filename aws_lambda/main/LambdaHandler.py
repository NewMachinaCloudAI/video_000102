import json
from boto3 import resource

def read_s3_file():
    
    # Use boto3 to get s3 Resource and read file
    s3 = resource('s3')
    bucket_name = 'video-000110-bucket'
    file_name = 'video-000102-test-file.txt'
    obj = s3.Object( bucket_name , file_name )
    file_contents = obj.get()['Body'].read().decode('UTF-8')
    return file_contents
    
def write_s3_file(file_content):
    
    # Use boto3 to use s3 Bucket and write file
    s3 = resource('s3')
    bucket_name = 'video-000110-bucket'
    file_name = 'video-000102-test-write-file.txt'
    bucket = s3.Bucket(bucket_name)
    bucket.put_object(Key=file_name, Body=file_content )
    return
    

def lambda_handler(event, context):
    
    # Read and return contents of S3 file and print to runtime console
    contents = read_s3_file()
    print( "File Contents->" + contents )
    
    # Write a new file
    write_s3_file('The oceans are still 100% unexplored')
    
    # Return status
    return {
        'statusCode': 200,
        'body': json.dumps('Successful reading and writing of S3 bucket')
    }