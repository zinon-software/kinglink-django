from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('يجب أن يكون لدى المستخدمين عنوان بريد إلكتروني')
		if not username:
			raise ValueError('يجب أن يكون لدى المستخدمين اسم مستخدم')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	username 				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=25,blank=True)

    description = models.CharField(max_length=100, blank=True)
    follows = models.ManyToManyField(Account,related_name="follows",blank=True)
    followers = models.ManyToManyField(Account,related_name="followers",blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"



REASON = [
    
    ('SPAM','SPAM'),
    ('INAPPROPRIATE','INAPPROPRIATE'),
    
]


class UserReport(models.Model):
    reported_user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='reported_user')
    reason = models.CharField(max_length=14,choices=REASON)
    reporting_user = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='reporting_user')
    date_reported = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.reported_user.username