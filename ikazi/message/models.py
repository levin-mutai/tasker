from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.mail import send_mail
# Create your models here.

class Client_messages(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    phone = PhoneNumberField(null=False, blank=False, unique=False)
    message = models.TextField(max_length=1000)
    sent_date = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = ("Message")
        verbose_name_plural = ("Messages")

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        send_mail(
            'IkokaziKE Client Message',
            self.message,
            self.email,
            ['noreply.lefla@gmail.com'],
            fail_silently=False,
        )
        send_mail(
            'IkokaziKE',
            'Thanks for getting in touch with ikokazi. Your message has been received. ',
            'noreply.lefla@gmail.com',
            [self.email],
            fail_silently=False,
        )
        return super(Client_messages, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class subscribe(models.Model):
    email = models.EmailField()
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        send_mail(
            'IkokaziKE email subscription',
            self.email,' subscribed IkokaziKe monthly updates.',
            self.email,
            ['noreply.lefla@gmail.com'],
            fail_silently=False,
        )
        send_mail(
            'IkokaziKE',
            'Thanks for subscribing to our monthly updates.',
            'noreply.lefla@gmail.com',
            [self.email],
            fail_silently=False,
        )
        return super(Client_messages, self).save(*args, **kwargs)
