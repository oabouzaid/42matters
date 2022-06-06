import os
import re
from pyspark import SparkContext

# Initializing the Spark context
sc = SparkContext("local", "PySpark Word Count")

# Reading the file
rdd = sc.textFile("text")  # This path is relative to /src/, as referenced in the Dockerfile


def clean_words(words):
    '''
    Remove any non-alphanumerical character, and also remove the 'BG:' prefixes
    '''
    return [re.sub('(bg\:)|([^A-Za-z0-9]+)', '', word.lower()) for word in words.split()]

rdd = (
    rdd
    # Keep only lines starting with 'BG:'
    .filter(lambda x: x.startswith('BG:'))
    # Split into words and clean them 
    .flatMap(clean_words)
    # Remove empty words
    .filter(lambda x: len(x)>0)
    # Word count
    .map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
    # Sorting by descreasing occurence, most common first
    .sortBy(lambda x: x[1], False)
    .coalesce(1)
)

rdd.saveAsTextFile('./src/output/')
# We can see that there is stop words within the text. Since the question doesn't ask to remove them, I kept them.
# But for more realistic use cases, we might want to remove them, by filtering them out using the list nltk.stopwords

top_n = 50
print("Count preview of the top {} most common words".format(top_n))
print(rdd.take(top_n))
