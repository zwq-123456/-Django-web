var videoEreeaStatic=false
var videoEditArea=$('#video_edit_area')
$('#open_add_video_btn').click(function () {
    if (!videoEreeaStatic){
        videoEditArea.show();
        videoEreeaStatic=true;
    } else{
        videoEditArea.hide();
        videoEreeaStatic=false;
    }
});