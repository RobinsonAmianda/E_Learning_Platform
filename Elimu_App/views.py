from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Question, Student, Tutorial, Instructor, Topic, Result
from django.utils.timezone import now

# === COURSE CRUD ===
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        instructor = request.POST['instructor']
        image = request.FILES.get('image')
        Course.objects.create(title=title, description=description, instructor=instructor, image=image)
        return redirect('course_list')
    return render(request, 'course_form.html')

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.title = request.POST['title']
        course.description = request.POST['description']
        course.instructor = request.POST['instructor']
        course.image = request.FILES.get('image', course.image)
        course.save()
        return redirect('course_list')
    return render(request, 'course_form.html', {'course': course})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        course.delete()
        return redirect('course_list')
    return render(request, 'course_confirm_delete.html', {'course': course})

# === QUESTION CRUD ===
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'question_list.html', {'questions': questions})

def question_create(request):
    if request.method == "POST":
        category = request.POST['category']
        question = request.POST['question']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer = request.POST['answer']
        Question.objects.create(
            category=category, question=question, option1=option1, option2=option2,
            option3=option3, option4=option4, answer=answer
        )
        return redirect('question_list')
    return render(request, 'question_form.html')

def question_update(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        question.category = request.POST['category']
        question.question = request.POST['question']
        question.option1 = request.POST['option1']
        question.option2 = request.POST['option2']
        question.option3 = request.POST['option3']
        question.option4 = request.POST['option4']
        question.answer = request.POST['answer']
        question.save()
        return redirect('question_list')
    return render(request, 'question_form.html', {'question': question})

def question_delete(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        question.delete()
        return redirect('question_list')
    return render(request, 'question_confirm_delete.html', {'question': question})

# === STUDENT CRUD ===
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        image = request.FILES.get('image')
        Student.objects.create(name=name, email=email, mobile=mobile, image=image)
        return redirect('student_list')
    return render(request, 'student_form.html')

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.mobile = request.POST['mobile']
        student.image = request.FILES.get('image', student.image)
        student.save()
        return redirect('student_list')
    return render(request, 'student_form.html', {'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

def tutorial_list(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'tutorial_list.html', {'tutorials': tutorials})

def tutorial_create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        video = request.FILES.get('video')
        Tutorial.objects.create(title=title, description=description, video=video)
        return redirect('tutorial_list')
    return render(request, 'tutorial_form.html')

def tutorial_update(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if request.method == "POST":
        tutorial.title = request.POST['title']
        tutorial.description = request.POST['description']
        tutorial.video = request.FILES.get('video', tutorial.video)
        tutorial.save()
        return redirect('tutorial_list')
    return render(request, 'tutorial_form.html', {'tutorial': tutorial})

def tutorial_delete(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if request.method == "POST":
        tutorial.delete()
        return redirect('tutorial_list')
    return render(request, 'tutorial_confirm_delete.html', {'tutorial': tutorial})

def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructor_list.html', {'instructors': instructors})

def instructor_create(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        image = request.FILES.get('image')
        Instructor.objects.create(name=name, email=email, mobile=mobile, image=image)
        return redirect('instructor_list')
    return render(request, 'instructor_form.html')

def instructor_update(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == "POST":
        instructor.name = request.POST['name']
        instructor.email = request.POST['email']
        instructor.mobile = request.POST['mobile']
        instructor.image = request.FILES.get('image', instructor.image)
        instructor.save()
        return redirect('instructor_list')
    return render(request, 'instructor_form.html', {'instructor': instructor})

def instructor_delete(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == "POST":
        instructor.delete()
        return redirect('instructor_list')
    return render(request, 'instructor_confirm_delete.html', {'instructor': instructor})

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'topic_list.html', {'topics': topics})

def topic_create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        Topic.objects.create(title=title, description=description)
        return redirect('topic_list')
    return render(request, 'topic_form.html')

def topic_update(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        topic.title = request.POST['title']
        topic.description = request.POST['description']
        topic.save()
        return redirect('topic_list')
    return render(request, 'topic_form.html', {'topic': topic})

def topic_delete(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        topic.delete()
        return redirect('topic_list')
    return render(request, 'topic_confirm_delete.html', {'topic': topic})

def result_list(request):
    results = Result.objects.all()
    return render(request, 'result_list.html', {'results': results})

def result_create(request):
    if request.method == "POST":
        username = request.POST['username']
        topic_name = request.POST['topic_name']
        good = request.POST.get('good') == "on"  # Checkbox values
        fail = request.POST.get('fail') == "on"
        marks = request.POST['marks']
        Result.objects.create(username=username, topic_name=topic_name, good=good, fail=fail, marks=marks, date=now())
        return redirect('result_list')
    return render(request, 'result_form.html')

def result_update(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == "POST":
        result.username = request.POST['username']
        result.topic_name = request.POST['topic_name']
        result.good = request.POST.get('good') == "on"
        result.fail = request.POST.get('fail') == "on"
        result.marks = request.POST['marks']
        result.date = now()
        result.save()
        return redirect('result_list')
    return render(request, 'result_form.html', {'result': result})

def result_delete(request, pk):
    result = get_object_or_404(Result, pk=pk)
    if request.method == "POST":
        result.delete()
        return redirect('result_list')
    return render(request, 'result_confirm_delete.html', {'result': result})
