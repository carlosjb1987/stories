from django.urls import path
from storyapp.stories import views

urlpatterns = [
    path('', views.list_stories, name='list_stories'),
    path('story/<int:story_id>/', views.detail_story, name='story'),
    path('story/<int:story_id>/submit/', views.submit_answers, name='submit_answers'),
]
