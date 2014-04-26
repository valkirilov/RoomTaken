from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = patterns('',
    url(r'^teachers/$', views.TeachersList.as_view()),
    url(r'^schedule/$', views.ScheduleList.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^free-rooms/', views.FreeRooms.as_view())
)

urlpatterns = format_suffix_patterns(urlpatterns)