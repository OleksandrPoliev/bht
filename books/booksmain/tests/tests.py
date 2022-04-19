import pytest
from ..models import BooksModel
from ..views import Main_View
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

@pytest.fixture
def dbs(db) -> BooksModel:
    return BooksModel.objects.create(title="The Domestic Horse", author="D. S. Mills", publish_date='2005-03-10',
                                         ISBN=9780521891134, num_pages=249,
                                         book_img='http://books.google.com/books/content?id=GHKuEeqC4U0C&printsec=frontcover&img=1&zoom=5&edge=curl&source=gbs_api',
                                         book_language='en')

def test_filter_category(dbs):
    assert BooksModel.objects.filter(title="The Domestic Horse").exists()

def test_update_category(dbs):
    category_from_db = BooksModel.objects.get(ISBN=9780521891134)
    assert category_from_db.ISBN == 9780521891134



class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_details(self):
        request = self.factory.get('/updata/1')
        request.user = AnonymousUser()
        response = Main_View.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_details_v(self):
        request = self.factory.post('sddfs')
        request.user = AnonymousUser()
        response = Main_View.as_view()(request)
        self.assertEqual(response.status_code, '200')






