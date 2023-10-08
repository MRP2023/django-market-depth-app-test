from django.urls import path
from .views import GetRedisDataView  # Import your GetRedisDataView here

urlpatterns = [
    # Define the URL pattern for the GetRedisDataView
    path('get_redis_data/', GetRedisDataView.as_view(), name='get_redis_data'),
    # Add other URL patterns for your project as needed
]
