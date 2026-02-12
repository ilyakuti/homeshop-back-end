from django.urls import path
from .views import homepage, detailpage, loginpage, logoutpage, sign_up

urlpatterns = [
    path ('', homepage, name="homepage_url"),
    path ("detail/<int:pk>/", detailpage, name="detail_url"),
    path ("authenticate/", loginpage, name="login_url"),
    path ("logout/", logoutpage, name="logout_url"),
    path ("sign-up/", sign_up, name="sign_up_url"),
]