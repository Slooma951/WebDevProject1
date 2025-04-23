from django.test import TestCase
from django.urls import reverse
from .models import User, Item, Category, Request

class InventoryTestCase(TestCase):
    def setUp(self):
        # Create users
        self.admin = User.objects.create_user(username='admin', password='password', role='Admin')
        self.coach = User.objects.create_user(username='coach', password='password', role='Coach')
        self.player = User.objects.create_user(username='player', password='password', role='Customer')

        # Create category and item
        self.category = Category.objects.create(name='Training Gear')
        self.item = Item.objects.create(name='Football', quantity=10, item_condition='New', category=self.category)

    def test_player_can_request_item(self):
        self.client.login(username='player', password='password')
        response = self.client.get(reverse('request_item', args=[self.item.id]))
        self.assertEqual(Request.objects.count(), 1)
        self.assertRedirects(response, reverse('home'))

    def test_coach_can_approve_request(self):
        # Player makes request
        req = Request.objects.create(user=self.player, item=self.item, status='Pending')
        self.client.login(username='coach', password='password')
        response = self.client.get(reverse('approve_request', args=[req.id]))
        req.refresh_from_db()
        self.assertEqual(req.status, 'Approved')
        self.assertRedirects(response, reverse('coach_requests'))

    def test_home_page_loads(self):
        self.client.login(username='player', password='password')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Available Items')
