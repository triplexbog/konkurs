from django.urls import path
from .views import FileUploadView, FileDetailView, AddAccessView, RemoveAccessView, UserFilesView, SharedFilesView

urlpatterns = [
    path('files', FileUploadView.as_view(), name='file-upload'),
    path('files/<file_id>', FileDetailView.as_view(), name='file-detail'),
    path('files/<file_id>/add-access', AddAccessView.as_view(), name='add-access'),
path('files/<file_id>/remove-access', RemoveAccessView.as_view(), name='remove-access'),

    path('files/disk', UserFilesView.as_view(), name='user-files'),
    path('shared', SharedFilesView.as_view(), name='shared-files'),
]
