import datetime

from freezegun       import freeze_time

from django.test     import TestCase, Client

from projects.models import *
from commons.models  import *
from users.models    import *
from core.utils      import *
from applies.models  import *


class ProjectTest(TestCase):
    maxDiff = None

    @freeze_time("2022-01-01T00:00:00Z")
    def setUp(self):
        ProjectCategory.objects.bulk_create([
            ProjectCategory(
                id    = 1,
                title = "스터디"
            ),
            ProjectCategory(
                id    =2,
                title = "클론코딩"
            ),
            ProjectCategory(
                id    =3,
                title = "대규모"
            ),
            ProjectCategory(
                id    = 4,
                title ="공모전"
            ),
            ProjectCategory(
                id    = 5,
                title = "해커톤"
            )
        ])

        Region.objects.bulk_create([
            Region(
                id            = 1,
                district_name = "강남구"
            ),
            Region(
                id            = 2,
                district_name = "서초구"
            ),
            Region(
                id            = 3,
                district_name = "용산구"
            ),
            Region(
                id            = 4,
                district_name = "동대문구"
            ),
            Region(
                id            = 5,
                district_name = "서대문구"
            ),
            Region(
                id            = 6,
                district_name = "종로구"
            ),
            Region(
                id            = 7,
                district_name = "영등포구"
            ),
            Region(
                id            = 8,
                district_name = "동작구"
            ),
            Region(
                id            = 9,
                district_name = "송파구"
            ),
            Region(
                id            = 10,
                district_name = "마포구"
            )
        ])

        ProgressStatus.objects.bulk_create([
            ProgressStatus(
                id   = 1,
                step = "진행 전"
            ),
            ProgressStatus(
                id   = 2,
                step = "진행 중"
            ),
            ProgressStatus(
                id   = 3,
                step = "진행 완료"
            )
        ])

        StackCategory.objects.bulk_create([
            StackCategory(
                id    = 1,
                title = "applicantion"
            ),
            StackCategory(
                id    = 2,
                title = "data"
            ),
            StackCategory(
                id    = 3,
                title = "devops"
            )
        ])

        TechnologyStack.objects.bulk_create([
            TechnologyStack(
                id                = 1,
                title             = "React",
                color             = "#61DAFB",
                stack_category_id = 1
            ),
            TechnologyStack(
                id                = 2,
                title             = "CSS",
                color             = "#0C75B9",
                stack_category_id = 1
            ),
            TechnologyStack(
                id                = 3,
                title             = "HTML",
                color             = "#E54C25",
                stack_category_id = 1
            ),
            TechnologyStack(
                id                = 4,
                title             = "JavaScript",
                color             = "#FFD939",
                stack_category_id = 1
            ),
            TechnologyStack(
                id                = 5,
                title             = "Python",
                color             = "#3676AB",
                stack_category_id = 1
            ),
            TechnologyStack(
                id                = 6,
                title             = "mysql",
                color             = "#4579A1",
                stack_category_id = 2
            ),
            TechnologyStack(
                id                = 7,
                title             = "django",
                color             = "#0A2E20",
                stack_category_id = 1
            ),
            TechnologyStack(
                id                = 8,
                title             = "git",
                color             = "#F05032",
                stack_category_id = 3
            )
        ])

        ImageType.objects.bulk_create([
            ImageType(
                id    = 1,
                title = "banner"
            ),
            ImageType(
                id    = 2,
                title = "project_thumbnail"
            ),
            ImageType(
                id    = 3,
                title = "project_detail"
            ),
            ImageType(
                id    = 4,
                title = "stack"
            ),
            ImageType(
                id    = 5,
                title = "user_profile"
            )
        ])
        Project.objects.create(
            id                  = 1,
            title               = '1',
            start_recruit       = "2022-05-01",
            end_recruit         = "2022-05-04",
            start_project       = "2022-05-05",
            end_project         = '2022-05-10',
            description         = 'test 1',
            like                = 1,
            hit                 = 2,
            front_vacancy       = 4,
            back_vacancy        = 2,
            is_online           = False,
            progress_status_id  = 1,
            project_category_id = 1,
            region_id           = 1
        )

        ProjectStack.objects.bulk_create([
            ProjectStack(
                id                  = 1,
                project_id          = 1,
                technology_stack_id = 1
            ),
            ProjectStack(
                id                  = 2,
                project_id          = 1,
                technology_stack_id = 2
            )
        ])

        Image.objects.create(
            id                  = 1,
            image_url           = "https://ggsd.s3.ap-northeast-2.amazonaws.com/4d1074a2-c605-46c4-b43f-dae9e499588f",
            image_type_id       = 2,
            project_id          = 1,
            user_id             = None,
            technology_stack_id = None
        )
        Portfolio.objects.bulk_create([
            Portfolio(
                id         = 2,
                file_url   = "https://docs.google.com/",
                is_private = 1
            ),
            Portfolio(
                id         = 10,
                file_url   = "https://docs.google.com/",
                is_private = 1
            ),
        ])
        UserStatus.objects.bulk_create([
            UserStatus(
                id             = 1,
                recruit_status = "프로젝트 구하는 중"
            ),
            UserStatus(
                id             = 2,
                recruit_status = "프로젝트 구하지 않는 중"
            ),
            UserStatus(
                id             = 3,
                recruit_status = "크루 구하는 중"
            ),
        ])

        Position.objects.bulk_create([
            Position(
                id   = 1,
                roll = "back-end"
            ),
            Position(
                id   = 2,
                roll = "front-end"
            )
        ])

        User.objects.bulk_create([
            User(
                id              = 1,
                kakao_id        = 1234567892,
                email           = "test1@gmail.com",
                name            = "임수연",
                batch           = 32,
                hit             = 0,
                like            = 2,
                github_repo_url = "https://github.com/imsooyen",
                portfolio_id    = 10,
                position_id     = 2,
                region_id       = 2,
                user_status_id  = 1,
                nickname        = "임쑤"
            ),
            User(
                id              = 2,
                kakao_id        = 78678923,
                email           = "test2@gmail.com",
                name            = "지기성",
                batch           = 32,
                hit             = 5,
                like            = 3,
                github_repo_url = "https://github.com/jiggy",
                portfolio_id    = 2,
                position_id     = 1,
                region_id       = 3,
                user_status_id  = 2,
                nickname        = "jiggyjiggy"
            )
        ])

        ProjectApplyStatus.objects.bulk_create([
            ProjectApplyStatus(
                id   = 1,
                type = "신청함",
            ),
            ProjectApplyStatus(
                id   = 2,
                type = "생성함",
            )
        ])

        ProjectApply.objects.bulk_create([
            ProjectApply(
                id                      = 1,
                position_id             = 2,
                project_id              = 1,
                project_apply_status_id = 2,
                user_id                 = 1
            ),
            ProjectApply(
                id                      = 2,
                position_id             = 1,
                project_id              = 1,
                project_apply_status_id = 1,
                user_id                 = 2
            ),
        ])

        ProjectApplyStack.objects.bulk_create([
            ProjectApplyStack(
                id                  = 1,
                project_apply_id    = 1,
                technology_stack_id = 1
            ),
            ProjectApplyStack(
                id                  = 2,
                project_apply_id    = 2,
                technology_stack_id = 2
            )
        ])
        RequestStatus.objects.bulk_create([
            RequestStatus(
                id                      = 1,
                type                    = "요청 중",
                project_apply_status_id = 1
            ),
            RequestStatus(
                id                      = 2,
                type                    = "거절댐",
                project_apply_status_id = 1
            ),
            RequestStatus(
                id                      = 3,
                type                    = "수락됌",
                project_apply_status_id = 1
            )
        ])

    def tearDown(self):
        ProjectCategory.objects.all().delete()
        ProgressStatus.objects.all().delete()
        StackCategory.objects.all().delete()
        TechnologyStack.objects.all().delete()
        Project.objects.all().delete()
        ProjectStack.objects.all().delete()
        Image.objects.all().delete()
        ImageType.objects.all().delete()
        Portfolio.objects.all().delete()
        UserStatus.objects.all().delete()
        User.objects.all().delete()
        Region.objects.all().delete()
        ProjectApply.objects.all().delete()
        ProjectApplyStack.objects.all().delete()
        RequestStatus.objects.all().delete()

    def test_project_detail_view_get_method_success(self):
        client   = Client()
        response = client.get("/projects/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "results": [{
                "project": {
                    "title"          : "1",
                    "front_vacancy"  : 4,
                    "back_vacancy"   : 2,
                    "front_fixed"    : 0,
                    "back_fixed"     : 0,
                    "start_recruit"  : "2022-05-01",
                    "end_recruit"    : "2022-05-04",
                    "start_project"  : "2022-05-05",
                    "end_project"    : "2022-05-10",
                    "region"         : "강남구",
                    "is_online"      : False,
                    "description"    : "test 1",
                    "thumbnail"      : ["https://ggsd.s3.ap-northeast-2.amazonaws.com/4d1074a2-c605-46c4-b43f-dae9e499588f"],
                    "category"       : "스터디",
                    "project_stacks" : [
                        {
                            "stack_id" : 1,
                            "title"    : "React",
                            "color"    : "#61DAFB"
                        },
                        {
                            "stack_id" : 2,
                            "title"    : "CSS",
                            "color"    : "#0C75B9"
                        }
                    ],
                    "creators": [
                        {
                            "id"         : 1,
                            "name"       : "임수연",
                            "position"   : "front-end",
                            "github_url" : "https://github.com/imsooyen",
                            "portfolio"  : [
                                {
                                    "file_url"   : None,
                                    "is_private" : True
                                }
                            ]
                        }
                    ],
                    "applicants": [
                        {
                            "id"           : 2,
                            "name"         : "지기성",
                            "position"     : "back-end",
                            "apply_status" : "신청함",
                            "github_url"   : "https://github.com/jiggy",
                            "portfolio"    : [
                                {
                                    "file_url"   : None,
                                    "is_private" : True
                                }
                            ]
                        }
                    ]
                }
            }
        ]})
