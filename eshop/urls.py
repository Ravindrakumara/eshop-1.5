from django.urls import path
from.import views
#
urlpatterns = [
 path('', views.land, name = 'land'),
 #path('items', views.item.as_view(), name='items'),
 path('items/<int:id>',views.items,name='items'),
 path('shop',views.shop, name='shop'),
 path('Account', views.Account, name='Account'),
 path('cart',views.cart, name='cart')
]
