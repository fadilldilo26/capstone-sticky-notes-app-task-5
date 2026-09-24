"""
Notes Model Module - Sticky Notes Application

This module defines the data models for the Sticky Notes application.
It contains the Note model which represents individual sticky notes
stored in the database.
"""

from django.db import models


class Note(models.Model):
    """
    Represents a single sticky note in the application.
    
    Each note has a title, content body, and automatic timestamp
    for when it was created.
    
    Attributes:
        title (CharField): The headline/title of the note (max 200 chars).
        content (TextField): The main body text of the note.
        created_at (DateTimeField): Automatic timestamp set when note is created.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the note.
        
        Returns:
            str: The title of the note.
        """
        return self.title