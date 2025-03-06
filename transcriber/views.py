from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
import tempfile
import os

# Add this if you want an index page
from django.shortcuts import render

def index(request):
    return render(request, 'transcriber/index.html')

@csrf_exempt
def speech_to_text(request):
    if request.method == 'POST':
        try:
            print("Received request")
            
            audio_file = request.FILES.get('audio_file')
            if not audio_file:
                print("No audio file received")
                return JsonResponse({'error': 'No audio file provided'}, status=400)

            print(f"Received audio file: {audio_file.name}, size: {audio_file.size}")

            # Create a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                for chunk in audio_file.chunks():
                    tmp_file.write(chunk)
                tmp_file_path = tmp_file.name

            try:
                recognizer = sr.Recognizer()
                with sr.AudioFile(tmp_file_path) as source:
                    audio = recognizer.record(source)
                
                try:
                    text = recognizer.recognize_google(audio)
                    print(f"Transcribed text: {text}")
                    
                    return JsonResponse({
                        'status': 'success',
                        'text': text
                    })
                except sr.UnknownValueError:
                    print("Could not understand audio")
                    return JsonResponse({
                        'status': 'error',
                        'error': 'Could not understand audio'
                    }, status=400)
                except sr.RequestError as e:
                    print(f"Google API error: {str(e)}")
                    return JsonResponse({
                        'status': 'error',
                        'error': f'API error: {str(e)}'
                    }, status=500)
                
            finally:
                # Clean up the temporary file
                if os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)
                    
        except Exception as e:
            print(f"Server error: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'error': str(e)
            }, status=500)

    return JsonResponse({
        'status': 'error',
        'error': 'Method not allowed'
    }, status=405)
