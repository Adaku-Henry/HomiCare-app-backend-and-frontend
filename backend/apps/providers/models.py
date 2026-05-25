from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# =========================
# PROVIDER PROFILE
# =========================
class ProviderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="provider_profile")

    profile_photo = models.ImageField(upload_to="providers/photos/", blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    national_id = models.CharField(max_length=100, unique=True)

    bio = models.TextField(blank=True, null=True)

    rating = models.FloatField(default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)

    is_verified = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.user} - Provider Profile"


# =========================
# PROVIDER SERVICES
# =========================
class ProviderService(models.Model):
    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="services"
    )

    service_name = models.CharField(max_length=255, default="General Service")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.service_name


# =========================
# PROVIDER PORTFOLIO
# =========================
class ProviderPortfolio(models.Model):
    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="portfolio"
    )

    image = models.ImageField(upload_to="providers/portfolio/")
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)


# =========================
# AVAILABILITY
# =========================
class ProviderAvailability(models.Model):
    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="availability"
    )

    day_of_week = models.CharField(max_length=20)  # Monday, Tuesday...
    start_time = models.TimeField()
    end_time = models.TimeField()

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return "{self.provider.user} - {self.day_of_week}"


# =========================
# VERIFICATION
# =========================
class ProviderVerification(models.Model):
    provider = models.OneToOneField(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="verification"
    )

    id_document = models.FileField(upload_to="providers/verification/")
    is_approved = models.BooleanField(default=False)

    submitted_at = models.DateTimeField(auto_now_add=True)


# =========================
# REVIEWS
# =========================
class ProviderReview(models.Model):
    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.PositiveIntegerField()  # 1–5 stars
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.provider.user} - {self.rating}"


# =========================
# NOTIFICATIONS
# =========================
class ProviderNotification(models.Model):
    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(max_length=255)
    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
