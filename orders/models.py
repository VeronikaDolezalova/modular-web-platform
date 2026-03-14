from django.db import models


class ServicePackage(models.Model):
    """
    Represents a service package available for ordering.
    Each package has a detail page with full description.
    """

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # unique slug (human-readable) for URL
    short_description = models.TextField()  # displayed in package listing
    content = models.TextField()  # full description on detail page
    price = models.DecimalField(max_digits=10, decimal_places=2)  # display only
    is_active = models.BooleanField(default=True)  # show/hide package
    order = models.PositiveIntegerField(default=0)  # display order on page

    def __str__(self):
        """Return the package name as string representation."""
        return self.name

    class Meta:
        ordering = ['order']  # display packages in defined order


class Order(models.Model):
    """
    Represents a customer order for a service package.
    Admin is notified by email upon submission.
    """

    package = models.ForeignKey(
        ServicePackage,
        on_delete=models.PROTECT,  # prevent deleting packages with existing orders
        related_name='orders'
    )
    name = models.CharField(max_length=200)  # customer name
    email = models.EmailField()  # customer email
    message = models.TextField(blank=True, null=True)  # optional note from customer
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return order summary as string representation."""
        return f"{self.name} — {self.package.name}"

    class Meta:
        ordering = ['-created']  # newest orders first