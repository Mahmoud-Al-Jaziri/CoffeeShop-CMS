"""
URL configuration for anteiku project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shopFront import views

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

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
