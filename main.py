photo_dict = {0:["cat","beach","sun"],1:["selfie","smile"]}
def get_score(prev_slide_num,next_slide_num):
    set1,set2 = set(photo_dict[prev_slide_num]),set(photo_dict[next_slide_num])
    return min(len(set1-set2),len(set1&set2),len(set2-set1))
    
