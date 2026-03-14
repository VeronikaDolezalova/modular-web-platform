from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import ServicePackage, Order


def package_list(request):
    """Display all active service packages."""
    packages = ServicePackage.objects.filter(is_active=True)
    return render(request, 'orders/package_list.html', {'packages': packages})


def package_detail(request, slug):
    """Display detail page for a service package and handle order submission."""
    package = get_object_or_404(ServicePackage, slug=slug, is_active=True)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message', '')

        # save order to database
        Order.objects.create(
            package=package,
            name=name,
            email=email,
            message=message
        )

        # notify admin by email
        send_mail(
            subject=f'New order: {package.name}',
            message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
        )

        return redirect('orders:order_success')

    return render(request, 'orders/package_detail.html', {'package': package})


def order_success(request):
    """Display order confirmation page."""
    return render(request, 'orders/order_success.html')