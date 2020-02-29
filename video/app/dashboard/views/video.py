from app.model.video import VideoType, FromType,NationalityType,Video,VideoSub,IdentTityType,VideoStar
from django.views.generic import View
from django.shortcuts import reverse,redirect
from app.libs.base_render import render_to_response
from app.utils.permission import dashboard_auth
from app.utils.common import check_and_get_video_tpye

class ExternaVideo(View):
    TEMPLATE='dashboard/auth/externa_video.html'
    @dashboard_auth
    def get(self,request ):
        error=request.GET.get('error','')
        data={'error':error}
        videos=Video.objects.exclude(from_to=FromType.custom.value)
        data['videos']=videos
        return render_to_response(request,self.TEMPLATE,data=data)
    def post(self,request):
        name=request.POST.get('name')
        image=request.POST.get('image')
        info=request.POST.get('info')
        video_type=request.POST.get('video_type')
        nationality=request.POST.get('nationality')
        from_to=request.POST.get('from_to')
        if not all([name, image, info, video_type, nationality, from_to]):
            return redirect('{}?error={}'.format(reverse('externa_video'), '缺少必要字段'))
        result = check_and_get_video_tpye(VideoType, video_type, '错误的视频类型')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('externa_video'), result['msg']))

        result = check_and_get_video_tpye(FromType, from_to, '非法的视频来源')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('externa_video'), result['msg']))

        result = check_and_get_video_tpye(NationalityType, nationality, '非法的国籍来源')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(reverse('externa_video'), result['msg']))
        Video.objects.create(
            name=name,
            image=image,
            info=info,
            video_type=video_type,
            nationality=nationality,
            from_to=from_to

        )
        return redirect(reverse('externa_video'))
class videoSub(View):
    TEMPLATE = 'dashboard/auth/video_sub.html'
    @dashboard_auth
    def get(self,request,video_id):
        data = {}
        video=Video.objects.get(pk=video_id)
        error=request.GET.get('error','')
        data['error']=error
        data['video']=video
        return render_to_response(request,self.TEMPLATE,data=data)
    def post(self,request,video_id):
        url=request.POST.get('url')
        video= Video.objects.get(pk=video_id)
        length=video.video_sub.count()
        VideoSub.objects.create( url=url,video=video,number=length+1)
        return redirect(reverse('video_sub',kwargs={'video_id':video_id}))
class VideoStarView(View):
    def post(self,request):
        name=request.POST.get('name')
        identity= request.POST.get('identity')
        video_id=request.POST.get('video_id')
        path_for=('{}'.format(redirect(reverse('video_sub', kwargs={'video_id': video_id}))))
        if not all([name,identity,video_id]):
            return ('{}?error={}'.format(path_for,'输入的内容有误'))
        result = check_and_get_video_tpye(IdentTityType, identity, '非法的身份')
        if result.get('code') != 0:
            return redirect('{}?error={}'.format(path_for, result['msg']))
        video = Video.objects.get(pk=video_id)
        VideoStar.objects.create(
            video=video,
            identity=identity,
            name=name
            )
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))
class starDelect(View):
    def get(self,request,star_id,video_id):
        VideoStar.objects.filter(id=star_id).delete()
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))




