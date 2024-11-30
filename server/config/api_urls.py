from django.urls import path, include

from apps.pockets.routers import pockets_router

urlpatterns = [
    path('auth/', include('apps.users.urls.auth')),
    path('users/', include('apps.users.urls.users_urls')),
]
