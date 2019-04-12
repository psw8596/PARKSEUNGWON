from django.urls import path
from .views import item_list, item_detail

app_name = 'shop'

urlpatterns = [
    path('', item_list),
   # path('<int:pk>', item_detail)
    path('100/', item_detail),
    path('123/', item_detail),    
    path('123123/', item_detail),
]