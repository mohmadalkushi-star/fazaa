from django.shortcuts import redirect, render, get_object_or_404
from .models import Item
from django.contrib.auth.decorators import login_required


def item_list(request):
    items = Item.objects.filter(is_available=True)

    # فلتر المدينة أولاً
    city = request.GET.get('city')
    if city:
        items = items.filter(city=city)

    # فلتر الحي
    neighborhood = request.GET.get('neighborhood')
    if neighborhood:
        items = items.filter(neighborhood=neighborhood)

    # فلتر التصنيف
    category = request.GET.get('category')
    if category:
        items = items.filter(category=category)

    # المدن المتاحة
    cities = Item.objects.filter(is_available=True)\
                         .values_list('city', flat=True)\
                         .distinct()

    # الأحياء — لو اختار مدينة يظهر أحياءها فقط
    if city:
        neighborhoods = Item.objects.filter(is_available=True, city=city)\
                                    .values_list('neighborhood', flat=True)\
                                    .distinct()
    else:
        neighborhoods = Item.objects.filter(is_available=True)\
                                    .values_list('neighborhood', flat=True)\
                                    .distinct()

    context = {
        'items'        : items,
        'cities'       : cities,
        'neighborhoods': neighborhoods,
    }
    return render(request, 'items/list.html', context)


def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    context = {
        'item': item,
    }
    return render(request, 'items/detail.html', context)


@login_required
def add_item(request):
    if request.method == 'POST':
        name        = request.POST['name']
        description = request.POST['description']
        category    = request.POST['category']
        condition   = request.POST['condition']
        price       = request.POST.get('price', 0)
        is_free     = 'is_free' in request.POST
        image       = request.FILES.get('image')

        # المدينة والحي تجيان تلقائياً من بروفايل المستخدم
        profile = request.user.profile

        Item.objects.create(
            owner        = request.user,
            name         = name,
            description  = description,
            category     = category,
            condition    = condition,
            price        = price,
            is_free      = is_free,
            city         = profile.city,
            neighborhood = profile.neighborhood,
            image        = image,
        )
        return redirect('dashboard')

    return render(request, 'items/add_item.html')