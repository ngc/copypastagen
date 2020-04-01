from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import json

post_data = json.load(open("json/data.json"))
print(post_data)

posts = [

    {
        'title': 'TestTestTest',
        'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor non sapien posuere porta sed a leo. Aenean mattis est venenatis nibh maximus, at convallis risus ornare. Praesent tristique risus sed vulputate euismod. Quisque sed vehicula dolor. Phasellus faucibus, odio sit amet commodo blandit, elit turpis dapibus metus, nec tristique tellus risus quis tortor. Pellentesque sodales suscipit felis at posuere. Donec sed elit id felis rutrum dictum sit amet ac dolor.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor non sapien posuere porta sed a leo. Aenean mattis est venenatis nibh maximus, at convallis risus ornare. Praesent tristique risus sed vulputate euismod. Quisque sed vehicula dolor. Phasellus faucibus, odio sit amet commodo blandit, elit turpis dapibus metus, nec tristique tellus risus quis tortor. Pellentesque sodales suscipit felis at posuere. Donec sed elit id felis rutrum dictum sit amet ac dolor.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor non sapien posuere porta sed a leo. Aenean mattis est venenatis nibh maximus, at convallis risus ornare. Praesent tristique risus sed vulputate euismod. Quisque sed vehicula dolor. Phasellus faucibus, odio sit amet commodo blandit, elit turpis dapibus metus, nec tristique tellus risus quis tortor. Pellentesque sodales suscipit felis at posuere. Donec sed elit id felis rutrum dictum sit amet ac dolor.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor non sapien posuere porta sed a leo. Aenean mattis est venenatis nibh maximus, at convallis risus ornare. Praesent tristique risus sed vulputate euismod. Quisque sed vehicula dolor. Phasellus faucibus, odio sit amet commodo blandit, elit turpis dapibus metus, nec tristique tellus risus quis tortor. Pellentesque sodales suscipit felis at posuere. Donec sed elit id felis rutrum dictum sit amet ac dolor.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor non sapien posuere porta sed a leo. Aenean mattis est venenatis nibh maximus, at convallis risus ornare. Praesent tristique risus sed vulputate euismod. Quisque sed vehicula dolor. Phasellus faucibus, odio sit amet commodo blandit, elit turpis dapibus metus, nec tristique tellus risus quis tortor. Pellentesque sodales suscipit felis at posuere. Donec sed elit id felis rutrum dictum sit amet ac dolor.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor non sapien posuere porta sed a leo. Aenean mattis est venenatis nibh maximus, at convallis risus ornare. Praesent tristique risus sed vulputate euismod. Quisque sed vehicula dolor. Phasellus faucibus, odio sit amet commodo blandit, elit turpis dapibus metus, nec tristique tellus risus quis tortor. Pellentesque sodales suscipit felis at posuere. Donec sed elit id felis rutrum dictum sit amet ac dolor.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor non sapien posuere porta sed a leo. Aenean mattis est venenatis nibh maximus, at convallis risus ornare. Praesent tristique risus sed vulputate euismod. Quisque sed vehicula dolor. Phasellus faucibus, odio sit amet commodo blandit, elit turpis dapibus metus, nec tristique tellus risus quis tortor. Pellentesque sodales suscipit felis at posuere. Donec sed elit id felis rutrum dictum sit amet ac dolor.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor non sapien posuere porta sed a leo. Aenean mattis est venenatis nibh maximus, at convallis risus ornare. Praesent tristique risus sed vulputate euismod. Quisque sed vehicula dolor. Phasellus faucibus, odio sit amet commodo blandit, elit turpis dapibus metus, nec tristique tellus risus quis tortor. Pellentesque sodales suscipit felis at posuere. Donec sed elit id felis rutrum dictum sit amet ac dolor."
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'main/index.html', context)