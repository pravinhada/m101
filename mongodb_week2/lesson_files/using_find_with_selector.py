
import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the school database
db=connection.students
scores = db.grades


def find():

    print "find, reporting for duty"

    query = {'type':'exam'}
    selector = {'student_id':1, '_id':0}
    # equivalent mongodb command
    # db.grades.find({type:'exam'},{student_id:true,'_id':false})

    try:
        iter = scores.find(query, selector)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    sanity = 0
    for doc in iter:
        print doc
        sanity += 1
        if (sanity > 10):
            break
        


def find_one():

    print "find one, reporting for duty"
    query = {'student_id':10}
    # equivalent mongodb command
    x# db.grades.find({student_id:10}).limit(1)
    
    try:
        doc = scores.find_one(query)
        
    except:
        print "Unexpected error:", sys.exc_info()[0]

    
    print doc


find()
find_one()
