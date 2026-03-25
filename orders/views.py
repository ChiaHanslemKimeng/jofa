from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .cart import Cart
from products.models import Product, Coupon
from .models import Order, OrderItem
from django.urls import reverse_lazy

class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))
        cart.add(product=product, quantity=quantity)
        return redirect('orders:cart_detail')

class CartRemoveView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('orders:cart_detail')

class CartDetailView(TemplateView):
    template_name = 'orders/cart_detail.html'

class CouponApplyView(View):
    def post(self, request):
        code = request.POST.get('code')
        cart = Cart(request)
        if cart.apply_coupon(code):
            from django.contrib import messages
            messages.success(request, f'Coupon "{code}" applied successfully!')
        else:
            from django.contrib import messages
            messages.error(request, 'Invalid or expired coupon code.')
        return redirect('orders:cart_detail')

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
    template_name = 'orders/order_create.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save(commit=False)
        order.user = self.request.user
        order.save()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        return super().form_valid(form)

class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user=request.user)
        return render(request, 'orders/order_detail.html', {'order': order})
