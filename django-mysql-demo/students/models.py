from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(100)], default=18
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(age__gte=18, age__lte=100),
                name="student_age_between_18_and_100",
            )
        ]

        indexes = [
            models.Index(fields=["email"], name="student_email_idx"),
        ]

    def __str__(self):
        return self.name
