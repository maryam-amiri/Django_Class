from django.urls import path

from . import views

app_name='reg_buy'

urlpatterns=[
    path('courseRegister',views.register_buy,name='CourseRegister'),
    # path('',views.product_list,name='product-list'),
    # path('<int:product_id>',views.product_details),
    # path('<slug:slug>',views.product_details,name='product-details')
]