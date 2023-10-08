import redis
from django.http import JsonResponse
from django.views import View

# Create a Redis connection
# redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

class GetRedisDataView(View):

    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    def get(self, request):
        # Replace 'your_key' with the actual key you want to fetch from Redis
        key = 'JHRML'

        # Try to fetch the data from Redis
        try:
            data = self.redis_client.get(key)
            print(data)
            if data is not None:
                # Data found in Redis, decode it (Redis stores data as bytes)
                data = data.decode('utf-8')
                return JsonResponse({'data': data})
            else:
                return JsonResponse({'error': 'Key not found in Redis'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
