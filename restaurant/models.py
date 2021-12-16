from functools import update_wrapper
from django.db import models
from django.db.models import Q



class TimeStamped(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RestaurantQuerySet(models.QuerySet):         
    """
        Custom get_query_set , based on the lookups provided
    """
    def search(self,query):
        lookup = (Q(name__iexact=query)|
                    Q(cuisines__iexact = query)|
                    Q(rating__iexact = query)
                )

        return self.filter(lookup)


class RestaurantManager(models.Manager):
    def get_queryset(self):
        return RestaurantQuerySet(self.model , using = self._db)
     

    def search(self , query = None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)



class Restaurant(TimeStamped):
    CUISINE_CATEG = {
        1 : "caribbean",
        2 : "vietnamese",
        3 : "korean", 
        4 : "indian"
    }
    name = models.CharField(max_length=256)
    cuisines = models.SmallIntegerField(choices=CUISINE_CATEG.items())
    avg_cost_for_two = models.DecimalField(max_digits=10, decimal_places=3)
    currency = models.CharField(max_length=50)
    has_table_booking = models.BooleanField()
    has_online_booking = models.BooleanField()
    agg_rating = models.IntegerField()
    rating_color =  models.CharField(max_length=200)
    rating_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    objects = RestaurantManager()
    class Meta:
        ordering = ['created_on']

    def __str__(self) -> str:
        return "Restaurant-{name}".format(self.name)