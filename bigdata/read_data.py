#!/usr/bin/env python
"""
Program to compute how many times every term occurs accross titles, for each author

"""
import mincemeat
import glob
import pprint

# Accessing all the files in directory
file_dir = glob.glob('/hw3data/*')



# Read the file contain
def contain(fname):
    f = open(fname)
    try:
        value = f.read()
    except:
        print "Exception in file read!"
    finally:
        f.close()
    return value


# Create dictionary for all source data
source_data = dict((fname, contain(fname)) for fname in file_dir)


# mapper function, key is document id and v is contains of document
def mapfn(k, v):
    for value in v.splitlines():
        paper,authors,title = value.split(':::')
        for author in authors.split('::'):
            w = {}
            for word in title.split():
                if word in w:
                    w[word] = w[word] + 1
                else:
                    w[word] = 1

            yield author, w


# reduce function
def reducefn(k, vs):
    result = {}
    # All the stopwords for filtering
    skeys = ['all', 'herself', 'should', 'to', 'only', 'under', 'do', 'weve', 'very', 'cannot', 'werent', 'yourselves', 'him', 'did', 'these', 
             'she', 'havent', 'where', 'whens', 'up', 'are', 'further', 'what', 'heres', 'above', 'between', 'youll', 'we', 'here', 'hers', 
             'both', 'my', 'ill', 'against', 'arent', 'thats', 'from', 'would', 'been', 'whos', 'whom', 'themselves', 'until', 'more', 'an', 
             'those', 'me', 'myself', 'theyve', 'this', 'while', 'theirs', 'didnt', 'theres', 'ive', 'is', 'it', 'cant', 'itself', 'im', 'in', 
             'id', 'if', 'same', 'how', 'shouldnt', 'after', 'such', 'wheres', 'hows', 'off', 'i', 'youre', 'well', 'so', 'the', 'yours', 'being', 
             'over', 'isnt', 'through', 'during', 'hell', 'its', 'before', 'wed', 'had', 'lets', 'has', 'ought', 'then', 'them', 'they', 'not', 
             'nor', 'wont', 'theyre', 'each', 'shed', 'because', 'doing', 'some', 'shes', 'our', 'ourselves', 'out', 'for', 'does', 'be', 'by', 
             'on', 'about', 'wouldnt', 'of', 'could', 'youve', 'or', 'own', 'whats', 'dont', 'into', 'youd', 'yourself', 'down', 'doesnt', 'theyd', 
             'couldnt', 'your', 'her', 'hes', 'there', 'hed', 'their', 'too', 'was', 'himself', 'that', 'but', 'hadnt', 'shant', 'with', 'than', 
             'he', 'whys', 'below', 'were', 'and', 'his', 'wasnt', 'am', 'few', 'mustnt', 'as', 'shell', 'at', 'have', 'any', 'again', 'hasnt', 
             'theyll', 'no', 'when', 'other', 'which', 'you', 'who', 'most', 'ours ', 'why', 'having', 'once']

    # loop starts here.
    for v in vs:
        for word in v:
            if len(word)>1 and word.lower() not in skeys:
                if word in result:
                    result[word] = result[word] + 1
                else:
                    result[word] = v[word]

    return result


# Server part
s = mincemeat.Server()

# Datesource
s.datasource = source_data
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

# print preety
pprint.pprint(results)
