testcase = int(input())
horizontal={}
vertical={}
p,q=0,0
a,b=[],[]
while(testcase):
  testcase-=1
  photo = list(map(str,input().split()))

  if(photo[0]=="H"):
    for i in range(2,len(photo)):
      a.append(photo[i])

    horizontal[p]=a
    a=[]
    p+=1

  if(photo[0]=="V"):
    for i in range(2,len(photo)):
      b.append(photo[i])

    vertical[q]=b
    b=[]
    q+=1

print(horizontal)
print(vertical)

'''''
4
H 3 cat beach sun
V 2 selfie smile
V 2 garden selfie
H 2 garden cat
{0: ['cat', 'beach', 'sun'], 1: ['garden', 'cat']}
{0: ['selfie', 'smile'], 1: ['garden', 'selfie']}
'''