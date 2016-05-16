#!coding:utf-8
from django.conf.urls import patterns, url
from data_base import views

urlpatterns = [#patterns('',
#        url(r'^$', views.show, name='show'),
#        url(r'^edit/$', views.edit, name='edit'),
        url(r'^pkg/$', views.pkg_list, name='pkg_list'),   # 一覧
        url(r'^pkg/add/$', views.pkg_edit, name='pkg_add'),  # 登録
        url(r'^pkg/mod/(?P<pkg_id>\d+)/$', views.pkg_edit, name='pkg_mod'),  # 修正
        url(r'^pkg/del/(?P<pkg_id>\d+)/$', views.pkg_del, name='pkg_del'),   # 削除

        # 感想
        url(r'^proglam/(?P<pkg_id>\d+)/$', views.ProglamList.as_view(), name='proglam_list'),  # 一覧
        url(r'^proglam/add/(?P<pkg_id>\d+)/$', views.proglam_edit, name='proglam_add'),        # 登録
        url(r'^proglam/mod/(?P<pkg_id>\d+)/(?P<proglam_id>\d+)/$', views.proglam_edit, name='proglam_mod'),  # 修正
        url(r'^proglam/del/(?P<pkg_id>\d+)/(?P<proglam_id>\d+)/$', views.proglam_del, name='proglam_del'),   # 削除

        url(r'^function/(?P<proglam_id>\d+)/$', views.FunctionList.as_view(), name='function_list'),  # 一覧
        url(r'^function/add/(?P<proglam_id>\d+)/$', views.function_edit, name='function_add'),        # 登録
        url(r'^function/mod/(?P<proglam_id>\d+)/(?P<function_id>\d+)/$', views.function_edit, name='function_mod'),  # 修正
        url(r'^function/del/(?P<proglam_id>\d+)/(?P<function_id>\d+)/$', views.function_del, name='function_del'),   # 削除
        url(r'^function/view/(?P<function_id>\d+)/$', views.function_view, name='function_view'),
]#)
