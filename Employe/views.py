from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import Context
from django.template.loader import get_template
from django.views.generic import *
from Employe.models import *

class search_job(CreateView):
    model = search
    template_name = "index.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        con = super(search_job, self).get_context_data(**kwargs)
        con['logged_in'] = self.request.user.is_authenticated()
        if(con['logged_in']==True):
            k = user_rights.objects.all().filter(user_id=self.request.user.id)[0].type
            con['rights'] = k
        else:
            con['rights'] = 0
        return con

    def get_success_url(self):
        return reverse("job",kwargs={'location':self.object.location,'sector':self.object.sector,'range':self.object.salary_range})

class get_jobs(ListView):
    model = Recruiter
    template_name = "jobs.html"

    def get_context_data(self, **kwargs):
        con = super(get_jobs, self).get_context_data(**kwargs)
        location = str(self.kwargs['location'])
        salary = int(self.kwargs['range'])
        sector = str(self.kwargs['sector'])
        jobs = Recruiter.objects.all().filter(location__icontains=location,salary__gte=salary,sector=sector)
        con['jobs'] = jobs
        return con

class add_job(CreateView):
    model = Recruiter
    template_name = "regietr2.html"
    fields = "__all__"

    def get_context_data(self, **kwargs):
        con = super(add_job, self).get_context_data(**kwargs)
        k = user_rights.objects.all().filter(user_id=self.request.user.id)[0].type
        con['rights'] = k
        return con

    def get_success_url(self):
        return reverse("finale", kwargs={'stats':'success'})

def status(response,stats):
    t = get_template("ack.html")
    _html = t.render(Context({'status': stats}))
    return HttpResponse(_html)

def register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        type = request.POST['type']
        if form.is_valid():
            new_user = form.save()
            msg="""
            <html>
            <head><title>Success</title>
            <script>
            window.location.href='/';
            </script>
            </head>
            <body>
            Registered Successfully... Redirecting to home page...
            </body>
            </html>
            """
            curr_user_id = User.objects.all().filter(username=request.POST['username'])[0].id
            rights = 0
            if type=="main":
                rights = 1
            temp = user_rights(user_id=curr_user_id,type=rights)
            temp.save()
            return HttpResponse(msg)
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })

def get_description(request,jobid):
    content = Recruiter.objects.all().filter(id=jobid)[0]
    contact = content.contact
    content = content.description
    msg="""
    <html>
    <head>
    <script>

    function show(matter) {
        $("#popup").show();
        $("#outer").load("/about/"+matter);
    }
    </script>
    </head>
    <body><h3 style="color:#179b77;">About<br></h3>
    """+content+"""<br><h3 style="color:#179b77;">Address<br></h3>"""+contact+"""
    </body>
    </html>
    """
    return HttpResponse(msg)

def get_jobs_list(request,search):
    content = set()
    content = Recruiter.objects.all().filter(recruiter__icontains=search)
    content1 = Recruiter.objects.all().filter(location__icontains = search)
    content2 = Recruiter.objects.all().filter(title__icontains = search)
    there = False
    msg="""
    <html>
    <head>
    <title>"""+str(search).capitalize()+"""</title>
    </head><div align='center'><div class="popup" id="popup">
    <span id="close" class="close" onclick="$('#popup').fadeToggle()">X</span>
    <div class="outer" id="outer"></div>
</div>
    """
    for x in content:
        there = True
        msg+="""
        <div class="card text-xs-center" style="width: 400px;display:inline-block;margin-right: 2px;margin-top: 40px;">
  <div class="card-header" style="color:white;background-color:rgba(19, 35, 47, 0.9);">
    <h3>"""+x.recruiter+"""</h3>
  </div>
  <div class="card-block">
    <h4 class="card-title"><b>Job</b> : """+x.title+"""</h4>
      <p class="card-text"><b>Salary</b> : """+str(x.salary)+"""</p>
      <p class="card-text"><b>Job type</b> : """+x.job_type+"""</p>
    <a href="javascript:void(0);" class="mdl-button" onclick="show("""+str(x.id)+""")">Details</a>
  </div>
  <div class="card-footer text-muted">
    2 days ago
  </div>
</div>
        """
    for x in content1:
        there = True
        msg += """
                <div class="card text-xs-center" style="width: 400px;display:inline-block;margin-right: 2px;margin-top: 40px;">
          <div class="card-header" style="color:white;background-color:rgba(19, 35, 47, 0.9);">
            <h3>""" + x.recruiter + """</h3>
          </div>
          <div class="card-block">
            <h4 class="card-title"><b>Job</b> : """ + x.title + """</h4>
              <p class="card-text"><b>Salary</b> : """ + str(x.salary) + """</p>
              <p class="card-text"><b>Job type</b> : """ + x.job_type + """</p>
            <a href="javascript:void(0);" class="mdl-button" onclick="show(""" + str(x.id) + """)">Details</a>
          </div>
          <div class="card-footer text-muted">
            2 days ago
          </div>
        </div>
            """
    for x in content2:
        there = True
        msg += """
                <div class="card text-xs-center" style="width: 400px;display:inline-block;margin-right: 2px;margin-top: 40px;">
          <div class="card-header" style="color:white;background-color:rgba(19, 35, 47, 0.9);">
            <h3>""" + x.recruiter + """</h3>
          </div>
          <div class="card-block">
            <h4 class="card-title"><b>Job</b> : """ + x.title + """</h4>
              <p class="card-text"><b>Salary</b> : """ + str(x.salary) + """</p>
              <p class="card-text"><b>Job type</b> : """ + x.job_type + """</p>
            <a href="javascript:void(0);" class="mdl-button" onclick="show(""" + str(x.id) + """)">Details</a>
          </div>
          <div class="card-footer text-muted">
            2 days ago
          </div>
        </div>
            """
    if(not there):
        msg+="""<h1>No search items found with '{0}'""".format(search)
    msg+="""</div>"""
    return HttpResponse(msg)

def signuplogin(request):
    t = get_template("signup_login.html")
    _html = t.render({},request)
    return HttpResponse(_html)