from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404

tasks = [
    {
        "id": 1,
        "title": "Kill russian-ork",
        "description": "Just do this",
        "created": "2022-01-24 12:00",
        "updated": "2022-01-25 12:00",
        "completed": False
    },
    {
        "id": 2,
        "title": "Hello World",
        "description": "A Good Day to Die Hard",
        "created": "2022-01-24 12:00",
        "updated": "2022-01-25 12:00",
        "completed": True
    },
    {
        "id": 3,
        "title": "Highway to hell",
        "description": "Living easy, lovin' free",
        "created": "2022-01-24 12:00",
        "updated": "2022-01-25 12:00",
        "completed": False
    },
]


def task_list_view(request: HttpRequest):
    ctx = {"object_list": tasks}
    return render(request, "task_list.html", ctx)


def task_details_view(request: HttpRequest, id: int) -> HttpResponse:
    for task in tasks:
        if task["id"] == id:
            return render(request, "task_details.html", {"object": task})
    raise Http404
