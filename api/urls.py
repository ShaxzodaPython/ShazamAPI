from .views import ArtistAPIViewSet, AlbumAPIViewSet, TrackAPIViewSet, SongAPIViewSet
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path, include


schema_view = get_schema_view(
    openapi.Info(
        title="Shazam API DOCS",
        default_version='v1',
        description="API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'artist', ArtistAPIViewSet, basename='artist')
router.register(r'album', ArtistAPIViewSet, basename='album')
router.register(r'track', TrackAPIViewSet, basename='track')
router.register(r'song', SongAPIViewSet, basename='song')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
    # path('artist/', ArtistView.as_view(), name='artist'),
    # path('artist/<int:id>/', ArtistDetailView.as_view(), name='artist-detail'),
    # path('album/', AlbumView.as_view(), name='album'),
    # path('album/<int:id>/', AlbumDetailView.as_view(), name='album-detail'),
    # path('track/', TrackView.as_view(), name='track'),
    # path('track/<int:id>/', TrackDetailView.as_view(), name='track-detail'),
    # path('song/', SongView.as_view(), name='song'),
    # path('song/<int:id>/', SongDetailView.as_view(), name='song-detail'),
]

urlpatterns += [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
