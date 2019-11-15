from django.urls import path
from . views import(
    view_wristwatch,
    detail_wristwatch_view,
    view_shoe,
    detail_shoe_view,
)

app_name = 'yomex' 


urlpatterns= [
    path('watch/',view_wristwatch,name='watch'),
    path('watch/<slug>/',detail_wristwatch_view, name='detail_watch'), 
    path('shoes/',view_shoe,name='shoes'),
    path('shoe/<slug>/',detail_shoe_view, name='detail_shoe'), 
 ]