from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . serializers import LanguageSerializer
from . models import Language


# Create your views here.
class LanguageAPIView(APIView):
    permission_classes = ()

    def get(self, request):
        languages = Language.objects.all()
        languages_serializer = LanguageSerializer(languages, many=True)
        return Response(languages_serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([])
def language_api_view(request):

    # list
    if request.method == 'GET':
        languages = Language.objects.all()
        language_serializer = LanguageSerializer(languages, many=True)
        return Response(language_serializer.data)

    # create
    elif request.method == 'POST':
        language_serializer = LanguageSerializer(data=request.data)

        # validation
        if language_serializer.is_valid():
            language_serializer.save()
            return Response(language_serializer.data, status=status.HTTP_201_CREATED)

        return Response(language_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([])
def language_detail_api_view(request, pk=None):
    # queryset
    language = Language.objects.filter(id=pk).first()

    # validation
    if not language:
        return Response({'message': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    # retrieve
    if request.method == 'GET':
        language_serializer = LanguageSerializer(language)
        return Response(language_serializer.data)

    # update
    elif request.method == 'PUT':
        language_serializer = LanguageSerializer(language, data=request.data)

        # validation
        if language_serializer.is_valid():
            language_serializer.save()
            return Response(language_serializer.data)

        return Response(language_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    elif request.method == 'DELETE':
        language.delete()
        return Response({'message': 'Deleted!'})
