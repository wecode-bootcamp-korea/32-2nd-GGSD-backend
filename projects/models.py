from django.db   import models
from core.models import TimeStampModel


class Project(TimeStampModel):
    title            = models.CharField(max_length=100)
    start_recruit    = models.DateField()
    end_recruit      = models.DateField()
    start_project    = models.DateField()
    end_project      = models.DateField()
    description      = models.TextField()
    like             = models.PositiveBigIntegerField(default=0)
    hit              = models.PositiveBigIntegerField(default=0)
    front_vacancy    = models.PositiveSmallIntegerField(default=0)
    back_vacancy     = models.PositiveSmallIntegerField(default=0)
    is_online        = models.BooleanField(default=True)
    progress_status  = models.ForeignKey("ProgressStatus", on_delete=models.SET_NULL, null=True)
    project_category = models.ForeignKey("ProjectCategory", on_delete=models.SET_NULL, null=True)
    region           = models.ForeignKey("commons.Region", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "projects"


class ProgressStatus(models.Model):
    step = models.CharField(max_length=20)

    class Meta:
        db_table = "progress_statuses"


class ProjectCategory(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        db_table = "project_categories"


class ProjectStack(TimeStampModel):
    project          = models.ForeignKey("Project", on_delete=models.CASCADE)
    technology_stack = models.ForeignKey("commons.TechnologyStack", on_delete=models.CASCADE)

    class Meta:
        db_table = "projects_stacks"