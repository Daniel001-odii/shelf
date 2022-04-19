from django.test import TestCase
from .models import User
# Create your tests here.
class ProfileViewTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="user1", email="user1@gmail.com", password="1234"
        )
        self.user2 = User.objects.create_user(
            username="user2", email="user2@gmail.com", password="1234"
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse(
            "users:profile", kwargs=({"username": self.user1.username}))
        )

        self.assertRedirects(
            response, "/users/login/?next=/users/profile/user1/")

    def test_returns_200(self):
        self.client.login(email="user1@gmail.com", password="1234")
        response = self.client.get(reverse(
            "users:profile", kwargs=({"username": self.user1.username})
        ))

        self.assertEqual(response.status_code, 200)

    def test_view_returns_profile_of_current_user(self):
        self.client.login(email="user1@gmail.com", password="1234")
        response = self.client.get(reverse(
            "users:profile", kwargs=({"username": self.user1.username}))
        )
        # Check we got the profile of the current user
        self.assertEqual(response.context["user"], self.user1)
        self.assertEqual(response.context["profile"], self.user1.profile)

    def test_view_returns_profile_of_a_given_user(self):
        self.client.login(email="user1@gmail.com", password="1234")
        # access the profile of the user 'user'
        response = self.client.get(reverse(
            "users:profile", kwargs=({"username": self.user2.username}))
        )
        self.assertEqual(response.context["user"], self.user2)
        # Check we got the profile of the user 'user2'
        self.assertEqual(response.context["profile"], self.user2.profile)