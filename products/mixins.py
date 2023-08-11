from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class CachedListViewMixin:
    cache_timeout = 60 * 1  # Cache for 1 minutes

    @method_decorator(cache_page(cache_timeout))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
