from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback

def feedback_view(request):
    message_success = None

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            message_success = 'Дякуємо за ваш відгук!'
            form = FeedbackForm()
    else:
        form = FeedbackForm()

    feedbacks = Feedback.objects.all().order_by('-created_at')

    return render(request, 'feedback/feedback.html', {
        'form': form,
        'feedbacks': feedbacks,
        'message_success': message_success
    })

