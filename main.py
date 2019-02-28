slide_dict = {0:["cat","beach","sun"],1:["selfie","smile"]}
slides = []
def get_score(prev_slide_num,next_slide_num):
    set1,set2 = set(slide_dict[prev_slide_num]),set(slide_dict[next_slide_num])
    return min(len(set1-set2),len(set1&set2),len(set2-set1))
def input_(fn = ""):
    f = open(fn,"r")
    testcase = int(f.readline())
    horizontal={}
    vertical={}
    p,q=0,0
    a,b=[],[]
    while(testcase):
        testcase-=1
        photo = list(map(str,f.readline().split()))
        if(photo[0]=="H"):
            for i in range(2,len(photo)):
                a.append(photo[i])
            horizontal[p]=a
            a=[]
            p+=1
        if(photo[0]=="V"):
            for i in range(2,len(photo)):
                b.append(photo[i])
            vertical[p]=b
            b=[]
            p+=1
    f.close()
    return horizontal,vertical
print(input_("test.txt"))
