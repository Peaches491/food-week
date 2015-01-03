from django.db import models
from django.utils import timezone
import datetime


class Ingredient(models.Model):
    # Almonds, Chicken Breast, Cumen
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=25)
    name_plural = models.CharField(max_length=25)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class LineItem(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=6)
    unit = models.ForeignKey(Unit)

    # Chopped
    ingredient_adjective = models.CharField(max_length=200, blank=True)
    # Almonds
    ingredient_name = models.ForeignKey(Ingredient)

    adjective_reverse = models.BooleanField(default=False)

    def get_amount(self):
        if self.amount > 1:
            unit = self.unit.name_plural
        else:
            unit = self.unit.name
        return " ".join((str(self.amount), unit,))

    def full_name(self):
        if not self.adjective_reverse:
            return " ".join([self.get_amount(), str(self.ingredient_adjective), str(self.ingredient_name)])
        else:
            return " ".join([self.get_amount(), str(self.ingredient_name), str(self.ingredient_adjective)])

    def __str__(self):
        return self.full_name()


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    add_date = models.DateField('date added')

    def was_added_recently(self):
        return self.add_date >= timezone.now().date() - datetime.timedelta(days=1)
    was_added_recently.admin_order_field = 'add_date'
    was_added_recently.boolean = True
    was_added_recently.short_description = 'Published recently?'

    line_items = models.ManyToManyField(LineItem)

    details = models.TextField()

    def __str__(self):
        return self.name