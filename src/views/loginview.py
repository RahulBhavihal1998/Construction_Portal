from django.http import JsonResponse
from rest_framework.views import APIView
from src.libraries import LoginLib

class LoginView(APIView):

    def post(self, requests):
        response_text, success_status = LoginLib().login(login_detail=requests.data)
        Response = {"success": success_status, "message": response_text}
        return JsonResponse(Response)





