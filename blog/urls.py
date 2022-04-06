from django.urls import path
from . import views

urlpatterns = [
    # POST urls
    path('', views.post_list, name='post_list'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
    path('<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete', views.delete_post, name='delete_post'),
    path('new', views.new_post, name='new_post'),

    # COMMENT urls
    path('<int:post_id>/comments', views.comment_list, name='comment_list' ),
    path('<int:post_id>/comments/<int:comment_id>', views.comment_detail, name='comment_detail' ),

]
