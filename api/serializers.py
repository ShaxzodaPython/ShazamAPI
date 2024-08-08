from rest_framework import serializers

from .models import Artist, Album, Track, Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name')


class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    class Meta:
        model = Album
        fields = ('title', 'artist')

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    album = AlbumSerializer(read_only=True)
    track = TrackSerializer(read_only=True)
    class Meta:
        model = Song
        fields = ('title', 'image', 'album', 'track', 'artist')
