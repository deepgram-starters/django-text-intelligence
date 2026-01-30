"""Django Text Intelligence Starter - Views"""
import os, json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from deepgram import DeepgramClient
from dotenv import load_dotenv
import toml

load_dotenv()
API_KEY = os.environ.get("DEEPGRAM_API_KEY")
if not API_KEY:
    raise ValueError("DEEPGRAM_API_KEY required")
deepgram = DeepgramClient(api_key=API_KEY)

@csrf_exempt
@require_http_methods(["POST"])
def analyze(request):
    try:
        body = json.loads(request.body)
        text, url = body.get('text'), body.get('url')
        if not text and not url:
            return JsonResponse({"error": {"type": "validation_error", "code": "INVALID_TEXT", "message": "text or url required", "details": {}}}, status=400)
        request_dict = {"url": url} if url else {"text": text}
        options = {"language": request.GET.get('language', 'en')}
        if request.GET.get('summarize') == 'true': options['summarize'] = True
        if request.GET.get('topics') == 'true': options['topics'] = True
        if request.GET.get('sentiment') == 'true': options['sentiment'] = True
        if request.GET.get('intents') == 'true': options['intents'] = True
        response_data = deepgram.read.v1.text.analyze(request=request_dict, **options)
        result = {"results": response_data.model_dump().get('results', {})} if hasattr(response_data, 'model_dump') else {"results": {}}
        return JsonResponse(result)
    except Exception as e:
        return JsonResponse({"error": {"type": "processing_error", "code": "INVALID_TEXT", "message": str(e), "details": {}}}, status=500)

@require_http_methods(["GET"])
def metadata(request):
    try:
        with open('deepgram.toml', 'r') as f:
            return JsonResponse(toml.load(f).get('meta', {}))
    except:
        return JsonResponse({'error': 'Failed'}, status=500)
