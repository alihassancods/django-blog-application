from django.db import models
from django.conf import settings # importing the project settings
from django.utils import timezone
# Create your models here.


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super(PublishedPostManager,self).get_queryset().filter(status=Post.Status.PUBLISHED)
        # this manager is used to display the published posts only
        # we have overridden the method to return published posts only




class Post(models.Model):

    objects = models.Manager()
    published = PublishedPostManager()
    """
    We have defined the two Managers like objects is default manager and published is 
    our custom defined manager which will use its custom query
    If we are going to use some custom developed manager then we must also explicitly
    define objects as well. Otherwise in default conditions the django itself defines objects.
    """


    class Status(models.TextChoices): # status subclass of the the TextChoices  
        DRAFT = 'DF','Draft' # The Name of the choice is DRAFT and DF is Value of Choice and Draft is label
    #   NAME = 'VALUE','Label'
        PUBLISHED = 'PB','Published'   
    title = models.CharField(max_length=100) #VARCHAR
    slug = models.SlugField(max_length=100) #VARCHAR
    body = models.TextField(max_length=300) #TEXT
    publishDate = models.DateTimeField(default=timezone.now) #DATETIME in SQL # DateTime accodring to timezone that when post was published
    # publish = models.DateTimeField(db_default=Now())
    """
    To use database generated values we use db_default instead of default, The timezone.now uses python to generate date and time
    While the database NOW function uses database to generate date and time
    More database functions at https://docs.djangoproject.com/en/5.0/ref/models/database-functions/.
    """
    created = models.DateTimeField(auto_now_add=True) # Date and Time when post is created, auto_now_add automatically saves date when creating object
    updated = models.DateTimeField(auto_now=True) # Date and Time when post is updated, auto_now automatically saves date when object is saved
    status = models.CharField(
    max_length=2, # like the 'DF' value will be stored  
    choices=Status, # the choices in Status Class will be used
    default=Status.DRAFT
) # this will be managing the status of the blog that its in published state or draft state
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='blog_posts')
    """
    The authors are defined by the AUTH of the Django and on_delete is models.CASCADE which will delete all posts
    on deletion of author, we use related_name to name relation from user to posts. Like a user has multiple blog Posts
    """
    class Meta:
        ordering = ['-publishDate'] # default ordering of the posts, the '-publish sorts in descending order
        indexes = [
            models.Index(fields=['-publishDate']), #
        ]

    def __str__(self):
        return self.title
