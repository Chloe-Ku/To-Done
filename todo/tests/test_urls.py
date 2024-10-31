from django.test import SimpleTestCase
from django.urls import reverse, resolve
from todo.views import (
    index, todo_from_template, template_from_todo, delete_todo, 
    template, updateListItem, removeListItem, createNewTodoList, 
    getListItemByName, getListItemById, markListItem, addNewListItem, 
    send_push, checkForNotifications, register_request, 
    login_request, logout_request, password_reset_request
)

# Chat GPT Helped Generate the skeleton for what we should be testing for (Since we need 20 tests per person)
# Additionally, Chat GPT Assisted in the generation of some of these as well and assisted in understanding why certain test cases were failing
class TestURLs(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('todo:index')
        self.assertEqual(resolve(url).func, index)

    def test_todo_url_resolves(self):
        url = reverse('todo:todo')
        self.assertEqual(resolve(url).func, index)

    def test_todo_list_id_url_resolves(self):
        url = reverse('todo:todo_list_id', args=[1])
        self.assertEqual(resolve(url).func, index)

    def test_todo_from_template_url_resolves(self):
        url = reverse('todo:todo_from_template')
        self.assertEqual(resolve(url).func, todo_from_template)

    def test_delete_todo_url_resolves(self):
        url = reverse('todo:delete_todo')
        self.assertEqual(resolve(url).func, delete_todo)

    def test_template_url_resolves(self):
        url = reverse('todo:template')
        self.assertEqual(resolve(url).func, template)

    def test_template_from_todo_url_resolves(self):
        url = reverse('todo:template_from_todo')
        self.assertEqual(resolve(url).func, template_from_todo)

    def test_update_list_item_url_resolves(self):
        url = reverse('todo:updateListItem')
        self.assertEqual(resolve(url).func, updateListItem)

    def test_update_list_item_id_url_resolves(self):
        url = reverse('todo:updateListItem', args=[1])
        self.assertEqual(resolve(url).func, updateListItem)

    def test_remove_list_item_url_resolves(self):
        url = reverse('todo:removeListItem')
        self.assertEqual(resolve(url).func, removeListItem)

    def test_create_new_todo_list_url_resolves(self):
        url = reverse('todo:createNewTodoList')
        self.assertEqual(resolve(url).func, createNewTodoList)

    def test_get_list_item_by_name_url_resolves(self):
        url = reverse('todo:getListItemByName')
        self.assertEqual(resolve(url).func, getListItemByName)

    def test_get_list_item_by_id_url_resolves(self):
        url = reverse('todo:getListItemById')
        self.assertEqual(resolve(url).func, getListItemById)

    def test_mark_list_item_url_resolves(self):
        url = reverse('todo:markListItem')
        self.assertEqual(resolve(url).func, markListItem)

    def test_add_new_list_item_url_resolves(self):
        url = reverse('todo:addNewListItem')
        self.assertEqual(resolve(url).func, addNewListItem)

    def test_send_push_url_resolves(self):
        url = reverse('todo:send_push')
        self.assertEqual(resolve(url).func, send_push)

    def test_check_for_notifications_url_resolves(self):
        url = reverse('todo:checkForNotifications')
        self.assertEqual(resolve(url).func, checkForNotifications)

    def test_register_url_resolves(self):
        url = reverse('todo:register')
        self.assertEqual(resolve(url).func, register_request)

    def test_login_url_resolves(self):
        url = reverse('todo:login')
        self.assertEqual(resolve(url).func, login_request)

    def test_logout_url_resolves(self):
        url = reverse('todo:logout')
        self.assertEqual(resolve(url).func, logout_request)

    def test_password_reset_url_resolves(self):
        url = reverse('todo:password_reset')
        self.assertEqual(resolve(url).func, password_reset_request)

