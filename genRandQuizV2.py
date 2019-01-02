import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
   'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck',
   'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
   'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
   'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
   'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(35):
    fileName = "TestNumber" + str(quizNum + 1) + ".txt"
    createFile = open(fileName,"w+")

    header = 'State Capitals Quiz #' + str(quizNum + 1) + "\n\n"
    createFile.write(header)

    states = list(capitals.keys())
    random.shuffle(states)

    ansFileName = "TestNumber" + str(quizNum + 1) + "_AnsKey.txt"
    createAnsFile = open(ansFileName,"w+")

    createAnsFile.close()
    createFile.close()

    appendFile = open(fileName, "a")
    appendAnsKeyFile = open(ansFileName,"a")

    for questionNum in range(50):
        question = states[questionNum]
        answer = capitals.get(states[questionNum])

        randNum1 = random.randint(0, 49)
        randNum2 = random.randint(0, 49)
        randNum3 = random.randint(0, 49)

        print(randNum1)
        print(randNum2)
        print(randNum3)

        falseAns1 = capitals.get(states[randNum1])
        falseAns2 = capitals.get(states[randNum2])
        falseAns3 = capitals.get(states[randNum3])

        ansBank = [answer,falseAns1,falseAns2,falseAns3]
        random.shuffle(ansBank)

        appendFile.write(str(questionNum + 1) + ".What is the capital of " + question + "?\n\n")
        appendFile.write(ansBank[0] + "\n" + ansBank[1] + "\n" + ansBank[2] + "\n" + ansBank[3] + "\n\n")

        appendAnsKeyFile.write("State: " + question + "\n")
        appendAnsKeyFile.write("Capital: " + answer + "\n\n")

    appendFile.close()
    appendAnsKeyFile.close()
