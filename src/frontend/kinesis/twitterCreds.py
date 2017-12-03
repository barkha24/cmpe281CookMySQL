
from TwitterAPI import TwitterAPI
import boto3
import json
import twitterCreds

## twitter credentials

consumer_key = "7w2pNZGboJPSNqQs9Zt982vQX"
consumer_secret = "5WfUuN1B2IZ9JUXoZGY6f8vdMQAKeDLiUzZSAytdBxGw6nWB3g"
access_token_key = "923223880524644353-o9kbfng8J8HqQu0iyQKYP0uJbsOtPSN"
access_token_secret = "kbAohAAzKlPycjyKF3QsoKH2Jz9aOD7zEbAn7TUe06bnM"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = boto3.client('kinesis')

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})

for item in r:
    kinesis.put_record(StreamName="twitter", Data=json.dumps(item), PartitionKey="filler")


