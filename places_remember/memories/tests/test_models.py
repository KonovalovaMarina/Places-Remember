from django.db.utils import IntegrityError
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Memory


class MemoryModelTest(TestCase):

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

    def test_title_length(self):
        memories = Memory.objects.all()
        for memory in memories:
            self.assertEqual(memory._meta.get_field('title').max_length, 80)

    def test_memory_str(self):
        memory = Memory.objects.get(id=1)
        memory_str = (f"User: {memory.user.first_name} {memory.user.last_name}, "
                      f"Location: {memory.location}, Title: {memory.title}, "
                      f"Description: {memory.description}")
        self.assertEqual(str(memory), memory_str)

    def test_nullable_fields(self):
        user = User.objects.get(id=2)
        try:
            a = Memory.objects.create(
                user=user,
                location=None,
                title=None,
                description=None
            )
            a.save()
        except IntegrityError:
            self.assertTrue(True)
