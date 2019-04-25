from django.urls import path
from api.music.views import songViews, genresView
from api.music.class_based import SongClassBased

urlpatterns = [

    #songs URI
    #path('songs/', songViews.song_request_base),
    path('songs/', SongClassBased.song_request_base.as_view()),
    path('song/<int:pk>', songViews.song_request_full),

    #genres URI
    path('genres/', genresView.genres_request_base),
    path('genres/<int:pk>', genresView.genres_request_full),
]