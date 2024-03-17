from django.shortcuts import render, HttpResponse
from translate import Translator

def home(request):
    if request.method == "POST":
        try:
            text = request.POST["translate"]
            language = request.POST["language"]
            if text and language:
                translator = Translator(to_lang=language)
                translation = translator.translate(text)
                return HttpResponse(translation)
            else:
                return HttpResponse("Text and language must be provided")
        except Exception as e:
            return HttpResponse(f"Translation failed: {e}")
    else:
        return render(request, "tapp/index.html")
