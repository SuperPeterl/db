from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name = 'posApp/login.html',redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
    path('category', views.category, name="category-page"),
    path('manage_category', views.manage_category, name="manage_category-page"),
    path('save_category', views.save_category, name="save-category-page"),
    path('delete_category', views.delete_category, name="delete-category"),
    path('products', views.products, name="product-page"),
    path('manage_products', views.manage_products, name="manage_products-page"),
    path('test', views.test, name="test-page"),
    path('save_product', views.save_product, name="save-product-page"),
    path('delete_product', views.delete_product, name="delete-product"),
    path('pos', views.pos, name="pos-page"),
    path('checkout-modal', views.checkout_modal, name="checkout-modal"),
    path('save-pos', views.save_pos, name="save-pos"),
    path('sales', views.salesList, name="sales-page"),
    path('receipt', views.receipt, name="receipt-modal"),
    path('delete_sale', views.delete_sale, name="delete-sale"),
    #path('employees', views.employees, name="employee-page"),
    #path('manage_employees', views.manage_employees, name="manage_employees-page"),
    #path('save_employee', views.save_employee, name="save-employee-page"),
    #path('delete_employee', views.delete_employee, name="delete-employee"),
    #path('view_employee', views.view_employee, name="view-employee-page"),
    path('bill',views.bill,name = 'bill'),
    path('createbill',views.createbill,name= 'createbill'),
    path('delete_bill', views.delete_bill, name="delete_bill"),
    path('manage_bill',views.manage_bill,name= 'manage_bill'),
    path('manage_bill_addProduct',views.manage_bill_addProduct,name= 'manage_bill_addProduct'),
    path('manage_bill_deleteProduct',views.manage_bill_deleteProduct,name= 'manage_bill_deleteProduct'),
    path('manage_bill_checkout',views.manage_bill_checkout,name= 'manage_bill_checkout'),
    path('material', views.material, name="material"),
    path('manage_material', views.manage_material, name="manage_material"),
    path('save_material', views.save_material, name="save_material"),
    path('delete_material', views.delete_material, name="delete_material"),
    path('manage_product_material', views.manage_product_material, name="manage_product_material"),
    path('link_product_material', views.link_product_material, name="link_product_material"),
    path('unlink_product_material', views.unlink_product_material, name="unlink_product_material")
]