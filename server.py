
from bottle import Bottle  ,  run ,route , static_file
from backend.logic import *

random_question = '10- 3'
score = 0;

@route('/')
def rootIndex():
    return 'Server is running on localhost:8080 , go to /game'

# Getting static file :) 
@route('/game')
def getIndexFile(): 
    return static_file('index.html' ,root="frontend");


@route('/css/<filename>')
def getIndexFile(filename): 
    return static_file(filename ,root="frontend/css");

@route('/js/<filename>')
def getIndexFile(filename): 
    return static_file(filename ,root="frontend/js");

# For timer
@route('/start')
def timer():
    # Should be on second 
    return 30

# For  question
@route('/question')
def timer():
    # Should be on second 
    return  prepareQuestion()


if __name__ == '__main__':
    run(port=8080 ,debug=True)