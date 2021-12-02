from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from django.conf.urls import url
from frontPage.consumer import ChatConsumer


websocket_urlPattern = [
    url(r'^(?P<username>[\w.@+-]+)', ChatConsumer),
]
application = ProtocolTypeRouter({
    'websockets': AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(websocket_urlPattern)))
})