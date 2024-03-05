from django.urls import path
from ecommerce_app import views
app_name='ecommerce_app'
urlpatterns=[
    path('',views.AllProdCat,name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>', views.ProDetail, name='prodCatdetail')

]