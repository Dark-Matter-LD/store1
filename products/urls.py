from django.conf.urls import include, url
from django.urls import path, re_path
from products import views

urlpatterns = [
    # path('landing/', views.landing, name='landing'),
    url(r'^product/(?P<product_id>\d+)/$', views.product, name='product'),
    

]