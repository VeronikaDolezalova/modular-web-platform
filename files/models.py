from django.db import models
from django.contrib.auth.models import User


class DownloadFile(models.Model):
    """
    Represents a downloadable file (e-book, guide, etc.).
    Either description or image must be provided - validated in form.
    """

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # unique slug (human-readable) for URL
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='files/', blank=True, null=True)
    file = models.FileField(upload_to='downloads/')  # the actual file to download
    has_detail_page = models.BooleanField(default=False)  # enable dedicated detail page
    content = models.TextField(blank=True, null=True)  # detail page content, if enabled
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='files'  # access author's files via user.files.all()
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the file name as string representation."""
        return self.name

    class Meta:
        ordering = ['-created']  # newest files first