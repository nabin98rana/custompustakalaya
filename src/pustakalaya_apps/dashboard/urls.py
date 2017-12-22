from django.conf.urls import url
from . import views
from . import collection_views

urlpatterns = [

    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^profile/$', views.profile, name="profile"),
    # /dashboard/profile/edit/
    url(r'^profile/edit/(?P<pk>\d+)/$', views.ProfileEdit.as_view(), name="profile_edit"),
    # dashboard/add/document/
    url(r'^document/add/$', views.AddDocumentView.as_view(), name="document_add"),
    # /dashboard/document/update/
    url(r'^document/update/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/', views.UpdateDocumentView.as_view(), name="document_update"),
    # /dashboard/document/delete/
    url(r'^document/delete/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/', views.DeleteDocumentView.as_view(), name="document_delete"),

    # /dashboard/audio/add/
    url(r'^audio/add/$', views.AddAudioView.as_view(), name="audio_add"),
    # /dashboard/audio/update/
    url(r'^audio/update/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/', views.UpdateAudioView.as_view(), name="audio_update"),
    url(r'^audio/delete/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/',views.DeleteAudioView.as_view(), name="audio_delete"),

    # /dashboard/video/add/
    url(r'^video/add/$', views.AddVideoView.as_view(), name="video_add"),
    # /dashboard/video/update/
    url(r'^video/update/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/', views.UpdateVideoView.as_view(), name="video_update"),
    url(r'^video/delete/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/',views.DeleteVideoView.as_view(), name="video_delete"),

    url(r'^collection/add/$', collection_views.AddCollection.as_view(), name="document_add"),
    #/dashboard/collections/
    url(r'^collection/add/$', collection_views.AddCollection.as_view(), name="collection_list"),
]
