import datetime

from freezegun import freeze_time

from django.test     import TestCase, Client

from projects.models import *
from commons.models  import *


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
                title             ="Python",
                color             ="#3676AB",
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
                id=1,
                title="banner"
            ),
            ImageType(
                id=2,
                title="project_thumbnail"
            ),
            ImageType(
                id=3,
                title="project_detail"
            ),
            ImageType(
                id=4,
                title="stack"
            ),
            ImageType(
                id=5,
                title="user_profile"
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
            region_id           = 1,
        )

        ProjectStack.objects.bulk_create([
            ProjectStack(
                id                 = 1,
                project_id         = 1,
                technology_stack_id= 1
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

    def tearDown(self):
        ProjectCategory.objects.all().delete()
        Region.objects.all().delete()
        ProgressStatus.objects.all().delete()
        StackCategory.objects.all().delete()
        TechnologyStack.objects.all().delete()
        Project.objects.all().delete()
        ProjectStack.objects.all().delete()
        Image.objects.all().delete()
        ImageType.objects.all().delete()

    def test_project_list_view_get_method_success(self):
        client   = Client()
        response = client.get("/projects")

        self.assertEqual(response.json(), {
            "results": [{
                "today"       : datetime.date.today().strftime("%Y-%m-%d"),
                "end_recruit" : "2022-05-04",
                "created_at"  : "2022-01-01T00:00:00Z",
                "sort"        : {
                    "default_sort"   : "-created_at",
                    "recent_created" : "-created_at",
                    "deadline"       : "-end_recruit"
                },
                "page_title" : None,
                "project_id" : 1,
                "category"   : "스터디",
                "title"      : "1",
                "thumbnail"  : ["https://ggsd.s3.ap-northeast-2.amazonaws.com/4d1074a2-c605-46c4-b43f-dae9e499588f"],
                "stacks"     : [
                    {
                        "id"    : 1,
                        "title" : "React",
                        "color" : "#61DAFB"
                    },
                    {
                        "id"    : 2,
                        "title" : "CSS",
                        "color" : "#0C75B9"
                    }
                ]
            }]
        })
        self.assertEqual(response.status_code, 200)