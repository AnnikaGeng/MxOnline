# coding: utf-8
__author__ = 'annika'
__date__ = '2018/10/23 12:28 PM'


from django.conf.urls import url, include
from .views import OrgView, AddUserAskView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask")
]