from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import *


# Create your views here.

def home(request):
    lang = 'en' if request.path.startswith('/en/') else 'ru'
    template = 'tours/home_en.html' if lang == 'en' else 'tours/home.html'

    slider_items = Slider.objects.filter(is_active=True)
    tours_all = Tours.objects.filter(is_active=True)
    categories = TourCategory.objects.all()
    tours_featured = Tours.objects.filter(is_active=True, is_featured=True)

    if request.method == 'POST':
        try:
            email = request.POST.get('booking_email')
            arrival_date_raw = request.POST.get('booking_arrival_date')
            guest_number = request.POST.get('booking_guest_number')
            tour_id = request.POST.get('booking_tour_id')

            tour = Tours.objects.get(pk=tour_id)
            # print("arrival_date_raw:", arrival_date_raw)
            arrival_date = datetime.strptime(arrival_date_raw, "%d/%m/%Y").date()

            # print("tour data:", email, arrival_date, guest_number, tour_id)

            booking = TourBooking(
                email=email,
                arrival_date=arrival_date,
                guest_number=guest_number,
                tour=tour
            )
            booking.save()

            # send_mail(
            #     'Your booking is confirmed',
            #     f'Thank you for booking the {tour.title} tour',
            #     settings.EMAIL_HOST_USER,
            #     [email],
            #     fail_silently=False
            # )

            if lang == 'en':
                return JsonResponse({'success': ' ✅ Your booking is confirmed!'}, status=200)

            return JsonResponse({'success': ' ✅ Бронирование принято!'}, status=200)

        except Exception as e:
            print("error:", e)
            return JsonResponse({'error': 'Произошла ошибка сервера'}, status=500)

    context = {
        'tours_all': tours_all,
        'slider_items': slider_items,
        'categories': categories,
        'tours_featured': tours_featured,
        'lang': lang,
    }
    return render(request, template, context)


def tours_list_by_category(request, pk):
    lang = 'en' if request.path.startswith('/en/') else 'ru'
    template = 'tours/tours_list_en.html' if lang == 'en' else 'tours/tours_list.html'

    category = get_object_or_404(TourCategory, pk=pk)
    tours = Tours.objects.filter(tour_category=category, is_active=True)
    categories = TourCategory.objects.all()


    context = {
        'tours': tours,
        'category': category,
        'categories': categories,
        'lang': lang,
    }
    return render(request, template, context)

def tour_detail(request, pk):
    lang = 'en' if request.path.startswith('/en/') else 'ru'
    template = 'tours/tour_detail_en.html' if lang == 'en' else 'tours/tour_detail.html'

    # template = 'tours/tour_detail.html'

    tour = get_object_or_404(Tours, pk=pk)
    programs = tour.programs.all()
    gallery_images = tour.gallery_images.all()
    categories = TourCategory.objects.all()

    if request.method == 'GET':
        context = {
            'tour': tour,
            'programs': programs,
            'gallery_images': gallery_images,
            'categories': categories,
            'lang': lang
        }
        return render(request, template, context)

    elif request.method == 'POST':
        try:
            email = request.POST.get('booking_email')
            arrival_date_raw = request.POST.get('booking_arrival_date')
            guest_number = request.POST.get('booking_guest_number')
            tour_id = request.POST.get('booking_tour_id')

            tour_obj = Tours.objects.get(pk=tour_id)
            arrival_date = datetime.strptime(arrival_date_raw, "%m/%d/%Y").date()

            # print("tour data:", email, arrival_date, guest_number, tour_id)

            booking = TourBooking(
                email=email,
                arrival_date=arrival_date,
                guest_number=guest_number,
                tour=tour_obj
            )
            booking.full_clean()
            booking.save()

            # email_subject = f'Подтверждение бронирования тура "{tour.title}"'
            # email_message = f'''Спасибо за бронирование тура "{tour.title}".
            # Дата прибытия: {arrival_date.strftime("%d.%m.%Y")}
            # Количество участников: {guest_number}
            # Мы свяжемся с вами для подтверждения бронирования.'''

            # send_mail(
            #     subject=email_subject,
            #     message=email_message,
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[email],
            #     fail_silently=False,
            # )

            if lang == 'en':
                return JsonResponse({'success': ' ✅ Your booking is confirmed!'}, status=200)
            return JsonResponse({'success': ' ✅ Бронирование принято!'}, status=200)

        except Exception as e:
            print("detail page booking exception", e)
            if lang == 'en':
                return JsonResponse({"error": "Error"}, status=500)
            return JsonResponse({"error": "Произошла ошибка."}, status=500)

def book_ticket(request):
    lang = 'en' if request.path.startswith('/en/') else 'ru'
    template = 'tours/book_ticket_en.html' if lang == 'en' else 'tours/book_ticket.html'
    categories = TourCategory.objects.all()

    context = {
        'categories': categories,
        'lang': lang
    }

    return render(request, template, context)


def contact(request):
    lang= 'en' if request.path.startswith('/en/') else 'ru'
    template = 'tours/contact_en.html' if lang == 'en' else 'tours/contact.html'

    contacts = ContactPage.objects.all()
    categories = TourCategory.objects.all()

    context = {
        'contacts': contacts,
        'categories': categories,
        'lang': lang
    }

    return render(request, template, context)


def uzbekistan(request):
    lang= 'en' if request.path.startswith('/en/') else 'ru'
    template = 'tours/uzbekistan_en.html' if lang == 'en' else 'tours/uzbekistan.html'

    categories = TourCategory.objects.all()
    cats_uzbekistan = UzbekistanCategory.objects.filter(is_active=True)
    cities = UzbekistanCities.objects.all()

    context = {
        'cats_uzbekistan': cats_uzbekistan,
        'cities': cities,
        'categories': categories,
        'lang': lang
    }

    return render(request, template, context)