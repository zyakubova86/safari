from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models

class UzbekistanCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название', )
    name_en = models.CharField(max_length=255, verbose_name='Название en', blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name='Слаг', blank=True, null=True)
    slug_en = AutoSlugField(populate_from='name_en', unique=True, verbose_name='Слаг en', blank=True, null=True)
    image = models.ImageField(upload_to='uzbekistan/categories/', verbose_name='Картинка', blank=True, null=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    text_en = models.TextField(verbose_name='Текст en', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Категория Узбекистана'
        verbose_name_plural = 'Категории Узбекистана'

    def __str__(self):
        return self.name


class Uzbekistan(models.Model):
    category = models.ForeignKey(UzbekistanCategory, on_delete=models.CASCADE, related_name='entries', verbose_name='Категория')
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(max_length=200, verbose_name='Название en', blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True, verbose_name='Слаг', blank=True, null=True)
    slug_en = AutoSlugField(populate_from='title_en', unique=True, verbose_name='Слаг en', blank=True, null=True)
    content = models.TextField(verbose_name='Текст')
    content_en = models.TextField(verbose_name='Текст en')
    image = models.ImageField(upload_to='uzbekistan/', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Узбекистан'
        verbose_name_plural = 'Узбекистан'

    def __str__(self):
        return self.title


class UzbekistanCities(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    name_en = models.CharField(max_length=255, verbose_name='Название en', blank=True, null=True)
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name='Слаг', blank=True, null=True)
    slug_en = AutoSlugField(populate_from='name_en', unique=True, verbose_name='Слаг en', blank=True, null=True)
    image = models.ImageField(upload_to='uzbekistan/cities/', verbose_name='Картинка', blank=True, null=True)
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    text_en = models.TextField(verbose_name='Текст en', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Город Узбекистана"
        verbose_name_plural = "Города Узбекистана"

    def __str__(self):
        return self.name


class TourCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    name_en = models.CharField(max_length=255, verbose_name='Название en', blank=True, null=True)
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    slug_en = models.SlugField(unique=True, verbose_name='Слаг en', blank=True, null=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    description_en = models.TextField(verbose_name='Описание en', blank=True, null=True)
    image = models.ImageField(upload_to='tours/categories/', verbose_name='Картинка')
    featured_image = models.ImageField(upload_to='tours/categories/', blank=True, null=True, verbose_name='Home картинка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Tours(models.Model):
    tour_category = models.ForeignKey(TourCategory, on_delete=models.CASCADE, related_name='tours', verbose_name='Категория')

    title = models.CharField(max_length=255, verbose_name='Название')
    title_en = models.CharField(max_length=255, verbose_name='Название en', blank=True, null=True)

    slug = AutoSlugField(populate_from='title',unique=True, always_update=True, verbose_name='Slug', blank=True, null=True)
    slug_en = AutoSlugField(populate_from='title_en',unique=True, always_update=True, verbose_name='Slug en', blank=True, null=True)

    short_description = models.TextField(verbose_name='Короткое описание')
    short_description_en = models.TextField(verbose_name='Короткое описание en', blank=True, null=True)

    full_description = RichTextField(verbose_name='Полное описание')
    full_description_en = RichTextField(verbose_name='Полное описание en', blank=True, null=True)

    itinerary = models.CharField(max_length=255, verbose_name='Маршрут')
    itinerary_en = models.CharField(max_length=255, verbose_name='Маршрут en', blank=True, null=True)

    location = models.CharField(max_length=255, verbose_name='Местоположение')
    location_en = models.CharField(max_length=255, verbose_name='Местоположение en', blank=True, null=True)

    duration_days = models.IntegerField(verbose_name='Количество дней')
    duration_nights = models.IntegerField(verbose_name='Количество ночей') 
    people_count = models.PositiveIntegerField(verbose_name='Количество людей') 
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0)
    lists_page_image = models.ImageField(upload_to='tours/lists_images/', verbose_name='Картинка для списка 365X305', blank=True, null=True)  
    main_image = models.ImageField(upload_to='tours/main_images/', verbose_name='Главная картинка 1200X700', blank=True, null=True)
    banner_image = models.ImageField(upload_to='tours/banner_images/', verbose_name='Баннерная картинка 1920X800', blank=True, null=True) 
    is_featured = models.BooleanField(default=False, verbose_name='Выделенный')
    is_active = models.BooleanField(default=True, verbose_name='Активный')    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f"/tours/{self.slug}/"


    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"    


class TourProgram(models.Model):
    tour = models.ForeignKey(Tours, related_name='programs', on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField(verbose_name='Номер дня')

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    title_en = models.CharField(max_length=255, verbose_name='Заголовок en', blank=True, null=True)

    description = RichTextField(verbose_name='Описание')
    description_en = RichTextField(verbose_name='Описание en', blank=True, null=True)

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"   

class TourGalleryImage(models.Model):
    tour = models.ForeignKey(Tours, related_name='gallery_images', on_delete=models.CASCADE)
    gallery_image = models.ImageField(upload_to='tours/gallery/', verbose_name='Картинка для галереи 1200x700')

    def __str__(self):
        return f"Gallery image for {self.tour.title}"


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='slider/', verbose_name='Картинка 1550x950')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайдеры"


class TourBooking(models.Model):
    TOUR_BOOKING_STATUS_CHOICES = [
            ('pending', 'В ожидании'),
            ('confirmed', 'Подтверждено'),
            ('cancelled', 'Отменено'), 
        ]

    tour = models.ForeignKey(Tours, on_delete=models.SET_NULL, related_name='bookings', verbose_name='Тур', null=True, blank=True)
    email = models.EmailField(verbose_name='Email')
    guest_number = models.PositiveIntegerField(verbose_name='Количество людей')
    arrival_date = models.DateField(verbose_name='Дата прибытия')
    status = models.CharField(max_length=255, verbose_name='Статус', choices=TOUR_BOOKING_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.tour.title} - {self.email}"

    class Meta:
        verbose_name = "Бронирование тура"
        verbose_name_plural = "Бронирования туров"


class ContactPage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    title_en = models.CharField(max_length=255, verbose_name='Заголовок en', blank=True, null=True)

    about_us = RichTextField(verbose_name='О нас')
    about_us_en = RichTextField(verbose_name='О нас en', blank=True, null=True)

    address = models.CharField(max_length=255, verbose_name='Адрес')
    address_en = models.CharField(max_length=255, verbose_name='Адрес en', blank=True, null=True)

    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=255, verbose_name='Телефон')
    banner_image = models.ImageField(upload_to='contact_page/', verbose_name='Картинка баннера 1920x800', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница Контакты"
        verbose_name_plural = "Страница Контакты"
