from django.db   import models
from core.models import TimeStampModel


class Region(models.Model):
    district_name = models.CharField(max_length=10)

    class Meta:
        db_table = "regions"


class TechnologyStack(models.Model):
    title          = models.CharField(max_length=20)
    color          = models.CharField(max_length=20)
    stack_category = models.ForeignKey("StackCategory", on_delete=models.SET_NULL, null=True)
    project        = models.ManyToManyField("projects.Project", through="projects.ProjectStack")

    class Meta:
        db_table = "technology_stacks"


class StackCategory(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        db_table = "stack_categories"


class Position(models.Model):
    roll = models.CharField(max_length=10)

    class Meta:
        db_table = "positions"


class Image(TimeStampModel):
    image_url        = models.URLField(max_length=2000)
    image_type       = models.ForeignKey("ImageType", on_delete=models.PROTECT)
    project          = models.ForeignKey("projects.Project", on_delete=models.CASCADE, null=True)
    user             = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    technology_stack = models.ForeignKey("commons.TechnologyStack", on_delete=models.CASCADE, null=True)
    banner           = models.ForeignKey("Banner", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "images"


class Banner(TimeStampModel):
    title       = models.CharField(max_length=40)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "banners"

class ImageType(TimeStampModel):
    title = models.CharField(max_length=20)

    class Meta:
        db_table = "image_types"