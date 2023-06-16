from cubeseed.userauth import views
from rest_framework import routers

def register_routes(router):
    router.register(r'userauth/register', views.RegisterUserView, basename='register')
    router.register(r'userauth/users', views.UserViewSet)
    router.register(r'userauth/groups', views.GroupViewSet)
    return router

urlpatterns = register_routes(routers.DefaultRouter()).urls
