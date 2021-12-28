from typing import List


# Things to note :
# 1) If it was a real world senario I would probably have used an ORM like sqlAlchemy or django orm depending on the use case
# this will help abstarct the db queries and also prevent the occurence of things like an SQl attack thus improving the application secuirity 

# 2) I have abstracted the db access queries into helper functions in order not to polute the main function with SQL queries


############ helper functions #######################

# recieves a valid sql query and executes it
def query_db(sql):
    with engine.connect() as connection:
        items = connection.execute(sql)

    return items

# returns a single post with id = post_id
def get_single_post(post_id):
    sql = f"SELECT * FROM post WHERE id = {post_id}"
    post = query_db(sql)
    return post

# returns all likes for a post with id = post_id
def get_post_likes(post_id):
    sql = f"SELECT user_id FROM like WHERE post_id = {post_id}"
    likes = query_db(sql)
    return likes

# returns user with id user_id
def get_user(user_id):
    sql = f"SELECT * FROM user WHERE id = {user_id}"
    user = query_db(sql)
    return user

# returns list of user ids
# this user ids corespond to the following of user with id user_id 
# i.e ids of the users who have been followed by user_id
def get_following_list(user_id):
    sql = f"SELECT following_id FROM follow WHERE follower_id = {user_id}"
    following = query_db(sql)
    return following



############## Q1 - Solution ################

def get_posts(user_id: int, post_ids: List[int]) -> List[Post]:
    '''
    Returns a list of posts corresponding to post_ids
    list of posts is in the same order as post ids
    list of post should have null for non existing post_ids
    '''
    post_list = []

    # get the list of all the people the requesting user is following 
    following_list: List[int] = get_following_list(user_id)

    for post_id in post_ids:

        post = get_single_post(post_id)

        if not post:
            # post is does not exist, then we need to append None to post_list and move to the next id
            post_list.append(None)
            continue

        # get all likes for the post 
        likes = get_post_likes(post_id)

        # determine if requesting user has liked the post
        if user_id in likes:
            post.liked = True
        else:
            post.liked = False

        # query to get author of each post
        author = get_user(post.user_id)

        # determine if the author is followed by requesting user
        if author.id in following_list:
            author.followed = True
        else:
            author.followed = False

        # attach author to coresponding post
        post.owner = author

        # append post to post_list 
        post_list.append(post)
        
    return post_list