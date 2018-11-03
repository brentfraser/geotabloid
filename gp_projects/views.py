from rest_framework import generics, permissions
from .models import TrackFeature, ImageNote, Note
from .serializers import TrackFeatureSerializer, ImageNoteSerializer, NGImageNoteSerializer, NGTrackFeatureSerializer, NGNoteSerializer
from django.http import HttpResponse
from django.db.models.functions import TruncDate
from django.shortcuts import render
from django.core.serializers import serialize


# Geojson serializer
def geojsonTrackFeed(request):
    """ returns all of the trackfeatures as geoJSON
    this should be revised to allow filtering """
    return HttpResponse(serialize('geojson', TrackFeature.objects.all(), fields=('timestamp_start', 'linestring')))


class TrackList(generics.ListAPIView):
    """ a restful view of TrackFeatures by owner """
    serializer_class = TrackFeatureSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return TrackFeature.objects.filter(owner=user).defer('linestring')


class TrackDetail(generics.RetrieveAPIView):
    """ a restful detail view of a TrackFeature """
    queryset = TrackFeature.objects.all()
    serializer_class = TrackFeatureSerializer
    permission_classes = (permissions.IsAuthenticated,)


class NGTrackFeatureList(generics.ListAPIView):
    """ a restful view of TrackFeatures by user, without the coordinates """
    serializer_class = NGTrackFeatureSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return TrackFeature.objects.filter(owner=user)


class ImageNoteList(generics.ListAPIView):
    """ a restful view of ImageNotes by owner """
    serializer_class = ImageNoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ImageNote.objects.filter(owner=user)

class ImageNoteDetail(generics.RetrieveAPIView):
    """ a restful detail view of an ImageNote """
    serializer_class = ImageNoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ImageNote.objects.filter(owner=user)

class NGImageNoteList(generics.ListAPIView):
    """ a restful view of ImageNotes, without the coordinate data """
    serializer_class = NGImageNoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ImageNote.objects.filter(owner=user)


class NGImageNoteDetail(generics.RetrieveAPIView):
    """ a restful detail view of an ImageNote, without the coordinate data """
    serializer_class = NGImageNoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return ImageNote.objects.filter(owner=user)


class NGNoteList(generics.ListAPIView):
    """ a restful view of Notes by owner, without the coordinate data """
    serializer_class = NGNoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(owner=user)


class NGNoteDetail(generics.RetrieveAPIView):
    """ a restful detail view of a Note, without the coordinate data """
    serializer_class = NGNoteSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(owner=user)


def UserView(request):
    """a view of all the userdata owned by the requesting owner"""
    date_list = Note.objects.annotate(date=TruncDate('timestamp')).distinct('date').values('date')
    note_list = Note.objects.filter(owner=request.user)
    image_list = ImageNote.objects.filter(owner=request.user)
    track_list = TrackFeature.objects.filter(owner=request.user)
    context = {'date_list': date_list, 'note_list': note_list, 'image_list': image_list, 'track_list': track_list}
    return render(request, 'userview.html', context=context)
