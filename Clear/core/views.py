from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html",
        {
            "title": "Django example",
        },
    )

# Hi its libby
# Hi its toby
