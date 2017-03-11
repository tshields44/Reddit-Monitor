
'''
Incomplete did it in Pyspark notebook
'''



import boto3

from pyspark import SparkContext





december_comments = sc.textFile("s3a://historical-reddit-comments/Dec_2016/*")
january_comments = sc.textFile("s3a://historical-reddit-comments/Jan_2017/*")

def monthly_trends(data)
    subreddits_rdd = data.flatMap(lambda x: json.loads(x))\
                                    .map(lambda comment: (comment['subreddit'], 1))\
                                    .reduceByKey(lambda a, b: a+b)\
                                    .sortBy(lambda a: a[1], ascending=False)

    # converts RDD to Spark DF
    subreddits_DF = subreddits_rdd.toDF()

    # converts DF to Pandas DF
    subreddits_pd = subreddits_DF.toPandas()

    #
    subreddit_pandas.columns = ['Subreddit', 'Comments']


    top_10_subreddits = subreddit_pandas.head(10)





if __name__ == '__main__':
    # setup spark session
    sc = SparkContext()
