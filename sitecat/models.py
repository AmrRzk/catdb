from django.db import models


class Home(models.Model):
    HOUSE_TYPE_CHOICES = [
        ('Terrace', 'Terrace'),
        ('Semi-D', 'Semi-Detached'),
        ('Bungalow', 'Bungalow'),
        ('Flat', 'Flat'),
        ('Apartment', 'Apartment'),
        ('Condominium', 'Condominium'),
        ('Penthouse', 'Penthouse')
    ]

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    house_type = models.CharField(
        max_length=20,
        choices=HOUSE_TYPE_CHOICES,
        default='Apartment'
    )

    def __str__(self) -> str:
        return f"{self.name}: {self.address}"


class Human(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not Disclosed')
    ]
    name = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default='N')
    birth_date = models.DateField('date of birth')
    description = models.CharField(max_length=300)
    home = models.ForeignKey(Home,
                             on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name


class Cat(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    name = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES, default='N')
    birth_date = models.DateField('date of birth')
    description = models.CharField(max_length=300)
    breed = models.ForeignKey(
        Breed, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        Human, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
