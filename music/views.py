from django.shortcuts import render, redirect
from django.views import View
from .forms import UploadSongForm
from .models import Song, Genre
from django.db.models import Q


class MainPage(View):
    @staticmethod
    def get(request, **kwargs):
        return render(request, 'music/head.html')


class UploadFile(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            form = UploadSongForm()
            return render(self.request, 'music/upload.html', {'form': form})
        else:
            return redirect('logon')

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            form = UploadSongForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                data['user'] = self.request.user.id
                Song(
                    author=data['author'],
                    title=data['title'],
                    genre=data['genre'],
                    file=data['file'],
                    user=data['user']
                ).save()
            songs = Song.objects.filter(user=self.request.user.id).order_by('-id')[0]
            form = UploadSongForm()
            return render(self.request, 'music/upload.html', {'form': form, 'songs': songs})
        else:
            return redirect('logon')


class SelectMySong(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            songs = Song.objects.filter(user=self.request.user.id)
            return render(self.request, 'music/music.html', {'songs': songs})
        else:
            return redirect('logon')

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            song_id = self.request.POST.get('song_id')
            Song.objects.filter(pk=song_id).delete()
            songs = Song.objects.filter(user=self.request.user.id)
            return render(self.request, 'music/music.html', {'songs': songs})
        else:
            return redirect('logon')


class SelectSongs(View):
    def get(self, request, **kwargs):
        if self.request.user.is_authenticated:
            title_list = []
            author_list = []
            user_song = Song.objects.filter(user=self.request.user.id)
            for i in user_song:
                title_list.append(i.title)
                author_list.append(i.author)
            songs = Song.objects.exclude(Q(title__in=title_list) | Q(author__in=author_list))
            return render(request, 'music/search.html', {'songs': songs, 'check': 0})
        else:
            return redirect('logon')

    def post(self, request, **kwargs):
        if self.request.user.is_authenticated:
            song_id = request.POST.get('song_id')
            song = Song.objects.get(pk=song_id)
            title = song.title
            user = self.request.user.id
            genre_id = Genre.objects.get(name=song.genre)
            Song(
                author=song.author,
                title=title,
                genre=genre_id,
                file=song.file,
                user=user
            ).save()
            songs = Song.objects.exclude(Q(title=title) | Q(author=song.author))
            return render(request, 'music/search.html', {'songs': songs})
        else:
            return redirect('logon')
