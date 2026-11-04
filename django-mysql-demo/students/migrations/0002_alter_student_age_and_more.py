import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="age",
            field=models.PositiveIntegerField(
                default=18,
                validators=[
                    django.core.validators.MinValueValidator(18),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
        migrations.AddConstraint(
            model_name="student",
            constraint=models.CheckConstraint(
                condition=models.Q(age__gte=18, age__lte=100),
                name="student_age_between_18_and_100",
            ),
        ),
    ]
