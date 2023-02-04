q1="""who is your favourite hero?
a.Ranbir kapoor
b.Ram charan
c.Ian somerhalder
d.paul wesley"""


q2="""who is your food
a.pav bhaji
b.Biryani

C.pani puri
d.Pizza"""

q3="""what is your favourite color
a.Blue
b.yellow
c.Pink
d.Black"""

q4="""what is your brand
a.Mast&hatbour
b.h&m
c.Tokyo Talkies
d.vini vinci"""
questions={q1:"a",q2:"b",q3:"a",q4:"b"}

name=input("Hi whats ur name")
print("Hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("DO you want to skip this question(yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans== questions[i]:
        print("wow!you got one point")
        score=score+1
        print("your current score is :",score)
    else:
        print("your answer ,u lost 1 mark")
        score=score-1
        print("ur current score is",score)
    flag2=input("Do you want to quit? type(yes/no)")
    if flag2=="yes":
                break
print("your total score is",score)
                
