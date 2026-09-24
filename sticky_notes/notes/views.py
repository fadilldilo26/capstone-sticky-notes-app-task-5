"""
Views Module - Sticky Notes Application

This module contains all view functions for the Sticky Notes application.
It handles HTTP requests for listing, creating, updating, and deleting notes.
"""

from django.shortcuts import render, get_object_or_404, redirect
from .models import Note


def note_list(request):
    """
    Displays a list of all sticky notes.
    
    Retrieves all Note objects from the database and renders them
    in the note_list template.
    
    Args:
        request (HttpRequest): The incoming HTTP request object.
        
    Returns:
        HttpResponse: Rendered HTML page containing all notes.
    """
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


def create_note(request):
    """
    Handles the creation of a new sticky note.
    
    If the request method is POST, it creates a new note with
    the provided title and content, then redirects to the note list view.
    If the request method is GET, it renders the create_note template.
    
    Args:
        request (HttpRequest): The incoming HTTP request object.
        
    Returns:
        HttpResponse: Redirect to notes list on success, or rendered form.
    """
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(title=title, content=content)
        return redirect('notes')
    return render(request, 'notes/create_note.html')


def update_note(request, note_id):
    """
    Handles the updating of an existing sticky note.
    
    Retrieves the note based on the provided note_id.
    If the request method is POST, it updates the note's title and content
    with the provided data, saves the changes, and redirects to the note
    list view. If the request method is GET, it renders the update_note
    template with the current note data.
    
    Args:
        request (HttpRequest): The incoming HTTP request object.
        note_id (int): The primary key of the note to update.
        
    Returns:
        HttpResponse: Redirect to notes list on success, or rendered form.
        
    Raises:
        Http404: If no note exists with the given note_id.
    """
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('notes')
    return render(request, 'notes/update_note.html', {'note': note})


def delete_note(request, note_id):
    """
    Handles the deletion of a sticky note.
    
    Retrieves the note based on the provided note_id.
    If the request method is POST, it deletes the note and redirects
    to the note list view. If the request method is GET, it renders
    the delete_note template with the current note data for confirmation.
    
    Args:
        request (HttpRequest): The incoming HTTP request object.
        note_id (int): The primary key of the note to delete.
        
    Returns:
        HttpResponse: Redirect to notes list after deletion, or confirmation page.
        
    Raises:
        Http404: If no note exists with the given note_id.
    """
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    return render(request, 'notes/delete_note.html', {'note': note})