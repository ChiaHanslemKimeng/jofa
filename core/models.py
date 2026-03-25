from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "FAQs"
        ordering = ['order']

    def __str__(self):
        return self.question

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.role}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
