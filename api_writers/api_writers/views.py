import json

from rest_framework.permissions import IsAuthenticated
from rest_framework_proxy.views import ProxyView

from django.conf import settings


class BooksAPIProxyView(ProxyView):
    permission_classes = (IsAuthenticated,)
    proxy_host = settings.MICROSERVICES.get('BooksMicroservice')
    source = "v1/books/"

    def get_headers(self, request):
        headers = super(BooksAPIProxyView, self).get_headers(request)

        if request.user.is_authenticated:
            user = {
                'id': request.user.id,
                'username': request.user.username,
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'is_active': request.user.is_active,
                'is_staff': request.user.is_staff,
                'is_superuser': request.user.is_superuser
            }
            headers['Authorization'] = json.dumps(user)
        return headers
