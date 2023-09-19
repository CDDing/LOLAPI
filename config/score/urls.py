from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
app_name='score'

urlpatterns = [
    path('score_view',views.score_view,name='score_view'),
    path('search_result',views.search_result,name='search_result'),
    path('summoner_search',views.summoner_search,name='summoner_search'),
    path('summoner_result',views.summoner_result,name='summoner_result'),
    path('stat_choose',views.stat_choose,name='stat_choose'),
    path('stat_result',views.stat_result,name='stat_result'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)