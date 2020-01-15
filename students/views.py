from django.shortcuts import render

# Create your views here.
def student_leave(request):
    if request.method=='POST':
        leave_type=request.POST.get('leave')
        leave_day=request.POST.get('day')
        leave_on=request.POST.get('leave_on')
        leave_session=request.POST.get('session')
        leave_reason=request.POST.get('reason')
        leave_discription=request.POST.get('message')
        a=leave(leave_type=leave_type,leave_day=leave_day,leave_on=leave_on,leave_reason=leave_reason,leave_discription=leave_discription)
        a.save()
    return render(request,'student-leave-management.html')
    