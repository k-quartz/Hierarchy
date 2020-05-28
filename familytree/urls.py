from django.urls import path
from .views import CreateMemberView
from . import views

urlpatterns = [
    path('', views.index, name="ft-index"),
    path('member/', views.DisplayMember, name="display-member"),
    path('member/<curpg>', views.DisplayMemberP, name="display-memberp"),
    path('member/add/', CreateMemberView.as_view(), name="new-member"),
    path('member/update/<id>/',
         views.updateMemberView, name="update-member"),
    path('member/search/',
         views.displayModalView, name="display_modal"),
    path('success/', views.success, name="ft-success"),
    path('member/addfamily/<int:mid>/<int:newid>/<int:reltypeid>',
         views.addFamily, name='add-family'),

]
