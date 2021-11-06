from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Albums List
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                    {"albums": albums})

# add to Albums List
def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/add_album.html", {"form": form})

#edit Album
def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "albums/edit_album.html", {
                "form": form,
                "album": album
    })

#delete Album
def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect(to='list_albums')
    return render(request, "albums/delete_contact.html",
                    {"album": album})

#view individual Album
def view_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/view_album.html", {"album": album})