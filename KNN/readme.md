## K - Nearest Neighbour Classifier

A classic lazy algorithm.

### Working

My code:

- accepts input as single list where each list element contains 2 elements.
- at index 0, a tuple representing the input feature
- at index 1, a string which holds the class name.
- At first, All euclidean distances are computed between given point p and the 
 points in the dataset.
- Then they are sorted based on the distance using selection sort.
- Then top K classes are choosen using python list slicing (sorted_dist_arr[:k])
- Then the class with maximum frequency in the top K classes is returned as the 
output

Could have used collections and other shortcuts to simplify the code but it is always
fun to write algorithms yourselves.
