import inspect
import logging
import time
import os as os_fn

from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.deprecation import MiddlewareMixin
from django_statsd.clients import statsd
from django_statsd.middleware import is_authenticated

logger = logging.getLogger("healthz")


class HealthCheckMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if request.method == "GET":
            if request.path == "/readiness":
                return self.readiness(request)
            elif request.path == "/healthz":
                return self.healthz(request)
        return self.get_response(request)

    def healthz(self, request):
        """
        Returns that the server is alive.
        """
        return HttpResponse("OK")

    def readiness(self, request):
        # # Connect to each database and do a generic standard SQL query
        # # that doesn't write any data and doesn't depend on any tables
        # # being present.
        # try:
        #     from django.db import connections
        #     for name in connections:
        #         cursor = connections[name].cursor()
        #         cursor.execute("SELECT 1;")
        #         row = cursor.fetchone()
        #         if row is None:
        #             return HttpResponseServerError("db: invalid response")
        # except Exception as e:
        #     logger.exception(e)
        #     return HttpResponseServerError("db: cannot connect to database.")
        #
        # # Call get_stats() to connect to each memcached instance and get it's stats.
        # # This can effectively check if each is online.
        # try:
        #     from django.core.cache import caches
        #     from django.core.cache.backends.memcached import BaseMemcachedCache
        #     for cache in caches.all():
        #         if isinstance(cache, BaseMemcachedCache):
        #             stats = cache._cache.get_stats()
        #             if len(stats) != len(cache._servers):
        #                 return HttpResponseServerError("cache: cannot connect to cache.")
        # except Exception as e:
        #     logger.exception(e)
        #     return HttpResponseServerError("cache: cannot connect to cache.")

        return HttpResponse("OK")


class MetricMiddleware(MiddlewareMixin):
    """statsd's timing data per view."""

    def process_view(self, request, view_func, view_args, view_kwargs):
        view = view_func
        if not inspect.isfunction(view_func):
            view = view.__class__
        try:
            view_name = view.__name__
            # for class based view try to find real function name under class
            if hasattr(view_func, 'actions'):
                func_name = view_func.actions.get(request.method.lower(), None)
                if func_name is not None:
                    view_name = '%s.%s' % (view_name, func_name)

            request._view_module = view.__module__
            request._view_name = view_name
            request._start_time = time.time()
        except AttributeError:
            pass

    def process_response(self, request, response):
        self._record_metrics(request, response.status_code)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            status_code = 404
        else:
            status_code = 500
        self._record_metrics(request, status_code)

    @staticmethod
    def metric_name(tpl, **kwargs):
        # add `env` and `os` tags to template and format
        return (tpl + ',env={env},os={os},lang=python').format(**kwargs)

    def _record_metrics(self, request, status_code):
        os = '-'
        if hasattr(request, 'ios_agent') and request.ios_agent:
            os = 'ios'
        elif hasattr(request, 'android_agent') and request.android_agent:
            os = 'android'
        code_group = int(status_code / 100)
        data = dict(status_code=status_code, code_group=code_group,
                    env=os_fn.getenv('DJANGO_SETTINGS_MODULE'), os=os, )

        # log exact status code (e.g. 200, 400)
        statsd.incr(self.metric_name('response.{status_code}', **data))
        # log group of response (e.g. 2xx, 4xx)
        statsd.incr(self.metric_name('response.{code_group}xx', **data))
        if hasattr(request, 'user') and is_authenticated(request.user):
            statsd.incr(self.metric_name('response.auth.{status_code}', **data))

        if hasattr(request, '_start_time'):
            data.update(
                module=request._view_module,
                name=request._view_name,
                method=request.method,
            )
            ms = int((time.time() - request._start_time) * 1000)

            statsd.timing(self.metric_name('response.timing', **data), ms)
            statsd.timing(self.metric_name('response.{status_code}.timing', **data), ms)
            statsd.timing(self.metric_name('response.{code_group}xx.timing', **data), ms)
            statsd.timing(self.metric_name('view.{module}.{name}.{method}.timing', **data), ms)
            statsd.incr(self.metric_name('view.{module}.{name}.{method}.count', **data))
            statsd.incr(self.metric_name('view.{module}.{name}.{method}.{status_code}.count', **data))

            # cache hit/miss data
            if hasattr(request, '_cache_hit'):
                statsd.incr(self.metric_name('view.{module}.{name}.{method}.cache_count', **data))
                statsd.incr(self.metric_name('response.cache_count', **data))
            else:
                statsd.incr(self.metric_name('view.{module}.{name}.{method}.non_cache_count', **data))
                statsd.incr(self.metric_name('response.non_cache_count', **data))
