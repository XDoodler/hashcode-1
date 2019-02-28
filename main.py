def get_score(slide_dict,prev_slide_num,next_slide_num):
    set1,set2 = set(slide_dict[prev_slide_num]),set(slide_dict[next_slide_num])
    return min(len(set1-set2),len(set1&set2),len(set2-set1))

#
#def maximize(dict):
#   dict: {0:["tag1","tag2"],1:["tag3","tag4"]}
#   returns {"ID1-ID2":score1, "ID2-ID3":score2}

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
h,v = input_("test.txt")
