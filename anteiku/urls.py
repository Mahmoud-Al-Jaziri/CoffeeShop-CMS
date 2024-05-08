from django.contrib import admin
from django.urls import path
from shopFront import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage,name="homePage"),
    path('register/',views.registerPage,name="registerPage"),
    path('login/',views.loginPage,name="loginPage"),
    path('logout/',views.logoutUser,name="logout"),
    path('dashboard/',views.dashboard,name="dashboardPage"),
    path('customer/<str:pk_test>',views.customer,name="customerPage"),
    path('products/',views.products,name="productsPage"),
    path('create_order/<str:pk>',views.createOrder,name="create_order"),
    path('update_order/<str:pk>',views.updateOrder,name="update_order"),
    path('delete_order/<str:pk>',views.deleteOrder,name="delete_order"),
    path('user/',views.userPage,name="user-Page"),
    path('account/',views.accountSettings,name="account"),
    path('contact/',views.contactus,name="contact"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="shopFront/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="shopFront/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="shopFront/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="shopFront/password_reset_done.html"), 
        name="password_reset_complete"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
