from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer, FileUpdateSerializer
from django.http import Http404
from rest_framework.exceptions import PermissionDenied, NotFound
from users.models import CustomUser 
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.conf import settings
import os

import logging

logger = logging.getLogger(__name__)

class FileUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        files = request.FILES.getlist('files')
        responses = []
        for file in files:
            file_path = os.path.join(settings.MEDIA_ROOT, file.name)
            try:
                with open(file_path, 'wb') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                responses.append({
                    'success': True,
                    'message': 'Success',
                    'name': file.name,
                    'url': f"{request.build_absolute_uri(settings.MEDIA_URL)}{file.name}",
                })
            except Exception as e:
                error_message = f"Error saving file: {file.name}. Error: {str(e)}"
                logger.error(error_message)
                responses.append({
                    'success': False,
                    'message': 'File not loaded',
                    'name': file.name
                })
        return Response(responses, status=status.HTTP_200_OK)


class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            file = File.objects.get(file_id=self.kwargs['file_id'])
            if file.owner != self.request.user and self.request.user not in file.shared_with.all():
                raise PermissionDenied({'message': 'Forbidden for you'})
            return file
        except File.DoesNotExist:
            raise NotFound({'message': 'Not found'})

    def delete(self, request, *args, **kwargs):
        file = self.get_object()
        if file.owner != request.user:
            raise PermissionDenied({'message': 'Forbidden for you'})
        file.delete()
        return Response({'success': True, 'message': 'File already deleted'}, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        file = self.get_object()
        if file.owner != request.user:
            raise PermissionDenied({'message': 'Forbidden for you'})
        serializer = FileUpdateSerializer(file, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'message': 'Renamed'}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class AddAccessView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        file_id = self.kwargs.get('file_id')
        email = request.data.get('email')
        try:
            file = File.objects.get(file_id=file_id)
            if file.owner != request.user:
                raise PermissionDenied({'message': 'Forbidden for you'})
            user = CustomUser.objects.get(email=email)
            file.shared_with.add(user)
            file.save()
            accesses = [{'fullname': f'{u.first_name} {u.last_name}', 'email': u.email, 'type': 'author' if u == file.owner else 'co-author'} for u in [file.owner] + list(file.shared_with.all())]
            return Response(accesses, status=status.HTTP_200_OK)
        except File.DoesNotExist:
            raise NotFound({'message': 'Not found'})
        except CustomUser.DoesNotExist:
            return Response({'message': {'email': ['User not found']}}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class RemoveAccessView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        file_id = self.kwargs.get('file_id')
        email = request.data.get('email')
        try:
            file = File.objects.get(file_id=file_id)
            if file.owner != request.user:
                raise PermissionDenied({'message': 'Forbidden for you'})
            user = CustomUser.objects.get(email=email)
            if user == file.owner:
                return Response({'message': 'Forbidden for you'}, status=status.HTTP_403_FORBIDDEN)
            file.shared_with.remove(user)
            file.save()
            accesses = [{'fullname': f'{u.first_name} {u.last_name}', 'email': u.email, 'type': 'author' if u == file.owner else 'co-author'} for u in [file.owner] + list(file.shared_with.all())]
            return Response(accesses, status=status.HTTP_200_OK)
        except File.DoesNotExist:
            raise NotFound({'message': 'Not found'})
        except CustomUser.DoesNotExist:
            return Response({'message': {'email': ['User not found']}}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class UserFilesView(generics.ListAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user)

class SharedFilesView(generics.ListAPIView):
    serializer_class = FileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return File.objects.filter(shared_with=self.request.user)
