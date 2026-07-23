questions = ["who is shah Rukh khan?", "WWE Wrestler","actor",
        "Astronaut", "plumber", 2],
[ "who is the prime minister of India?", "Narendra Modi", "Rahul Gandhi",
        "Amit Shah", "Manmohan Singh", 1],  
["who is the president of USA?", "Donald Trump", "Barack Obama",
        "Joe Biden", "George Bush", 3],
["who is the founder of Microsoft?", "Bill Gates", "Steve Jobs",
        "Elon Musk", "Mark Zuckerberg", 1],
["who is the founder of Tesla?", "Bill Gates", "Steve Jobs",
        "Elon Musk", "Mark Zuckerberg", 3],
["who is the founder of Facebook?", "Bill Gates", "Steve Jobs",
        "Elon Musk", "Mark Zuckerberg", 4],
["who is the founder of Amazon?", "Jeff Bezos", "Steve Jobs",
        "Elon Musk", "Mark Zuckerberg", 1],
["who is the founder of Apple?", "Bill Gates", "Steve Jobs",
        "Elon Musk", "Mark Zuckerberg", 2],
["who is the founder of Google?", "Bill Gates", "Steve Jobs",
        "Elon Musk", "Larry Page", 4],
prizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
i = 0

for question in questions:
    sum = 0
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")
    #check wheter the answer is correct or not
    a = (input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))
    if(question[5]== a):
        print("Correct answer")
    else:
        print(f"Incorrect answer. The correct answer is option {question[5]}")
        print("better luck next time")
        break
    print(f"you have won {prizes[i]} rupees")
    i += 1