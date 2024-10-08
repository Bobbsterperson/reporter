from django.shortcuts import render, redirect
from .forms import SubmissionForm
from .models import Submission

def home(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SubmissionForm()

    submissions = Submission.objects.all().order_by('-submitted_at')
    return render(request, 'jornal/home.html', {'form': form, 'submissions': submissions})
