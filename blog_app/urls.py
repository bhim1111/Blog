
from django.urls import path
from blog_app import views

urlpatterns = [
    path("",views.post_list, name="post-list"),
    path("post_detail/<int:pk>/", views.post_detail, name="post-detail"),
    path("draft_list/", views.draft_list, name="draft-list"),
    path("draft_detail/<int:pk>/", views.draft_detail, name="draft-detail"),
]
