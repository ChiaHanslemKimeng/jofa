from django.views.generic import TemplateView, CreateView, ListView
from .models import FAQ, Partner, ContactMessage, TeamMember
from products.models import Product
from blog.models import Post
from reviews.models import Review
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Product.objects.filter(featured=True).order_by('-created_at')[:6]
        context['latest_posts'] = Post.objects.filter(published=True)[:3]
        context['partners'] = Partner.objects.all()
        # Fetch top 6 approved reviews for the home page slider
        context['reviews'] = Review.objects.filter(approved=True)[:6]
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.all()
        return context

class FAQView(ListView):
    model = FAQ
    template_name = 'core/faq.html'
    context_object_name = 'faqs'

class ContactView(CreateView):
    model = ContactMessage
    fields = ['name', 'email', 'phone', 'subject', 'message']
    template_name = 'core/contact.html'
    success_url = reverse_lazy('core:home')
