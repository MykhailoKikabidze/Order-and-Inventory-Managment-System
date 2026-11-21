from django.test import Client, TestCase  # type: ignore[reportMissingImports]


class AdminTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_admin_login_page(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)

