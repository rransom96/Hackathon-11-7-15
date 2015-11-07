from django.shortcuts import render, render_to_response
from django.views.generic import View


class WelcomePage(View):

    def get(self, request):
        #return render_to_response('hackathon_app/homepage.html')
        return render(self.request, 'hackathon_app/homepage.html')





