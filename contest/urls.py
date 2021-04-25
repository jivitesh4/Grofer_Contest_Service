from django.urls import path
from . import views


urlpatterns = [
    path('generateticket', views.GroferContest.as_view({"post":"generate_ticket"}) ),
    path('takepart', views.GroferContest.as_view({"post":"take_part"})),
    path('upcomingevent', views.GroferContest.as_view({"get":"upcoming_event"})),
    path('lastweekwinners', views.GroferContest.as_view({"get":"last_week_winners"}))
   
]