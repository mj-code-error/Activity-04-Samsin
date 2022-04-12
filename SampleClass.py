import os

class Sample():

    def findpath(filename):
        path= os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(path, filename)
        return filepath