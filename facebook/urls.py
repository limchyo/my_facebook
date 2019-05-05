from django.urls import path
from .views import (
    play, play2, profile, event, fail, help, warn, newsfeed, detail_feed,
    pages, new_feed, remove_feed, edit_feed, new_page, edit_page, remove_page,
    remove_comment,
)
urlpatterns = [
    path('play/', play, name="play"),
    path('play2/', play2, name="play2"),
    path('limchyo/profile/', profile, name="profile"),
    path('event/', event, name="event"),
    path('fail/', fail, name="fail"),
    path('help/', help, name='help'),
    path('warn/', warn, name='warn'),

    path('', newsfeed, name="newsfeed"),
    path('feed/<pk>/', detail_feed, name="detail_feed"),
    path('feed/<pk>/edit', edit_feed, name="edit_feed"),
    path('feed/<pk>/remove', remove_feed, name="remove_feed"),
    path('new/', new_feed, name="new_feed"),

    path('pages/', pages, name="pages"),
    path('pages/new', new_page, name="new_page"),
    path('pages/<pk>/edit', edit_page, name="edit_page"),
    path('pages/<pk>/remove', remove_page, name="remove_page"),

    path('comment/<pk>/remove', remove_comment, name="remove_comment"),
]
