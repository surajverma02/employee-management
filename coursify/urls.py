
from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home_page"),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),
    path('signup/', signup_page, name="signup_page"),
    path('register/', Employee_Data, name="Employee_Data"),
    path('delete/<int:id>/', Delete_data, name="Delete_data"),
    path('update/<int:id>/', Update_data, name="Update_data"),
    path('updated/<int:id>/', updated, name="updated"),
]
