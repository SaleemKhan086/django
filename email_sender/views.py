from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
# Create your views here.from django.views import View
class sendMailView(View):
    error=None
    def get(self, request):
        print("in get..")
        print(self.error)
        return render(request,"email_sender/send_mail_template.html",{"error":self.error});

    def post(self, request):
        from_address="saleemkanjla786@gmail.com"
        data = request.POST;
        to_address = data['to_address']
        l = [to_address,]
        subject = data['subject']
        msg = data['message']
        try:
            code = send_mail(subject,msg,from_address,l,fail_silently=False)
            print("mail sent" )
            print(code)
            return HttpResponse("sent successfully")
        except:
            print("mail not sent")
            self.error="Mail not sent!!"
            return self.get(request)
