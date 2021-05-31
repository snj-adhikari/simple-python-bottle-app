import pandas as pd
import random

def prepareQuestion(): 
    result = pd.DataFrame()

    symbol = ['-' , '+' , '*' , '/' , '%']

    loopRange = range(10)
    for loopRange in loopRange :
        bigNo = random.randint(50 , 500)
        smallNo =random.randint(1 , 50) 
        randomSym = random.randint(0,4)
        query = str(bigNo) + symbol[randomSym] + str(smallNo)
        question = ''
        answer = ''
        
        if symbol[randomSym] == '*' :
            question = str(bigNo) + ' X ' + str(smallNo)

            
        elif symbol[randomSym] == "%": 
            question = str(bigNo) + ' mod ' + str(smallNo)
        
        else : 
            question = str(bigNo) + ' '+ symbol[randomSym] + ' ' + str(smallNo)
        
        answer = round(eval(query));
        dictVar = {
            'question' : question,
            'answer' : answer,
        }
        print(dictVar)
        result = result.append(dictVar, ignore_index=True)

    return result;





