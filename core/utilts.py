from enum import Enum


class ApplyStatusType(Enum):
    applicant = 1
    creator   = 2


class PositionRoll(Enum):
    back_end  = 1
    front_end = 2


class RequestType(Enum):
    request = 1
    deny    = 2
    confirm = 3


class ImageType(Enum):
    banner           = 1
    project_thumbnail= 2
    project_detail   = 3
    stack            = 4
    user_profile     = 5


class ProgressStatus(Enum):
    before_start=1
    in_progress =2
    done        =3