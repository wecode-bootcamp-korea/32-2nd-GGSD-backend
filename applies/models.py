from django.db   import models
from core.models import TimeStampModel


class ProjectApply(TimeStampModel):
    project_apply_status = models.ForeignKey("ProjectApplyStatus", on_delete=models.PROTECT)
    project              = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    position             = models.ForeignKey("commons.Position", on_delete=models.PROTECT)
    user                 = models.ForeignKey("users.User", on_delete=models.CASCADE)
    project_apply_stack  = models.ManyToManyField("commons.TechnologyStack", through="ProjectApplyStack")

    class Meta:
        db_table = "projects_applies"


class ProjectApplyStatus(TimeStampModel):
    type = models.CharField(max_length=20)

    class Meta:
        db_table = "projects_applies_statuses"


class RequestStatus(TimeStampModel):
    type                 = models.CharField(max_length=20)
    project_apply_status = models.ForeignKey("ProjectApplyStatus", on_delete=models.CASCADE)

    class Meta:
        db_table = "request_statuses"


class ProjectApplyStack(TimeStampModel):
    project_apply    = models.ForeignKey("ProjectApply", on_delete=models.CASCADE)
    technology_stack = models.ForeignKey("commons.TechnologyStack", on_delete=models.CASCADE)

    class Meta:
        db_table = "projects_applies_stacks"
