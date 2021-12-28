from typing import List
Post = 1


# Q2 - Algorithmic design
def merge_posts(list_of_posts: List[List[Post]]) -> List[Post]:

    result = []

    for list_of_post in list_of_posts:
        for post in list_of_post:
            result.append(post)

    result = sorted(result, key=lambda post: post.id) # sort by id
    result = sorted(result, key=lambda post: post.created_at, reverse=True) # sort by created_at in descendiing order

    return result

    # Things to note 
    # 1) Sort Stability: In Python Sorts are guaranteed to be stable. That means that when multiple records have the same key, 
    # their original order is preserved.

    # because of sort stability in python, by first sorting the posts by id and them sorting by created_at 
    # it ensures that posts with the same created_at are sorted by id in ascending order

    # Link to python docs: https://docs.python.org/3/howto/sorting.html#sort-stability-and-complex-sorts


def merge(left:List[Post], right:List[Post])->List[Post]:
    """
    takes 2 sorted list left and right merges the 2 list together 
    and returns a single sorted list 
    """
    merged = []

    i,j = 0,0

    while i < len(left) and j < len(right):

        if left[i]["created_at"] < right[j]["created_at"]:
            merged.append(left[i])
            i+=1

        elif right[j]["created_at"] < left[i]["created_at"]:
            merged.append(right[j])
            j+=1

        else: #this means that  right[j]["created_at"] and  left[i]["created_at"] are equal 
            # Now we have to use the id to determine the order
            if left[i]["id"] < right[j]["id"] :
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1


    if i < len(left):
        while i < len(left):
            merged.append(left[i])
            i+=1

    if j < len(right):
        while j < len(right):
            merged.append(right[j])
            j+=1


    return merged


def merge_posts(list_of_posts: List[List[Post]]) -> List[Post]:
    """
    We are using recursion to do a buttom up merge sort on the list of lists

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
    # continues merging the list_of_posts until we arrive at the base case
    # Base case => the list_of_posts has been merged into a single list of posts (returned in line 41)
    return merge_posts(result)