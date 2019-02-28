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
    for items in frame:
        for item in items:
            print(item, end = '')
        print()
