from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('address', views.CustomerAddressViewset)
router.register('productrating', views.ProductRatingViewset)

urlpatterns = [
    # Vendors
    path('vendors/',  views.VendorList.as_view()),
    path('vendor/<int:pk>/',  views.vendorDetail.as_view()),
    # Products
    path('products/',  views.ProductList.as_view()),
    path('products/<str:tag>',  views.TagProductList.as_view()),
    path('product/<int:pk>/',  views.ProductDetail.as_view()),
    path('related-products/<int:pk>/',  views.RelatedProductList.as_view()),
    # Products Categories
    path('categories/',  views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    # Customers
    path('customers/',  views.CustomerList.as_view()),
    path('customer/<int:pk>/',  views.CustomerDetail.as_view()),
    path('customer-update/<int:pk>/',  views.CustomerUpdate.as_view()),
    path('user/<int:pk>/',  views.UserDetail.as_view()),
    path('customer/login/',  views.customer_login, name='customer_login'),
    path('customer/register/',  views.customer_register, name='customer_register'),
    path('customer/<int:pk>/address/',  views.CustomerAddressList.as_view()),
    #Order
    path('orders/',  views.OrderList.as_view()),
    path('order/<int:pk>/',  views.OrderDetail.as_view()),
    path('orderitems/',  views.OrderItemList.as_view()),
    path('customer/<int:pk>/orderitems/',  views.CustomerOrderItemList.as_view()),
    path('update-order-status/<int:order_id>',  views.update_order_status, name='update_order_status'),
    path('update_product_download_count/<int:product_id>',  views.update_product_download_count, name='update_product_download_count'),
    #Wishlist
    path('wishlist/',  views.WishList.as_view()),
    path('check-in-wishlist/',  views.check_in_wishlist, name='check_in_wishlist'),
    path('customer/<int:pk>/wishlistitems/',  views.CustomerWishlistItems.as_view()),
    path('customer/<int:pk>/removewishlistitems/<int:id>',  views.CustomerRemoveWishlistItems.as_view()),
    
    
]

urlpatterns+=router.urls