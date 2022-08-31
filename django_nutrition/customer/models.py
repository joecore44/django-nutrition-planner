from django.db import models
from django.db import models
from django.contrib.auth.models import User
from trainer.models import BillingPlan
from django.utils import timezone

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, 
        on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',
        upload_to='customer_media/profile')
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class CustomerSubscription(models.Model):
    CustomerProfile = models.ForeignKey(CustomerProfile, 
        on_delete=models.CASCADE)
    billing_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField()
    billing_plan_id = models.OneToOneField(BillingPlan, 
        on_delete=models.CASCADE)


    def __str__(self):
        return 'Subscription ' + str(self.billing_date)