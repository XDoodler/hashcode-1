import sys
import numpy as np
def get_score(slide_dict,prev_slide_num,next_slide_num):
    set1,set2 = set(slide_dict[prev_slide_num]),set(slide_dict[next_slide_num])
    return min(len(set1-set2),len(set1&set2),len(set2-set1))

#
#def maximize(dict):
#   dict: {0:["tag1","tag2"],1:["tag3","tag4"]}
#   returns {"ID1-ID2":score1, "ID2-ID3":score2}
def sort_by_score(d):
    return np.array(d).view('i8,i8,i8').sort(order = ["f2"],axis = 0)
def arrange(v,h):
    vl = sort_by_score(maximize(v))
    
def brute_force(horizontal, vertical):
    frame = []
    for item_id in horizontal:
        f = [item_id]
        frame.append(f)
    l = 0
    f = []
    for item_id in vertical:
        f.append(item_id)
        l += 1
        if l == 2:
            l = 0
            frame.append(f)
            f = []
    print(len(frame))
    for item in frame:
        if type(item) == type(""):
            print(item)
        else:
            print(" ".join(list(map(str,item))))
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
h,v = input_(sys.argv[1])
brute_force(h,v)
