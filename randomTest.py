# coding = GBK
#! python3
# randomTest.py  - Create quizzes with questions and answers in 
# random order, along with hte answer

import random

capitals = { 'Alabama': 'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
'Arkansas': 'Little Rock','California':'Sacramento','Colorado': 'Denver',
'Connecticut':'Hardford','Delaware': 'Dover','Florida' : 'Tallahassee',
'Georgia':'Atlanta','Hawaii':'Honolulu','Idaho':'Boise','Illinois' :
'Springfield','Indiana' :'Indianapolis','Iowa':'Des Moines','Kansas':
'Topeka', 'Kentuncky': 'Frankfort', 'Louisana':'Baton Rouge','Maine':
'Augousta','Marvland':'Annapolis','Massachusetts':'Boston','Michigan':
'Lansing','Minnesota':'Saint Paul' ,'Mississippi':'Jackson','Missouri':
'Jefferson City','MOntana':'Helena','Nebraska' :'Lincoln','Nevada':
'Carson City','New Hampshire':'Concord','New Jersey':'Trenton','New Mexico':
'Santa Fe','New York':'Albany','North Carolina':'Raleigh','North Dakota':
'Bismarck','Ohio':'Columbus','Oklahoma':'Oklahoma City','Oregon':'Salem',
'Pennsylvania':'Harrisburg','Rhode Island':'Providence',
'South Carolina':'Columbia','South Dakota':'Pierre','Tennessee':
'Nashville','Texas':'Austin','Utah':'Salt Lake City','Vermont':'Montpelier',
'Virginia':'Richmond','Washington':'Olympia','West Virginia':'Charleston','Wisconsin':
'Madison','Wyoming':'Cheyenne'}

for quizNum in range(35):
    quizFile = open('capitalsquiz%s.txt' % (quizNum +1 ),'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum +1),'w')
    
    # Wirte out the header 
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) +'State Capitals Quiz (Form %s)' % (quizNum +1))
    quizFile.write('\n\n')


     # Shuffle the order of the states.
    states = list (capitals.keys())
    random.shuffle(states)

     # Loop through all 50 states , making a question for each .

    for questionNum in range(50):
    
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers [wrongAnswers.index(correctAnswer)]
        wrongAnswers= random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
 

     # Write the question and answer options to the quiz file

    quizFile.write('%s. What is the capital of %s? \n' %(questionNum +1,states[questionNum]                       ))
    for i in range(4):
            
        quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i]))
    quizFile.write('\n')

       # write the answer key to a file
    answerKeyFile.write('%s. %s\n'  % (questionNum +1,'ABCD'[
                 answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()

