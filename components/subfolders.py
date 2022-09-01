import os

os.walk(directory)
[x[0] for x in os.walk(directory)]
next(os.walk('.'))[1]