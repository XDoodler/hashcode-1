slide_dict = {0:["cat","beach","sun"],1:["selfie","smile"]}
slides = []
def get_score(prev_slide_num,next_slide_num):
    set1,set2 = set(slide_dict[prev_slide_num]),set(slide_dict[next_slide_num])
    return min(len(set1-set2),len(set1&set2),len(set2-set1))
def input_():
    n = int(input())
    photos = {}
    for i in range(n):
        inp = input().strip().split()
        hv = inp[0]
        tags = inp[-int(inp[1])]
        photos[i] = [hv,tags]
    print(photos)
print(input_())

    
