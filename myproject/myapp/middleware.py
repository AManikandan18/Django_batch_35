from django.http import HttpResponse
# from time

class Mymiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Middleware initialized...")
        
    def __call__(self,Request):
        print("Before View(Request Intercepted)")
        response = self.get_response(Request)
        print("Afer View (Response Going to Browser...)")
        return response
    