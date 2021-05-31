
from bottle import Bottle , static_file

rootApp = Bottle()

random_question = '10- 3'
score = 0;

@rootApp.route('/')
def rootIndex():
    return 'Server is running on localhost:8080 , go to /game'

# Getting static file :) 
@rootApp.route('/game')
def getIndexFile(): 
    return static_file('index.html' ,root="frontend");


@rootApp.route('/css/<filename>')
def getIndexFile(filename): 
    return static_file(filename ,root="frontend/css");

@rootApp.route('/js/<filename>')
def getIndexFile(filename): 
    return static_file(filename ,root="frontend/js");

# For timer
@routeApp.route('/start')
def timer():
    # Should be on second 
    return 30;

# For  question
@routeApp.route('/question')
def timer():
    # Should be on second 
    return  random_question;

# For maintaing score 
@routeApp.route('/score') 
def score(): 
    return score+1;

if __name__ == '__main__':
    rootApp.run(port=8080 ,debug=True)