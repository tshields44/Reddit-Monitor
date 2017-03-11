from __future__ import print_function
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kinesis import KinesisUtils, InitialPositionInStream
import datetime
import json


s3_target_bucket_name = 'reddit-spark-streaming'
aws_region = 'us-west-1'
kinesis_stream = 'reddit-spark-streaming'
kinesis_endpoint = 'https://kinesis.' + aws_region + '.amazonaws.com'
kinesis_app_name = 'reddit-trends'
kinesis_initial_position = InitialPositionInStream.LATEST
kinesis_checkpoint_interval = 10
spark_batch_interval = 10



spark_context = SparkContext(appName=kinesis_app_name)

spark_streaming_context = StreamingContext(spark_context, spark_batch_interval)

kinesis_stream = KinesisUtils.createStream(
    spark_streaming_context, kinesis_app_name, kinesis_stream, kinesis_endpoint,
    aws_region, kinesis_initial_position, kinesis_checkpoint_interval)

# Take Dstream and does count of subreddits
subreddits_rdd = kinesis_stream.flatMap(lambda x: json.loads(x))\
                                .map(lambda comment: (comment['subreddit'], 1))\
                                .reduceByKey(lambda a, b: a+b)\
                                .sortBy(lambda a: a[1], ascending=False)

# converts RDD to Spark DF
subreddits_DF = subreddits_rdd.toDF()

# converts DF to Pandas DF
subreddits_pd = subreddits_DF.toPandas()





# save that rdd to S3
commit_to_s3 = subreddits_rdd.saveAsTextFiles('s3://' + s3_target_bucket_name +
            '/spark_streaming_processing/ '+
            datetime.datetime.isoformat(datetime.datetime.now()).replace(':','_'))

spark_streaming_context.start()

spark_streaming_context.awaitTermination()
