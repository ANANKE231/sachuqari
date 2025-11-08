from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from .models import Order

@csrf_exempt
def home(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        phone = request.POST.get('phoneNumber')
        video_type = request.POST.get('videoType')
        num_people = request.POST.get('numPeople')
        delivery_method = request.POST.get('deliveryMethod')
        gmail = request.POST.get('gmailAddress')
        people_data = request.POST.get('peopleData')

        saved_paths = []

        for file_key, file in request.FILES.items():
            if file:
                filename = file.name
                upload_path = os.path.join(settings.MEDIA_ROOT, filename)

                # Avoid overwriting files
                base, ext = os.path.splitext(filename)
                counter = 1
                while os.path.exists(upload_path):
                    filename = f"{base}_{counter}{ext}"
                    upload_path = os.path.join(settings.MEDIA_ROOT, filename)
                    counter += 1

                with open(upload_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                saved_paths.append(f"/media/{filename}")

        order = Order.objects.create(
            full_name=full_name,
            phone=phone,
            video_type=video_type,
            num_people=num_people,
            delivery_method=delivery_method,
            gmail=gmail,
            people_data=people_data,
            image_paths=",".join(saved_paths),
        )

        return JsonResponse({
            'status': 'success',
            'message': f'Order saved with {len(saved_paths)} images.',
            'image_paths': saved_paths
        }, status=201)

    return render(request, 'home.html')

# def custom_admin(request):
#     orders = Order.objects.all()
#     return render(request, 'admin.html', {'orders': orders})

