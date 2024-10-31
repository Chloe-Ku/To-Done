from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from todo.models import List, ListItem, Template, TemplateItem, ListTags, SharedUsers, SharedList

# Chat GPT Helped Generate the skeleton for what we should be testing for (Since we need 20 tests per person)
# Additionally, Chat GPT Assisted in the generation of some of these as well and assisted in understanding why certain test cases were failing
class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jacob', email='jacob@example.com', password='top_secret')
        self.todo_list = List.objects.create(
            title_text="Test List",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user,
            list_tag="Test Tag"
        )
        self.list_item = ListItem.objects.create(
            item_name="Test Item",
            item_text="This is a test list item",
            created_on=timezone.now(),
            finished_on=timezone.now(),
            due_date=timezone.now(),
            tag_color="#f9f9f9",
            list=self.todo_list,
            is_done=False
        )
        self.template = Template.objects.create(
            title_text="Test Template",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user
        )
        self.template_item = TemplateItem.objects.create(
            item_text="Sample Template Item",
            created_on=timezone.now(),
            template=self.template,
            finished_on=timezone.now(),
            tag_color="#f9f9f9",
            due_date=timezone.now()
        )
        self.list_tag = ListTags.objects.create(
            user_id=self.user,
            tag_name="Urgent",
            created_on=timezone.now()
        )
        self.shared_user = SharedUsers.objects.create(
            list_id=self.todo_list,
            shared_user="testuser2"
        )
        self.shared_list = SharedList.objects.create(
            user=self.user,
            shared_list_id="123456"
        )

    def test_list_str(self):
        self.assertEqual(str(self.todo_list), "Test List")

    def test_list_creation(self):
        test_list = List.objects.create(
            title_text="Another Test List",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user
        )
        self.assertEqual(test_list.title_text, "Another Test List")
        self.assertFalse(test_list.is_shared)

    def test_list_tag_creation(self):
        self.assertEqual(str(self.list_tag), "Urgent")

    def test_list_item_str(self):
        self.assertEqual(str(self.list_item), "This is a test list item: False")

    def test_list_item_delay_calculation(self):
        self.list_item.finished_on = timezone.now() + timezone.timedelta(days=3)
        self.list_item.due_date = timezone.now()
        self.list_item.is_done = True
        self.list_item.calculate_delay()
        self.assertEqual(self.list_item.delay, 3)

    def test_list_item_completion_time_calculation(self):
        self.list_item.created_on = timezone.now() - timezone.timedelta(days=2)
        self.list_item.finished_on = timezone.now()
        self.list_item.is_done = True
        self.list_item.calculate_completion_time()
        self.assertEqual(self.list_item.completion_time, 2)

    def test_template_str(self):
        self.assertEqual(str(self.template), "Test Template")

    def test_template_item_str(self):
        self.assertEqual(str(self.template_item), "Sample Template Item")

    def test_shared_users_creation(self):
        self.assertEqual(str(self.shared_user), str(self.todo_list))

    def test_shared_list_creation(self):
        self.assertEqual(str(self.shared_list), str(self.user))

    def test_shared_list_str(self):
        self.assertEqual(str(self.shared_list), str(self.user))

    def test_list_default_is_shared(self):
        new_list = List.objects.create(
            title_text="Default Shared Status",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user
        )
        self.assertFalse(new_list.is_shared)

    def test_template_item_due_date(self):
        self.assertIsNotNone(self.template_item.due_date)
    
    def test_list_item_delay_on_time(self):
        self.list_item.finished_on = self.list_item.due_date
        self.list_item.is_done = True
        self.list_item.calculate_delay()
        self.assertEqual(self.list_item.delay, 0)

    def test_list_item_no_completion_time_if_not_done(self):
        self.list_item.is_done = False
        self.list_item.calculate_completion_time()
        self.assertEqual(self.list_item.completion_time, 0)

    def test_update_list_tag_name(self):
        self.list_tag.tag_name = "High Priority"
        self.list_tag.save()
        self.assertEqual(ListTags.objects.get(id=self.list_tag.id).tag_name, "High Priority")

    def test_template_item_str_with_finished_on(self):
        self.template_item.finished_on = timezone.now()
        self.template_item.save()
        self.assertEqual(str(self.template_item), "Sample Template Item")

    def test_shared_user_str(self):
        self.assertEqual(str(self.shared_user), str(self.todo_list))

    def test_list_shared_property(self):
        self.todo_list.is_shared = True
        self.todo_list.save()
        self.assertTrue(List.objects.get(id=self.todo_list.id).is_shared)

    def test_template_str_with_updated_title(self):
        self.template.title_text = "Updated Template Title"
        self.template.save()
        self.assertEqual(str(Template.objects.get(id=self.template.id)), "Updated Template Title")

    def test_multiple_templates(self):
        template2 = Template.objects.create(
            title_text="Second Template",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user
        )
        templates = Template.objects.filter(user_id=self.user)
        self.assertEqual(templates.count(), 2)
        self.assertIn(template2, templates)
