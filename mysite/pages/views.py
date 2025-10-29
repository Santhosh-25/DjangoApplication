from django.shortcuts import render, redirect
from .forms import ProjectForm

def project_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  # ✅ request.FILES added
        if form.is_valid():
            form.save()
            return redirect('pages_project_add')
    else:
        form = ProjectForm()
    return render(request, 'pages/project_add.html', {'form': form})
