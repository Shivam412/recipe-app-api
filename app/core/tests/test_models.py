from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """ Test creating a new user with an email is successful """
        email = 'shivam@mail.com'
        password = 'pass@123'
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test the email for the new user is normalized """
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email=email,
                                                    password="Password@1234")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Test creating user with no email raises error """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Pass@1234')

    def test_create_new_super_user(self):
        """ Test creating a new super user """
        user = get_user_model().objects.create_superuser(
            email='test@company.com', password='pass@123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
