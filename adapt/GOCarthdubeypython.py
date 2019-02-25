import math
import json
import matplotlib.pyplot as plt
level=[1,2,3]   #1-easy 2-medium 3-hard
marks=[2,5,8,11,14,17,20,23,26]   #Possible marks for the question
tm=0        #TotalMarks
#2-easy,5-easy,8-easy,11-mid, 14-mid, 17-mid, 20-hard, 23-hard, 26-hard (As defined in problem statement)
def upgrade(l,m,total,marks):
    total=total+m
    if(m!=26):
        z=m+3
    else:
        z=m
    y=0
    
    if(z<11):
        y=1
    elif(z>8 and z<20):
        y=2
    elif(z>17):
        y=3
    return y,z,total
def downgrade(l,m,marks):
    if(m!=2):
        z=m-3
    else:
        z=m
    y=0
    if(z<11):
        y=1
    elif(z>8 and z<20):
        y=2
    elif(z>17):
        y=3
    return y,z
def printques(y,z,data,npr):
    blue=str(y)
    z=z
    red=str(z)
    p=data['Questions'][blue][red]
    wow=npr
    dip=wow[z]
    print(p[dip])
    if(y==1):
        print('Level-Easy')
    elif(y==2):
        print('Level-Medium')
    elif(y==3):
        print('Level-Hard')
    print('Marks for this question:')
    print(z)
    print('If you wish to give the wrong answer, press 0.')
    print('If you wish to give the right answer press 1.' )
    n=int(input())
    wow[z]=wow[z]+1
    return n,wow
#Starting point now
l=2
m=14
nonrep=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #So that questions don't repeat
yourmarks=[]
with open("questions.json") as json_file:
    data = json.load(json_file)
t=printques(l,m,data,nonrep)
for i in range(0,10):
    if(t[0]==0):
        yourmarks.append(m)
        res=downgrade(l,m,marks)
        first=res[0]
        l=res[0]
        second=res[1]
        m=res[1]
        t=printques(first,second,data,nonrep)
        nonrep=t[1]
    
    elif(t[0]==1):
        yourmarks.append(m)
        res=upgrade(l,m,tm,marks)
        first=res[0]
        l=res[0]
        second=res[1]
        m=res[1]
        tm=res[2]
        t=printques(first,second,data,nonrep)
        nonrep=t[1]
print('Your Final score is:')
print(tm)
ques=[1,2,3,4,5,6,7,8,9,10]
plt.plot(ques,yourmarks)
plt.xlabel("Questions")
plt.ylabel("Marks")
tm=str(tm)
plt.title('Score Graph generated, Total score is:'+tm)
plt.show()
