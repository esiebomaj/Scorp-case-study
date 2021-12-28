from typing import List

# Note: the main merge post function is in line 60 below. the merge function is an helper that is used in the main function 

# Helper function
def merge(left:List[Post], right:List[Post])->List[Post]:
    """
    takes 2 sorted list left and right, merges the 2 list together 
    and returns a single list of posts that is sorted in decending order of created_at
    if created_at is equal we sort by id
    """

    merged = []

    # we start the pointers at the end of both list 
    i = len(left)-1  # pointer for left list
    j = len(right)-1  # pointer for right list


    while i >= 0 and j >= 0:
        # for both post we check which has a greater created_at and add it the our merged list (descending order)
        if left[i]["created_at"] > right[j]["created_at"]: 
            merged.append(left[i])
            i = i-1

        elif right[j]["created_at"] > left[i]["created_at"]:
            merged.append(right[j])
            j = j-1

        else: 
            #this means that right[j]["created_at"] and left[i]["created_at"] are equal 
            # Now we have to use the id to determine the order
            if left[i]["id"] < right[j]["id"] :
                merged.append(left[i])
                i = i-1
            else:
                merged.append(right[j])
                j = j-1


    # if after coming out of the while loop, either i or j is not yet less than 0
    # that means that we have not finished going through one of the lists
    #  and the if logic below accounts for that 
    if i >= 0:
        while i >= 0:
            merged.append(left[i])
            i = i-1

    if j >= 0:
        while j >= 0:
            merged.append(right[j])
            j = j-1


    return merged



# Main merge post function
def merge_posts(list_of_posts: List[List[Post]]) -> List[Post]:
    """
    returns a list of posts sorted by their created_at in descending order
    We are using a buttom up merge sort algorithm on the list of lists

    """
    N = len(list_of_posts)

    # if the lenght of list_of_posts is 1 that means we have 
    # reached the base case and we just return the first item which will be sorted
    if N == 1:
        return list_of_posts[0]
    
    result = []

    # we iterate through the list_of_posts, taking 2 lists at a time 
    # and merging this 2 list together using the merge function defined above
    for i in range(0, N, 2):
        try:
            merged = merge(list_of_posts[i], list_of_posts[i+1])
            result.append(merged)
        except IndexError:
            result.append(list_of_posts[i])
    
    # This is a recursive call to merge_posts 
    # continues merging the result until we arrive at the base case
    # Base case => the list_of_posts has been merged into a single list of posts (returned in line 71)
    return merge_posts(result)

