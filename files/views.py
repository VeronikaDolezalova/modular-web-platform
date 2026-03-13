from django.shortcuts import render, get_object_or_404
from .models import DownloadFile


def file_list(request):
    """Display a grid of all available files for download."""
    files = DownloadFile.objects.all()
    return render(request, 'files/file_list.html', {'files': files})


def file_detail(request, slug):
    """Display detail page for a file, only if has_detail_page is enabled."""
    file = get_object_or_404(DownloadFile, slug=slug, has_detail_page=True)
    return render(request, 'files/file_detail.html', {'file': file})