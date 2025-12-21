from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField()
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
    



#1 - 1 Relationship
#1 user can have only 1 profile => 1
#1 profile is associated to only 1 user => 1
# oneToOnefield()=> Any model


## 1 - M relationship
#1 user can add M post => M
# 1 post is associated to only 1 user => 1
# in django use foreignkey()=> Use in many side model


## M -M Relationship # 1 student can learn from M teacher => M
#1 student can teach M student => M
# manyToManyField => Any place