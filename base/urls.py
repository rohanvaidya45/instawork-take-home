from django.urls import path
from .views import MemberList, MemberDetail, MemberCreate, MemberUpdate, MemberDelete

urlpatterns = [
    path('', MemberList.as_view(), name='members'),
    path('member/<int:pk>/', MemberDetail.as_view(), name='member'),
    path('member-create/', MemberCreate.as_view(), name='member-create'),
    path('member-update/<int:pk>/', MemberUpdate.as_view(), name='member-update'),
    path('member-delete/<int:pk>/', MemberDelete.as_view(), name='member-delete'),
]