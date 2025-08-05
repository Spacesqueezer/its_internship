from django.urls import path
from .views import index_page, get_last_deals

urlpatterns = [
    path('', index_page, name='user_info'),
    path('last_active_deals/', get_last_deals, name='last_active_deals'),
]
