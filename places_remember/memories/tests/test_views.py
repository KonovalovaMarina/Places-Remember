from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Memory


class ViewsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        test_user1 = User.objects.create_user(
            username='User1',
            first_name='First name 1',
            last_name='Last name 1'
        )
        test_user2 = User.objects.create_user(
            username='User2',
            first_name='First name 2',
            last_name='Last name 2'
        )
        Memory.objects.create(
            user=test_user1,
            location='Екатеринбург, Тургенева 4',
            title='Название1',
            description='Описание1'
        )
        Memory.objects.create(
            user=test_user2,
            location='Екатеринбург, Тургенева 4',
            title='Название2',
            description='Описание2'
        )

    def setUp(self):
        self.user = User.objects.get(username='User1')

    def test_get_home_status_code(self):
        self.client.force_login(self.user)
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_get_home_empty_list_memories(self):
        self.client.force_login(self.user)
        response = self.client.get('/home/')
        self.assertEqual(str(response.context['memories'][0]),
                         (f"User: First name 1 Last name 1, "
                          f"Location: Екатеринбург, Тургенева 4, Title: Название1, "
                          f"Description: Описание1"))

    def test_add_memory_status_code(self):
        self.client.force_login(self.user)
        response = self.client.post('/add_memory/')
        self.assertEqual(response.status_code, 200)

    def test_add_memory(self):
        self.client.force_login(self.user)
        memories_count_before = Memory.objects.filter(user=self.user).all().count()
        data = {'location': 'Екатеринбург, Мира 19', 'title': '123', 'description': '123'}
        response = self.client.post('/add_memory/', data=data)
        memories_count_after = Memory.objects.filter(user=self.user).all().count()
        self.assertEqual(memories_count_after, memories_count_before + 1)

    def test_delete_memory_status_code(self):
        self.client.force_login(self.user)
        memory = Memory.objects.get(user=self.user)
        response = self.client.get('/delete_memory/'+str(memory.id))
        self.assertEqual(response.status_code, 302)

    def test_delete_memory(self):
        self.client.force_login(self.user)
        memory = Memory.objects.get(user=self.user)
        response = self.client.get('/delete_memory/'+str(memory.id))
        memory_del = Memory.objects.filter(id=memory.id).first()
        self.assertIsNone(memory_del)
