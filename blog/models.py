from django.db import models

class Category(models.Model):
    """
    Represents a blog category.
    Articles can belong to multiple categories.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        """Return the category name as string representation."""
        return self.name

    class Meta:
        verbose_name_plural = "Categories" # fix plural name in admin


class Article(models.Model):
    """
    Represents a blog article. Image and Facebook discussion link are optional.
    Publishing is controlled by is_published flag and published datetime.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)    # unique slug (human-readable) for URL
    perex = models.TextField() # short summary of the article, shown on the homepage and category pages
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True) # when the article was published, can be null if not published yet
    created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False) # if true, article is visible on the site, otherwise it's a draft
    categories = models.ManyToManyField(Category, related_name='articles') # an article can belong to multiple categories, and a category can have multiple articles
    fb_discussion_url = models.URLField(blank=True, null=True) # optional URL to Facebook discussion for the article

    def __str__(self):
        """Return the article title as string representation."""
        return self.title

    class Meta:
        ordering = ['-published'] #newest article first