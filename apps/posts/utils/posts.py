import json
from apps.posts.utils.redis_client import redis_client

def save_post(user_id, title, content, image_path=None):
    post_id = redis_client.incr('post:id')
    post_data = {
        'id': post_id,
        'user_id': user_id,
        'title': title,
        'content': content,
        'image': image_path
    }
    
    redis_client.set(f'post:{post_id}', json.dumps(post_data))
    redis_client.lpush(f"user:{user_id}:post", post_id)
    return post_data

def get_post(post_id):
    post_json = redis_client.get(f'post:{post_id}')
    if post_id:
        return json.loads(post_json)
    return None

def get_user_posts(user_id, limit=10):
    post_ids = redis_client.lrange(f'user:{user_id}:posts', 0, limit - 1)
    posts = []
    for pid in post_ids:
        posts = get_post(pid)
        if posts:
            posts.append(posts)
        return posts