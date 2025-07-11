import redis
from django.conf import settings


redis_client = redis.StrictRedis(
    host=getattr(settings, 'REDIS_HOST', 'localhost'),
    port=getattr(settings, 'REDIS_PORT', '6379'),
    db=0,
    decode_responses=True
)