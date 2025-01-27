from django.shortcuts import render, get_object_or_404
from property.decorators import verified_user_required
from .models import Property
from users.models import CustomUser

# Create your views here.


def index(request):
    properties = Property.objects.all()
    return render(request, 'properties/index.html', {'properties': properties})

@verified_user_required
def property_detail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    return render(request, 'properties/property_detail.html', {'property': property})

@verified_user_required
def dashboard(request):
    user = request.user  # Get the currently logged-in user
    properties = Property.objects.filter(agent=user)

    # Count properties by status
    approved_count = properties.filter(status='approved').count()
    sold_count = properties.filter(status='sold').count()
    rented_count = properties.filter(status='rented').count()
    pending_count = properties.filter(status='pending').count()

    total_properties = approved_count + sold_count + rented_count

    return render(request, 'properties/dashboard.html', {
        'user': user,
        'properties': properties,
        'total_properties': total_properties,
        'approved_count': approved_count,
        'sold_count': sold_count,
        'rented_count': rented_count,
        'pending_count': pending_count,
    })


@verified_user_required
def add_property(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES['image']

        user = request.user
        property = Property.objects.create(
            title=title,
            description=description,
            price=price,
            image=image,
            agent=user,
            status='pending'
        )

        property.save()

        return render(request, 'properties/add-property.html', {'message': 'Property added successfully!'})

    return render(request, 'properties/add-property.html')


def verification_required(request):
    return render(request, 'properties/verification_required.html')

def pricing(request):
    return render(request, 'properties/pricing.html')

def about(request):
    return render(request, 'properties/about-us.html')

def contact(request):
    return render(request, 'properties/contact.html')

def faq(request):
    return render(request, 'properties/faq.html')

def services(request):
    return render(request, 'properties/our-service.html')