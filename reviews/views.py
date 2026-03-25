from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Review
from products.models import Product

class ReviewCreateView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if rating and comment:
            Review.objects.create(
                product=product,
                user=request.user,
                rating=rating,
                comment=comment
            )
        return redirect('products:product_detail', slug=product.slug)
