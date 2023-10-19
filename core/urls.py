# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet
from authors.views import AuthorViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'authors', AuthorViewSet, basename='author')

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for Your Project",
        contact=openapi.Contact(email="your_email@example.com"),
    ),
    public=True,
)

urlpatterns = [
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
