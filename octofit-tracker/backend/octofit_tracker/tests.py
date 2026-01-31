from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create(name='Test User', email='test@example.com', team=t)
        self.assertEqual(str(u), 'Test User')
    def test_activity_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create(name='Test User', email='test@example.com', team=t)
        a = Activity.objects.create(user=u, type='Run', duration=10, date='2026-01-31')
        self.assertEqual(a.type, 'Run')
    def test_workout_create(self):
        w = Workout.objects.create(name='Test Workout', description='desc', suggested_for='All')
        self.assertEqual(str(w.name), 'Test Workout')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='Test Team')
        l = Leaderboard.objects.create(team=t, points=100)
        self.assertEqual(l.points, 100)
