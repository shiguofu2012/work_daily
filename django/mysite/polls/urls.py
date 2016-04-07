from django.conf.urls import patterns, url

urlpatterns = patterns('polls.views',
        url(r'^hello$', 'hello'),
        url(r'^test$', 'test'),
        url(r'^download$', 'download')
        )
