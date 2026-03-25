from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    SKIN_TYPE_CHOICES = [
        ('all', 'All Skin Types'),
        ('dry', 'Dry Skin'),
        ('oily', 'Oily Skin'),
        ('sensitive', 'Sensitive Skin'),
        ('combination', 'Combination Skin'),
    ]

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    ingredients = models.TextField()
    skin_type = models.CharField(max_length=20, choices=SKIN_TYPE_CHOICES, default='all')
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])

    def __str__(self):
        return self.name

class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    products = models.ManyToManyField(Product, related_name='wishlisted_by', blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Ritual Wishlist"

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.PositiveIntegerField(help_text="Percentage discount (1-100)")
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, related_name='coupons', blank=True, help_text="Apply to specific products (leave blank for all)")

    def __str__(self):
        return f"{self.code} ({self.discount}%)"

    def is_valid(self):
        from django.utils import timezone
        now = timezone.now()
        return self.active and self.valid_from <= now <= self.valid_to
