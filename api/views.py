from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Artist, Album, Track, Song
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer, SongSerializer

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Artist <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class ArtistAPIViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

# class ArtistView(APIView):
#     def get_queryset(self):
#         return Artist.objects.all()
#
#     def get(self, request):
#         query = self.get_queryset()
#         search_data = request.query_params.get('search')
#         if search_data is not None:
#             query = query.filter(title__icontains=search_data)
#         serializer = ArtistSerializer(query, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ArtistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#         context_error = {
#             "status": 400,
#             "data": serializer.data,
#             "message": "Xatolik ro'y berdi",
#         }
#         return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
#
# # API generic
# # class ArtistApiView(ListAPIView):
# #     serializer_class = ArtistSerializer
# #
# #     def get_queryset(self):
# #         queryset = Artist.objects.all()
# #         search_data = self.request.query_params.get('search')
# #         if search_data is not None:
# #             queryset = queryset.filter(title__icontains=search_data)
# #         return queryset
#
# class ArtistDetailView(APIView):
#     def get(self, request, id):
#         try:
#             artist = Artist.objects.filter(id=id)
#         except:
#             context_error = {
#                 "status": 400,
#                 "message": "Xatolik ro'y berdi"
#             }
#             return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
#         if artist:
#             serializer = ArtistSerializer(artist[0])
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         context_error = {
#             "status": 400,
#             "message": "Xatolik ro'y berdi"
#         }
#         return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, id):
#         artist = Artist.objects.get(id=id)
#         serializer = ArtistSerializer(instance=artist, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         artist = Artist.objects.get(id=id)
#         serializer = ArtistSerializer(instance=artist, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         artist = Artist.objects.get(id=id)
#         artist.delete()
#         context_error = {
#             "status": 200,
#             "message": "O'chirildi"
#         }
#         return Response(data=context_error, status=status.HTTP_204_NO_CONTENT)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Album <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# class AlbumView(APIView):
#     def get_queryset(self):
#         return Album.objects.all()
#
#     def get(self, request):
#         query = self.get_queryset()
#         search_data = request.query_params.get('search')
#         if search_data is not None:
#             query = query.filter(title__icontains=search_data)
#         serializer = AlbumSerializer(query, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = AlbumSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#         context_error = {
#             "status": 400,
#             "data": serializer.data,
#             "message": "Xatolik ro'y berdi",
#         }
#         return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
#
# # API generic
# # class AlbumApiView(ListAPIView):
# #     serializer_class = AlbumSerializer
# #
# #     def get_queryset(self):
# #         queryset = Album.objects.all()
# #         search_data = self.request.query_params.get('search')
# #         if search_data is not None:
# #             queryset = queryset.filter(title__icontains=search_data)
# #         return queryset
# class AlbumDetailView(APIView):
#     def get(self, request, id):
#         try:
#             album = Album.objects.filter(id=id)
#         except:
#             context_error = {
#                 "status": 400,
#                 "message": "Xatolik ro'y berdi"
#             }
#             return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
#         if album:
#             serializer = AlbumSerializer(album[0])
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         context_error = {
#             "status": 400,
#             "message": "Xatolik ro'y berdi"
#         }
#         return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, id):
#         album = Album.objects.get(id=id)
#         serializer = AlbumSerializer(instance=album, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         album = Album.objects.get(id=id)
#         serializer = AlbumSerializer(instance=album, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         album = Album.objects.get(id=id)
#         album.delete()
#         context_error = {
#             "status": 200,
#             "message": "O'chirildi"
#         }
#         return Response(data=context_error, status=status.HTTP_204_NO_CONTENT)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Track <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class TrackAPIViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


# class TrackView(APIView):
#     def get_queryset(self):
#         return Track.objects.all()
#
#     def get(self, request):
#         query = self.get_queryset()
#         search_data = request.query_params.get('search')
#         if search_data is not None:
#             query = query.filter(title__icontains=search_data)
#         serializer = TrackSerializer(query, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = TrackSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#         context_error = {
#             "status": 400,
#             "data": serializer.data,
#             "message": "Xatolik ro'y berdi",
#         }
#         return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
#
# # API generic
# # class TrackApiView(ListAPIView):
# #     serializer_class = TrackSerializer
# #
# #     def get_queryset(self):
# #         queryset = Track.objects.all()
# #         search_data = self.request.query_params.get('search')
# #         if search_data is not None:
# #             queryset = queryset.filter(title__icontains=search_data)
# #         return queryset
#
# class TrackDetailView(APIView):
#     def get(self, request, id):
#         try:
#             track = Track.objects.filter(id=id)
#         except:
#             context_error = {
#                 "status": 400,
#                 "message": "Xatolik ro'y berdi"
#             }
#             return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
#         if track:
#             serializer = TrackSerializer(track[0])
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         context_error = {
#             "status": 400,
#             "message": "Xatolik ro'y berdi"
#         }
#         return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, id):
#         track = Track.objects.get(id=id)
#         serializer = TrackSerializer(instance=track, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         track = Track.objects.get(id=id)
#         serializer = TrackSerializer(instance=track, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         track = Track.objects.get(id=id)
#         track.delete()
#         context_error = {
#             "status": 200,
#             "message": "O'chirildi"
#         }
#         return Response(data=context_error, status=status.HTTP_204_NO_CONTENT)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Song <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class SongAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

#
# class SongView(APIView):
#     def get_queryset(self):
#         return Song.objects.all()
#
#     def get(self, request):
#         query = self.get_queryset()
#         search_data = request.query_params.get('search')
#         if search_data is not None:
#             query = query.filter(title__icontains=search_data)
#         serializer = SongSerializer(query, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = SongSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
#         context_error = {
#             "status": 400,
#             "data": serializer.data,
#             "message": "Xatolik ro'y berdi",
#         }
#         return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)
#
# # API generic
# # class SongApiView(ListAPIView):
# #     serializer_class = SongSerializer
# #
# #     def get_queryset(self):
# #         queryset = Song.objects.all()
# #         search_data = self.request.query_params.get('search')
# #         if search_data is not None:
# #             queryset = queryset.filter(title__icontains=search_data)
# #         return queryset
#
# class SongDetailView(APIView):
#     def get(self, request, id):
#         try:
#             song = Song.objects.filter(id=id)
#         except:
#             context_error = {
#                 "status": 400,
#                 "message": "Xatolik ro'y berdi"
#             }
#             return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
#         if song:
#             serializer = SongSerializer(song[0])
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#         context_error = {
#             "status": 400,
#             "message": "Xatolik ro'y berdi"
#         }
#         return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, id):
#         song = Song.objects.get(id=id)
#         serializer = SongSerializer(instance=song, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         song = Song.objects.get(id=id)
#         serializer = SongSerializer(instance=song, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         song = Song.objects.get(id=id)
#         song.delete()
#         context_error = {
#             "status": 200,
#             "message": "O'chirildi"
#         }
#         return Response(data=context_error, status=status.HTTP_204_NO_CONTENT)