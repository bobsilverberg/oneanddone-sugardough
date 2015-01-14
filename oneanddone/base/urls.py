# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from django.conf import settings
from django.conf.urls import patterns, url

from oneanddone.base import views


urlpatterns = patterns('',
    (r'^(?P<path>contribute\.json)$', 'django.views.static.serve',
     {'document_root': settings.BASE_DIR}),
    url(r'^$', views.HomeView.as_view(), name='base.home'),
)
