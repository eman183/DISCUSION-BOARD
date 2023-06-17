from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("boards/<int:board_id>",views.board_topics,name="board_topics"),
    path("boards/<int:board_id>/new",views.new_topic,name="new_topic")


]