from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RentalRequest, Review
from django.http import HttpResponseForbidden
from items.models import Item

@login_required
def send_request(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if request.method == 'POST':
        start_date = request.POST['start_date']
        end_date   = request.POST['end_date']
        message    = request.POST.get('message', '')

        RentalRequest.objects.create(
            borrower   = request.user,
            item       = item,
            start_date = start_date,
            end_date   = end_date,
            message    = message,
        )
        return redirect('dashboard')

    return render(request, 'rentals/request.html', {'item': item})


@login_required
def dashboard(request):
    my_requests = RentalRequest.objects.filter(borrower=request.user)
    my_items    = Item.objects.filter(owner=request.user)
    incoming    = RentalRequest.objects.filter(item__owner=request.user)

    context = {
        'my_requests': my_requests,
        'my_items'   : my_items,
        'incoming'   : incoming,
    }
    return render(request, 'rentals/dashboard.html', context)


@login_required
def update_request_status(request, request_pk, action):
    rental = get_object_or_404(RentalRequest, pk=request_pk)

    # تأكد إن صاحب الأداة هو اللي يوافق
    if rental.item.owner != request.user:
        return HttpResponseForbidden()

    if action == 'accept':
        rental.status = 'accepted'
        rental.item.is_available = False
        rental.item.save()
    elif action == 'reject':
        rental.status = 'rejected'
    elif action == 'returned':
        rental.status = 'returned'
        rental.item.is_available = True
        rental.item.save()

    rental.save()
    return redirect('dashboard')


@login_required
def add_review(request, rental_pk):
    rental = get_object_or_404(RentalRequest, pk=rental_pk)

    # فقط المستعير يقدر يقيّم
    if rental.borrower != request.user:
        return HttpResponseForbidden()

    # فقط بعد الإرجاع
    if rental.status != 'returned':
        return redirect('dashboard')

    # لو قيّم قبل كذا
    if hasattr(rental, 'review'):
        return redirect('dashboard')

    if request.method == 'POST':
        rating  = request.POST['rating']
        comment = request.POST.get('comment', '')

        Review.objects.create(
            rental   = rental,
            reviewer = request.user,
            rating   = rating,
            comment  = comment,
        )
        return redirect('dashboard')

    return render(request, 'rentals/review.html', {'rental': rental})