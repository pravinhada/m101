
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.reddit
scores = db.stories


def find():

    print "find, reporting for duty"

    query = {'title':{'$regex':'Microsoft'}}
    projection = {'title':1, '_id':0}
    # equivalent mongodb command
    # db.stories.find({title: {$regex:'Microsoft'}},{title:true,'_id':false})

    try:
        iter = scores.find(query, projection)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    for doc in iter:
        print doc
        sanity += 1
        if (sanity > 10):
            break
        

find()

