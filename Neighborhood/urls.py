from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('hood', views.home, name='hood'),
    path('user/', views.profile, name='profile'),
    path('search/', views.search_results, name='search_results'),  
    path('neighbourhood/<neighborhood_id>',views.neighborhood,name='neighbourhood'),
    path('joinhood/<neighborhood_id>',views.join_hood,name="joinhood"),
    path('leavehood/<neighborhood_id>',views.leave_hood,name="leavehood")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)