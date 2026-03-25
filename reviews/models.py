from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Review by {self.user.username} on {self.product.name}'
