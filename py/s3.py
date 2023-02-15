# import boto3

# client= boto3.client('s3')
# range=s3.list_buckets()
# for i in range[("Buckets")]:
#     print(f'{i["Name"]}')


# import boto3

# s3_client = boto3.client('s3')

# response = s3_client.create_bucket(
#      Bucket='my_bucket1'
# )
# CreateBucketConfiguration={
#        'LocationConstriant': 'ap-northeast-3'
#     },
# print(response)


# import boto3
# #create an object for s3 service
# s3_client = boto3.client('s3',region_name='ap-northeast-3')
# #create bucket

# response = s3_client.create_bucket(

#    Bucket='my_bucket1',
#    CreateBucketConfiguration={
#        'Location_Constriant': 'ap-northeast-3'
#     },

# )
# print('response')


import boto3
#create an object for s3 service
s3 = boto3.client('s3',region_name='ap-northeast-3')
r= s3.delete_bucket(
    Bucket = 'rayachoty-bucket'
)
print(response)




