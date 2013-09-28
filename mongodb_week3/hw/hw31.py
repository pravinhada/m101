# Code to remove the lowest homework grade for each Students

import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

def remove_lowest_score():
    print "\nRemoving the grade of type Homework with the lowest score for each student\n"
    db = connection.school
    grades = db.students
    query = {"scores.type":"homework"}

    try:
        cursor = grades.find(query)
    except:
        print "Unexpected error:", sys.exc_info()[0]

    try:    
        for doc in cursor:
            new_scores = []
            higher_score = 0.0
            for score in doc['scores']:
                if score['type'] == 'homework':
                    if score['score'] > higher_score:
                        higher_score = score['score']
                else:
                    new_scores.append(score)

            new_scores.append({'type':'homework','score':higher_score})
            grades.update({'_id':doc['_id'],'name':doc['name']},{'$set':{'scores':new_scores}})

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


remove_lowest_score()

# After executing this script, run following mongodb command
# db.grades.count()
# db.students.find({_id:100}).pretty()


# Averaging the score (the maximum average score) using mongodb command
# db.students.aggregate({'$unwind':'$scores'},{'$group':{'_id':'$_id', 'average':{$avg:'$scores.score'}}}, {'$sort':{'average':-1}}, {'$limit':1})
