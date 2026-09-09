import math

def euclidean_distance(p1,p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# dataset in the form [(coordinate),classname]
dataset = (
            [(1,2),'A'],
            [(1,3),'A'],
            [(2,2),'A'],
            [(2,7),'A'],
            [(8,3),'B'],
            [(9,1),'B'],
            [(7,9),'B'],
            [(8,2),'B'],
            [(24,1),'C'],
            [(24,3),'C'],
            [(22,4),'C']
        )

def predict(p,k):
    class_with_dist = []
    for row in dataset:
        dist = euclidean_distance(p,row[0])
        class_with_dist.append([row[1],dist])
    # sort the distances
    for i in range(len(class_with_dist)):
        min_index = i
        for j in range(i+1,len(class_with_dist)):
            if class_with_dist[j][1] < class_with_dist[min_index][1]:
                min_index = j
        if min_index != i:
            class_with_dist[min_index], class_with_dist[i] = class_with_dist[i], class_with_dist[min_index] # swap
    
    # now choose the top k closest classes
    top_classes = {}
    for row in class_with_dist[:k]:
        top_classes[row[0]] = top_classes.get(row[0],0) + 1
    return max(top_classes, key = top_classes.get)
    
print(predict((22,3),3))
    
