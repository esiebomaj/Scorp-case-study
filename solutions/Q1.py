from typing import List, NamedTuple

# helper functions for db accesss in order not to polute the main function with SQL queries
def get_single_post(post_id:int):
    """
    returns a single post with id = post_id
    """
    sql = f"SELECT * FROM post WHERE id = {post_id}"
    with engine.connect() as connection:
        post = connection.execute(sql)
    return post

def get_post_likes(post_id:int):
    """
    returns all likes for a post with id = post_id
    """
    sql = f"SELECT * FROM like WHERE post_id = {post_id}"
    with engine.connect() as connection:
        likes = connection.execute(sql)
    return likess

def get_post_author(author_id):
    """
    returns all likes for a post with id = post_id
    """
    sql = f"SELECT * FROM user WHERE id = {author_id}"
    with engine.connect() as connection:
        author = connection.execute(sql)
    return author

def get_following_list(user_id:int)->List[int]:
    """
    returns list of all users following 
    """
    sql = f"SELECT following_id FROM follow WHERE follower_id = {user_id}"
    with engine.connect() as connection:
        following = connection.execute(sql)

    return following



# Q1 - Day-to-day programming
def get_posts(user_id: int, post_ids: List[int]) -> List[Post]:
    '''
    Returns a list of posts corresponding to post_ids
    list of posts is in the same order as post ids
    list of post should have null for non existing post_ids
    query format ====> db_posts = SELECT * FROM post WHERE id IN post_ids
    '''
    post_list = []

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
        author = get_post_author(post_id)

        # determine if the author is followed by requesting user
        # get following list for requesting user 
        if author.id in following_list:
            author.followed = True
        else:
            author.followed = False

        # attach author to coresponding post
        post.owner = author

        # append post to post_list 
        post_list.append(post)
        
    return post_list