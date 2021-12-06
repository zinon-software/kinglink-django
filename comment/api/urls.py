from django.urls import path
from .views import CommentListAPIView, PUTAndDeleteCommentAPIView


urlpatterns = [
    path('<int:post_id>', CommentListAPIView.as_view(), name='comment_list'),
    path('id/<int:comment_id>', PUTAndDeleteCommentAPIView.as_view(), name='comment_PUT_And_Delete'),
]