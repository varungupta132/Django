from django.shortcuts import render , redirect

# Create your views here.
from django.http import HttpResponse
from .utils import send_email_to_client , send_email_with_attachment

# def home(request):
#     names={"name" :  {"age":25},"nam":{"age":18}}
#     return render(request,'index.html',{"names":names})

# def home(request):
#     names={"name" :  {"age":25},"nam":{"age":18}}
#     return render(request,'varun 01/index.html',{"names":names})

def home(request):
    return render(request,'varun 01/index.html')    
def success_page(request):
    return HttpResponse("<h1>successfully varun gupta </h1>")


# def send_email(request):
#     send_email_to_client()
#     return redirect("/")

def send_email(request):
    subject = "This email is from Django server with Attachment"
    message = "Hey please find this attach file with this email"
    recipient_list = ["guptavarun132@gmail.com"]
    file_path = r"C:\Users\gupta\OneDrive\Desktop\AIML SECTION.xlsx"
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/')