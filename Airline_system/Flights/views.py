from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight, GuestBooking
from .forms import GuestBookingForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.dateparse import parse_date
from django.utils import timezone
# Create your views here.



### Landing page
def index(request):
    return render(request, 'flights/index.html', {
        'flights' : Flight.objects.all()
    })



### Search Form - if from or to matches any date, returns those flights. 
# # No available flights and show available flights with thematching from/to/date
def search(request):
    flights = []
    show_fallback = False
    origin = request.GET.get("from", "").strip()
    destination = request.GET.get("to", "").strip()
    departure_date = request.GET.get("date", "").strip()

    if request.GET:  # Only search after form submission
        query = Flight.objects.all()

        if origin:
            query = query.filter(origin__city__icontains=origin)

        if destination:
            query = query.filter(destination__city__icontains=destination)

        fallback_query = query  # Save before date filter

        if departure_date:
            date_obj = parse_date(departure_date)
            if date_obj:
                query = query.filter(departure_time__date=date_obj)

        if query.exists():
            flights = query
        elif fallback_query.exists():
            flights = fallback_query
            show_fallback = True

    context = {
        "flights": flights,
        "from": origin,
        "to": destination,
        "date": departure_date,
        "show_fallback": show_fallback
    }

    return render(request, "flights/search.html", context)


# ### Book_flight
# def book_flight(request, flight_id):
#      flight = get_object_or_404(Flight, id=flight_id)

#      if request.method == "POST":
#             form = GuestBookingForm(request.POST)
#             if form.is_valid():
#                 booking = form.save(commit=False)  
#                 booking.flight = flight
#                 booking.booking_date = timezone.now()
#                 booking.save()
#                 return redirect("booking_success", booking.id) 
#      else:
#             form = GuestBookingForm()

#      return render(request, "flights/book.html", {"form": form, "flight": flight})


def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == "POST":
        form = GuestBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight = flight
            booking.booking_date = timezone.now()

            # Associate with user if logged in
            if request.user.is_authenticated:
                booking.user = request.user  # You must have a `user` field in the model

            booking.save()
            return redirect("booking_success", booking.id)
    else:
        form = GuestBookingForm()

    return render(request, "flights/book.html", {"form": form, "flight": flight})

def booking_success(request, booking_id):
    booking = get_object_or_404(GuestBooking, id=booking_id)
    return render(request, "flights/booking_success.html", {"booking": booking})


### Flight details Page
def flight(request, flight_id):
    
    if Flight.objects.filter(id=flight_id).exists():
        flight = Flight.objects.get(id=flight_id)
        
        return render(request, 'flights/flight.html', {
            'flight' : flight,
            ##'passengers': flight.passengers.all(),
            ##'non_passenger': Passenger.objects.exclude(flights=flight).all()
            })
    return render (request, 'flights/404.html', {
        'flight' : flight_id
    })

    

### Booking Page
def book(request):
    if request.method == 'POST':
        form = GuestBookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking successful!")
            return redirect('book')
        form = GuestBookingForm()

    else:
        form = GuestBookingForm()
    return render(request, 'flights/book.html', {'form': form})
    


#### Login 

def login(request):
    pass


#### Logout

def logout(request):
    pass


#### cancel booking

def cancel_book(request):
    pass


### view history

def history(request):
    pass