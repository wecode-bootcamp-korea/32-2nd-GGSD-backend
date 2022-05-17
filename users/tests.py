
import json, jwt

from django.conf import settings
from django.test import TestCase, Client
from django.db   import transaction

from unittest.mock import patch, MagicMock

from commons.models import Image, ImageType
from users.models   import User

class KakaoLoginTest(TestCase):
    def setUp(self):
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
        
        with transaction.atomic():
            ImageType.objects.create(
                title = 'banner'
            )
            User.objects.create(
                id = 1,
                kakao_id      = 2238479606,
                email         = "isyqwer1@gmail.com",
                name          = "수연"
            )
            Image.objects.create(
                user_id = 1,
                image_url = "http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg",
                image_type_id = 1
            )

    def tearDown(self):
        
        with transaction.atomic():
            
            User.objects.all().delete()
            Image.objects.all().delete()
        
        
    @patch("users.views.requests.get")
    def test_kakao_signin_success(self, mocked_kakao_user_info):
        c = Client()
        
        class MockedResponse:
            def json(self):
                return{
                    "id" : 2238479606,
                    "kakao_account": {
                        "profile": {
                                "nickname": "수연",
                                "profile_image_url": "http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg",
                                },
                        "email" : "isyqwer1@gmail.com",
                    }  
                }
                
        mocked_kakao_user_info.return_value = MockedResponse()

        headers  = {"Authorization": "가짜 access_token"}
        
        response = c.get("/users/login", **headers)
        
        user_id = jwt.decode(response.json()['ACCESS_TOKEN'], settings.SECRET_KEY, settings.ALGORITHM)    
            
        access_token = jwt.encode({'id':user_id['id']}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS', 'access_token' : access_token})
        
        
    @patch("users.views.requests.get")
    def test_kakao_signup_success(self, mocked_kakao_user_info):
        c = Client()
        
        class MockedResponse:
            def json(self):
                return {
                    "id": 2238479606,
                    "kakao_account": {
                        "profile": {
                            "nickname": "수연",
                            "profile_image_url": "http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg",
                        },
                        "email" : "isyqwer1@gmail.com",
                    }
                }
                
        mocked_kakao_user_info.return_value = MockedResponse()
        
        headers  = {"Authorization": "가짜 access_token"}
        
        response = c.get("/users/login", **headers)
        
        user_id = jwt.decode(response.json()['access_token'], settings.SECRET_KEY, settings.ALGORITHM)    
            
        access_token = jwt.encode({'id':user_id['id']}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'MESSAGE' : 'SUCCESS', "access_token" : access_token})