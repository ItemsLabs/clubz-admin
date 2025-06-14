from django.urls import path, include, re_path

from core.views import index, UpdateUserAvatarView, terms, RevenueCatSyncView, force, uritest, datafeedsimtest
from core.views_inner import process_simulations

urlpatterns = [
    path('api/', include([
        path('users/', include([
            path('profile/', include([
                path('avatar/', UpdateUserAvatarView.as_view()),
            ])),
        ])),
        re_path('revenuecat/sync/?', RevenueCatSyncView.as_view()),
    ])),
    path('inner/', include([
        re_path('process_simulations/?', process_simulations),
        path("__force__", force),
        path("__uritest__", uritest),
        path("__datafeedsimtest__", datafeedsimtest)
    ])),
    path('terms.html', terms),
    path('terms', terms),
    path('', index),
]
