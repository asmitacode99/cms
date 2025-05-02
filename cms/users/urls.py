from django.urls import path
from .views import user_detail_view
from .views import user_redirect_view
from .views import user_update_view
from cms.users.api.v1.views import UserListAPIView
# from cms.users.api.v1.auths import UserRegisterationView, UserLoginTokenView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cms.users.api.v1.auths import UserRegisterationView, UserLoginTokenView



app_name = "users"
urlpatterns = [
    
    path("register/", UserRegisterationView.as_view(), name="register"),
    path("login/", UserLoginTokenView.as_view(), name="login"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
   
    

]
