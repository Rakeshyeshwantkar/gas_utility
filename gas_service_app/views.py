from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from .forms import ServiceRequestForm
from .models import ServiceRequest

def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save()
            # You can associate the service request with the logged-in customer here
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_service_request.html', {'form': form})

def track_service_request(request):
    # Retrieve service requests associated with the logged-in customer
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'track_service_request.html', {'service_requests': service_requests})


@login_required  # Apply the login_required decorator to the view
def track_service_request(request):
    # Retrieve service requests associated with the logged-in customer
    service_requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'track_service_request.html', {'service_requests': service_requests})
