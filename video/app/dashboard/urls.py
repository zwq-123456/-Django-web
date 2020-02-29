from django.urls import path
from .views.base import Index
from .views.video import ExternaVideo,videoSub,VideoStarView,starDelect
from .views.auth import Login,AdminManger,Logout,UpdateAdminStatus
urlpatterns = [
    path('',Index.as_view(),name='dashboard_index'),
    path('Login',Login.as_view(),name='dashboard_Login'),
    path('admin/Manger',AdminManger.as_view(),name='AdminManger'),
    path('logout',Logout.as_view(),name='logout'),
    path('admin/manger/update/status',UpdateAdminStatus.as_view(),name='admin_update_manger'),
    path('video/externa',ExternaVideo.as_view(),name='externa_video'),
    path('video/videosub/<int:video_id>',videoSub.as_view(),name='video_sub'),
    path('video/star',VideoStarView.as_view(),name='video_star'),
    path('video/star/delete/<int:star_id>/<int:video_id>',starDelect.as_view(),name='Del')
]