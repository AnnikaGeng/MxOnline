# coding: utf-8
__author__ = 'annika'
__date__ = '2018/10/14 10:55 AM'

import xadmin

from .models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_field = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentAdmin(object):
    list_display = ['course__name', 'comments', 'add_time']
    search_field = ['course__name', 'comments']
    list_filter = ['course__name', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['fav_id', 'fav_type', 'add_time']
    search_field = ['fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'has_read', 'message']
    search_field = ['user', 'has_read', 'message']
    list_filter = ['user', 'has_read', 'message']


class UserCourseAdmin(object):
    list_display = [ 'course', 'add_time']
    search_field = ['course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)