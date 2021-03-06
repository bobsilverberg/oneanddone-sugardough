# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import urllib
from warnings import warn

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect
from django.utils import timezone
from django.utils.encoding import smart_str

import tower
from tower import ugettext as _

from oneanddone.base import urlresolvers
from oneanddone.base.helpers import urlparams


class ClosedTaskNotificationMiddleware(object):
    """
    Add messages to the request if required.
    """
    def process_request(self, request):
        if request.user.is_authenticated():
            for attempt in request.user.attempts_requiring_notification:
                messages.warning(request,
                                 _('The task that you were working on, "%s", has expired or become invalid '
                                   'and therefore has been closed.' % attempt.task.name),
                                 extra_tags='modal-message')
                attempt.requires_notification = False
                attempt.save()


class TimezoneMiddleware(object):
    """
    Set the current timezone for all requests to be UTC.

    Will handle more complex timezone logic once we have more formal
    timezone support in the app.
    """
    def process_request(self, request):
        timezone.activate(timezone.utc)


class LocaleURLMiddleware(object):
    """
    1. Search for the locale.
    2. Save it in the request.
    3. Strip them from the URL.
    """

    def __init__(self):
        if not settings.USE_I18N or not settings.USE_L10N:
            warn("USE_I18N or USE_L10N is False but LocaleURLMiddleware is "
                 "loaded. Consider removing fjord.base.middleware."
                 "LocaleURLMiddleware from your MIDDLEWARE_CLASSES setting.")

        self.exempt_urls = getattr(settings, 'FF_EXEMPT_LANG_PARAM_URLS', ())

    def _is_lang_change(self, request):
        """Return True if the lang param is present and URL isn't exempt."""
        if 'lang' not in request.GET:
            return False

        return not any(request.path.endswith(url) for url in self.exempt_urls)

    def process_request(self, request):
        prefixer = urlresolvers.Prefixer(request)
        urlresolvers.set_url_prefix(prefixer)
        full_path = prefixer.fix(prefixer.shortened_path)

        if self._is_lang_change(request):
            # Blank out the locale so that we can set a new one. Remove lang
            # from the query params so we don't have an infinite loop.
            prefixer.locale = ''
            new_path = prefixer.fix(prefixer.shortened_path)
            query = dict((smart_str(k), request.GET[k]) for k in request.GET)
            query.pop('lang')
            return HttpResponsePermanentRedirect(urlparams(new_path, **query))

        if full_path != request.path:
            query_string = request.META.get('QUERY_STRING', '')
            full_path = urllib.quote(full_path.encode('utf-8'))

            if query_string:
                full_path = '%s?%s' % (full_path, query_string)

            response = HttpResponsePermanentRedirect(full_path)

            # Vary on Accept-Language if we changed the locale
            old_locale = prefixer.locale
            new_locale, _ = urlresolvers.split_path(full_path)
            if old_locale != new_locale:
                response['Vary'] = 'Accept-Language'

            return response

        request.path_info = '/' + prefixer.shortened_path
        request.locale = prefixer.locale
        tower.activate(prefixer.locale)
