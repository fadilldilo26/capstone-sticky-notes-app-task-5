"""
Stickynotes Views Module

Contains the main index view for the Sticky Notes application.
This app serves as an entry point that redirects users to the 
main notes listing page.
"""

from django.shortcuts import redirect


def index(request):
    """
    Main index view for the Sticky Notes application.
    
    Redirects all traffic from the root URL to the /notes 
    endpoint where the full note list is displayed.
    
    Args:
        request (HttpRequest): The incoming HTTP request object.
        
    Returns:
        HttpResponseRedirect: A redirect response to '/notes'.
    """
    return redirect('/notes')