from django.test import TestCase
from .models import Post
# Create your tests here

class BlogTests(TestCase):
    def setUp(self):
        Post.objects.create(
            title='my test title',
            body='just a Test',
        )

    def test_string_representation(self):
        post = Post(title='My entry title')
        self.assertEqual(str(post), post.title)

    def test_post_list_view(self):
        response = self.client.get('/mydkhbt/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'my test title')
        self.assertTemplateUsed(response, 'pages/mydkhbt.html')

    def test_post_detail_view(self):
        response = self.client.get('/mydkhbt/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'my test title')
        self.assertTemplateUsed(response, 'pages/postdkhbt.html')

