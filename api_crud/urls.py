
from django.contrib import admin
from django.urls import include, path

# urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/contest/', include('contest.urls')),
]