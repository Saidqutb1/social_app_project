from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from .models import Chat, Message
from django.db.models import Q

# Create your views here.

User = get_user_model()


@login_required
def search_users(request):
    query = request.GET.get('q')
    users = User.objects.filter(Q(username__icontains=query) | Q(email__icontains=query)) if query else []
    return render(request, 'chats/search.html', {'users': users})


@login_required
def chat_view(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    chat = Chat.objects.filter(participants=request.user).filter(participants=other_user).first()

    if not chat:
        chat = Chat.objects.create()
        chat.participants.add(request.user, other_user)

    messages = Message.objects.filter(chat=chat).order_by('timestamp')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(chat=chat, sender=request.user, content=content)
            return redirect('chats:chat_view', user_id=user_id)

    return render(request, 'chats/chat.html', {'chat': chat, 'messages': messages})


@login_required
def chat_list(request):
    chats = Chat.objects.filter(participants=request.user)
    return render(request, 'chats/chat_list.html', {'chats': chats})


