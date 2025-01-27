from django.db import models

# Create your models here.
status_choices = (
    ('pending', 'Pending'),
    ('approved', 'Approved'),
    ('rejected', 'Rejected'),
    ('sold', 'Sold'),
    ('rented', 'Rented'),
)

class Property(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='property_images/')
    agent = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=status_choices, default='pending')

    def __str__(self):
        return f'${self.title} - ${self.agent.email}'