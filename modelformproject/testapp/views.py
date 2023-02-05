from django.shortcuts import render

# Create your views here.
from testapp.forms import StudentForm
def student_view(request):
	form = StudentForm()
	if request.method == 'POST':
	   form = StudentForm(request.POST)
	   if form.is_valid():
		   form.save()
		   print('Records Inserted into D/B sucessfully')
		   form = StudentForm()
	return render(request, 'testapp/studentform.html', {'form':form})
