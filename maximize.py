def maximize(images):
    """
    dict: {0:["tag1","tag2"], 1:["tag3","tag4"]}
    returns [[ID1, ID2, score1], [ID2, ID3, score2]]
    """
    frames = []
    l = []
    for item in images:
        l.append(item)
    if l%2 == 1:
        del(l[-1])
    for i in range(0, len(l), 2):
        score = get_score(images, l[i], l[i+1])
        frames.append([l[i], l[i+1], score])
    return frames




def maximize(images):
    """
    dict: {0:["tag1","tag2"], 1:["tag3","tag4"]}
    returns [[ID1, ID2, score1], [ID2, ID3, score2]]
    """
    frames = []
    l = []
    d = {}
    for item in images:
        l.append(item)
        d[item] = 1
    for i in range(len(l)):
        if l[i] not in d:
            continue
        score = -1
        ind = -1
        for j in range(i+1, len(l)):
            if l[j] not in d:
                continue
            sc = get_score(images, i, j)
            if sc > score:
                score = sc
                ind = j
        if score != -1:
            frames.append([l[i], l[ind], score])
            del(d[l[i]])
            del(d[l[ind]])
    return frames
