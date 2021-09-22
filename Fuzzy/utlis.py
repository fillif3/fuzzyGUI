def centroid(fuzzy_sets,weights,number_of_points=100):
    left,right = getBoundsOfSet(fuzzy_sets)
    step = (right-left)/number_of_points
    arg=left
    sum=0
    membershipValueSum=0
    for _ in range(number_of_points):
        values=[]
        for f,w in zip(fuzzy_sets,weights):
            values.append(min(f.get_fuzzy_value(arg),w))
        membershipValue = max(values)
        sum+=membershipValue*arg
        membershipValueSum+=membershipValue
        arg+=step
    return sum/membershipValueSum


def getBoundsOfSet(fuzzy_sets):
    max_left = fuzzy_sets[0].left
    max_right = fuzzy_sets[0].right
    for f in fuzzy_sets:
        if f.left < max_left:
            max_left = f.left
        if f.right > max_right:
            max_right = f.right
    return max_left,max_right

