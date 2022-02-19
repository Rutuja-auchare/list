print("WELCOME TO KBC")
question_list=["how many continents are there?",
"what is the capital of india?",
"navgurukul mai kon sa course paya jata hai?"
]
optoin_list=[["four","nine","seven","eight"],
["chindigad","bhopal","chennai","delhi"]
["software engineering","turisum","counseling","agreecluture"]
]
solustion_list=[3,4,1]
ans=["3.seven","4.delhi","1.software engineering"]
i=0
r=1
y=0
count=0
while i<len(question_list):
    i1=(question_list)[i]
    print(i1)
    j=0
    k=i
    while j<len(optoin_list[i]):
        i=(option_list)[k][j]
        print(j+1,i)
        j=j+1
    lifeline1=input("do you want 50 50 lifeline:")
    if lifeline=="yes":
        if count==o:
            print(ans[y+i])
            print(ans[y+r])
            n=int(input("enter the answer"))
            if n==solution_list[i]:
                print("your first answer is right")
                print("ypur score is",1)
                else:
                    print("your first answer is wrong")
                    print("your score is",0)
                    print("game is over")
                    breck
                count+=1
            else:
                print("you already use lifeline")
                m=int(input("enter answer"))
                if m==solustion_list[i]:
                    print("your second answer is right")
                    print("your score is ,2")
                else:
                    print("your second answer is wrong")
                    print("your score is",1)
        elif lifeline=="no":
            u=int(input("choose your answer"))
            if u==solustion_list[i]:
                print("your answer is correct")
                print("your score is 3")
                print("you are winner in this game")
            else:
                print("your answer is wrong")
                print("your score is,2")
                print("game is over")
                breck
        else:
            print("error")
        i+=1        





















print(" solusion_list=[3,4,1]
ans=["3.sevev", "4 .delhi","1.software engineering"]
i=0
r=1
y=0
count=0
while i<len(question_list):
    i1=(question_list)[i]
    print(i1)
    j=0
    k=i
    while j<len(option_list)[i]:
        i=()



        
    




















