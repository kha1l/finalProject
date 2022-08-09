from django.test import TestCase
from .models import Song, Genre


class SongTest(TestCase):
    def test_models(self):
        Genre(
            name='jazz'
        ).save()
        genre = Genre.objects.filter(
            name='jazz'
        )
        self.assertTrue(genre, Genre)
        self.assertEqual(genre[0].name, 'jazz')
        Song(
            author='test_author',
            title='test_title',
            genre=genre[0],
            file='test.mp3',
            user='1'
        ).save()
        list_res = Song.objects.filter(title='test_title')
        self.assertTrue(list_res)
        self.assertEqual(list_res[0].title, 'test_title')
        list_res.delete()
        after_del = Song.objects.filter(title='test_title')
        self.assertFalse(after_del)
        genre.delete()
        genre_list = Genre.objects.filter(name='jazz')
        self.assertFalse(genre_list)
