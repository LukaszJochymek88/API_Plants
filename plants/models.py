from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False, null=False, default="",
        verbose_name="Nazwa",
        unique=True,
        help_text="Nazwa kategori",
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False, null=False, default="",
        verbose_name="Nazwa",
        unique=True,
        help_text="Rodzaj Pokoju",
    )
    TEMPERATURE_CHOICES = [
        ("COLD" , "cold"),
        ("MEDIUM" , "medium"), 
        ("WARM" , "warm"),
    ]
    temperature = models.CharField(
        max_length=10,
        choices=TEMPERATURE_CHOICES,
        blank=False, null=False, 
        verbose_name="Temperature",
        help_text="",
    )
    EXPOSURE_CHOICES = [
        ("DARK" , "dark"),
        ("SHADE" , "shade"), 
        ("PARTSUN" , "part sun"),
        ("FULLSUN" , "full sun"),
    ]
    exposure = models.CharField(
        max_length=10,
        choices=EXPOSURE_CHOICES,
        blank=False, null=False,
        verbose_name="Ekspozycja",
        help_text=""
    )
    HUMIDITY_CHOICES = [
        ("LOW" , "low"),
        ("MEDIUM" , "medium"), 
        ("HIGH" , "high"),
    ]
    humidity = models.CharField(
        max_length=10,
        choices=HUMIDITY_CHOICES,
        blank=False, null=False,
        verbose_name="Humidity",
        help_text=""
    )
    draft = models.BooleanField(
        blank=True, null=False, default=False,
        verbose_name="Drafty?",
        help_text=""
    )

    # class Meta:
    #     verbose_name = "Room"
    #     ordering = ['name']
    
    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False, null=False,
        unique=True,
        verbose_name="Nazwa Rośliny",
        help_text="Nazwa Rośliny",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        blank=False, null=False,
        verbose_name="Plant's category",
        help_text="",
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.SET_NULL,
        blank=True, null=True, default=None,
        verbose_name="Plant's room",
        help_text="",
    )
    watering_interval = models.PositiveIntegerField(
        blank=False, null=False, default="",
        verbose_name="Okres podlewania",
        help_text="dni"
    )
    fertilizing_interval = models.PositiveIntegerField(
        blank=False, null=False,
        verbose_name="Okres nawożenia",
        help_text="dni"
    )
    EXPOSURE_CHOICES = Room.EXPOSURE_CHOICES
    required_exposure =  models.CharField(
        max_length=10,
        choices=EXPOSURE_CHOICES,
        blank=False, null=False,
        verbose_name="Ekspozycja",
        help_text=""
    )
    HUMIDITY_CHOICES = Room.HUMIDITY_CHOICES
    required_humidity = models.CharField(
        max_length=10,
        choices=HUMIDITY_CHOICES,
        blank=False, null=False, 
        verbose_name="Ekspozycja",
        help_text="",
    )
    TEMPERATURE_CHOICES = Room.TEMPERATURE_CHOICES
    required_temperature = models.CharField(
        max_length=10,
        choices=TEMPERATURE_CHOICES,
        blank=False, null=False, 
        verbose_name="Temperatura",
        help_text="",
    )

    blooming = models.BooleanField(
        blank=True, null=False, default=False,
        verbose_name="Blooming?",
        help_text="",
    )
    DIFFICULTY_CHOICES = (
        (1, "Low"),
        (2, "Medium-Low"),
        (3, "Medium"),
        (4, "Medium-high"),
        (5, "High"),
    )
    defficulty = models.PositiveIntegerField(
        choices=DIFFICULTY_CHOICES,
        blank=False, null=False, default=1,
        verbose_name="Cultivation difficulty level",
        help_text="",
    )

    last_watered = models.DateTimeField(
        blank=True, null=True, default=None,
        verbose_name="Ostatnie Podlanie",
        help_text="",
        )
    last_fertilized = models.DateTimeField(
        verbose_name="Ostatnie nawożenie",
        blank=True, null=True, default=None,
        )

    # class Meta:
    #     verbose_name = "Plant"
    #     ordering = ['name', 'category', 'room', 'watering_interval', 'fertilizing_interval', 'required_exposure', 'required_humidity', 'blooming', 'defficulty', 'last_watered', 'last_fertilized' ]
    
    def __str__(self):
        return self.name