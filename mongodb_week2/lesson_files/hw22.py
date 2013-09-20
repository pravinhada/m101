# Code to remove the lowest homework grade for each Students

import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

def remove_homework():
    print "\nRemoving the grade of type Homework with the lowest socre for each student\n"
    db = connection.students
    grades = db.grades
    query = {'type':'homework'}

    try:
        cursor = grades.find(query)
        cursor = cursor.sort([('student_id', pymongo.ASCENDING),('score',pymongo.ASCENDING)])    
        # cursor = cursor.limit(10)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    loop = -1
    count = 0
    for doc in cursor:
        if doc['student_id'] == loop:
            print doc
            count += 1
        else:
            grades.remove(doc)
            loop = loop + 1

    print "Total Count: ", count

remove_homework()

# After executing this script, run following mongodb command
# db.grades.count()
# db.grades.find().sort({'score':-1}).skip(100).limit(1)
# db.grades.find({},{'student_id':1, 'type':1, 'score':1, '_id':0}).sort({'student_id':1, 'score':1, }).limit(5)


# Averaging the score (the maximum average score) using mongodb command
# db.grades.aggregate({'$group':{'_id':'$student_id','average':{$avg:'$score'}}},{'$sort':{'average':-1}},{'$limit':1})
