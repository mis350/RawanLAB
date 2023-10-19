from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rawan_view(request):
    x = HttpResponse("Hello Rawan")
    name = "rawan"
    x = HttpResponse(f""" 
    <html> 
         <body> 
             <h1> hi this is your lab work  </h1>         
                <p> welcome to mis 350 course {name}  </p>      

                <p> here is a link to google <a href= "www.google.com">  goolge </p>
         </body>          
    </html> """)




    return x 
