from django.test import TestCase
from .models import Event, Guest
from django.test.client import Client
from django.contrib.auth.models import User


class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name='1支部会议', status=True, limit=2000, address='软件学院',
                             start_time='2019-08-31 02:18:22')
        Guest.objects.create(id=1, event_id=1, realname='张三', phone='12345678900', email='zhangsan@mail.com',
                             sign=False)

    def test_event_model(self):
        result = Event.objects.filter(name='1支部会议')
        self.assertEqual(result[0].address, '软件学院')
        self.assertTrue(result[0].status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='12345678900')
        self.assertEqual(result.realname, '张三')
        self.assertFalse(result.sign)


class IndexPageTest(TestCase):
    '''index登录首页测试'''

    def test_index_page_renders_index_template(self):
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class LoginActionTest(TestCase):
    '''测试登录函数'''

    def setUp(self):
        User.objects.create_user('auser', 'auser@mail.com', 'auser123456')  # 创建用户
        self.c = Client()

    def test_login_action_username_password_null(self):
        '''用户密码为空'''
        test_data = {'username': '', 'password': ''}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error', response.content)

    def test_login_action_username_password_error(self):
        '''用户名密码错误'''
        test_data = {'username': 'user1', 'password': '987654321'}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'username or password error', response.content)

    def test_login_action_success(self):
        '''登陆成功'''
        test_data = {'username': 'auser', 'password': 'auser123456'}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)


class EventManageTest(TestCase):
    '''会议管理'''

    def setUp(self):
        User.objects.create_user('auser', 'auser@mail.com', 'auser123456')  # 创建用户
        Event.objects.create(id=10, name='aMeeting', limit=2000, status=True, address='SoftwareSchool',
                             start_time='2019-08-31 02:18:22')
        self.c = Client()
        test_data = {'username': 'auser', 'password': 'auser123456'}
        response = self.c.post('/login_action/', data=test_data)

    def test_event_manage_success(self):
        '''测试会议列表'''
        response = self.c.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'aMeeting', response.content)
        self.assertIn(b'SoftwareSchool', response.content)

    def test_event_manage_search_success(self):
        '''测试会议搜索'''
        response = self.c.get('/search_name/', {'name': 'xiaomi6'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'aMeeting', response.content)
        self.assertIn(b'SoftwareSchool', response.content)


class GuestManageTest(TestCase):
    '''参会人员管理'''

    def setUp(self):
        User.objects.create_user('auser', 'auser@mail.com', 'auser123456')  # 创建用户
        Event.objects.create(id=10, name='aMeeting', limit=2000, status=True, address='SoftwareSchool',
                             start_time='2019-08-31 02:18:22')
        Guest.objects.create(event_id=1, realname='zhangsan', phone='12345678900', email='zhangsan@mail.com',
                             sign=False)
        self.c = Client()
        test_data = {'username': 'auser', 'password': 'auser123456'}
        response = self.c.post('/login_action/', data=test_data)

    def test_guest_manage_success(self):
        '''参会人员信息'''
        response = self.c.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'zhangsan', response.content)
        self.assertIn(b'12345678900', response.content)

    def test_guest_manage_search_success(self):
        '''参会人员搜索'''
        response = self.c.get('/search_phone/', {'phone': 12345678900})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'zhangsan', response.content)
        self.assertIn(b'12345678900', response.content)


class SignIndexActionTest(TestCase):
    '''会议签到'''

    def setUp(self):
        User.objects.create_user('auser', 'auser@mail.com', 'auser123456')  # 创建用户
        Event.objects.create(id=1, name='meeting1', limit=2000, status=True, address='SoftwareSchool',
                             start_time='2019-08-31 12:12:22')
        Event.objects.create(id=2, name='meeting2', limit=2000, status=True, address='SoftwareSchool',
                             start_time='2019-08-31 12:56:22')
        Guest.objects.create(event_id=1, realname='zhangsan', phone='12345678900', email='zhangsan@mail.com',
                             sign=False)
        Guest.objects.create(event_id=2, realname='lisi', phone='12345678901', email='lisi@mail.com',
                             sign=True)
        self.c = Client()
        test_data = {'username': 'auser', 'password': 'auser123456'}
        response = self.c.post('/login_action/', data=test_data)

    def test_sign_index_action_phone_null(self):
        '''手机号为空'''
        response = self.c.post('/sign_index_action/1/', {'phone': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'phone error', response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        '''手机号或发布会id错误'''
        response = self.c.post('/sign_index_action/2/', {'phone': '12345678900'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'event id or phone error', response.content)

    def test_sign_index_action_user_sign_has(self):
        '''用户已经签到'''
        response = self.c.post('/sign_index_action/2/', {'phone': '12345678901'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'user has sign in', response.content)

    def test_sign_index_action_sign_success(self):
        '''签到成功'''
        response = self.c.post('/sign_index_action/1/', {'phone': '12345678900'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'sign in success', response.content)
