import mincemeat
import glob
import stopwords

# Accessing all the files in directory
# Set the file path here.
file_dir = glob.glob('*')

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
        paper, authors, title = value.split(':::')
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
    for v in vs:
        for word in v:
            if word in result:
                result[word] = result[word] + 1
            else:
                result[word] =v[word]

    return result


# Server part
s = mincemeat.Server()

# Datesource
s.datasource = source_data
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

print results
