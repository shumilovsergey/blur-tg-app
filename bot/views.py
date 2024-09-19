from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import telegram_format


@api_view(['POST'])
def getMessage(request):
    message = telegram_format(request.data)
    print(message)
    if message.chat_id == "507717647" and message.audio:
        text = message.title + "    //_//   " + message.audio
        message.sendMessage(text=text)

    if message.text != "/start":
        message.deleteMessage()
    return Response("ok", status=200)





