from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

import core.views

urlpatterns = [
    path("posts/", core.views.PostList.as_view()),
    path("posts/create/", core.views.CreatePost.as_view()),
    path("posts/post=<int:pk>/", core.views.UpvoteView.as_view()),
    path("users/create/", core.views.SignUp.as_view()),
    path("users/get_token/", obtain_auth_token, name="api_token_auth"),
]
