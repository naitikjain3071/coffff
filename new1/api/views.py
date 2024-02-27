from django.shortcuts import render

# Create your views here.
# # api/views.py

from django.http import JsonResponse
from rest_framework.decorators import api_view
from PIL import Image
import numpy as np
import os
# from .utils import run_analysis

import numpy as np
import cv2
def run_analysis(image: np.ndarray):
    lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)

    # Calculate the average of L*, a*, and b* channels
    L_score = np.mean(lab_image[:, :, 0])  * (100.0 / 255.0)
    a_score = np.mean(lab_image[:, :, 1]) - 128
    b_score = np.mean(lab_image[:, :, 2]) - 128
    lab_image_list = lab_image.tolist()
    return {
        "error_message": "",
        "result": [
            {"L_score": L_score, "a_score": a_score, "b_score": b_score},
            {"L_score": L_score, "a_score": a_score, "b_score": b_score},
        ]
    }


@api_view(['POST'])
def analysis(request):
    if request.method != 'POST':
        return JsonResponse({'error_message': 'Invalid request method', 'result': []})

    image_file = request.FILES.get('image')
    if not image_file:
        return JsonResponse({'error_message': 'No image provided', 'result': []})

    try:
        image = Image.open(image_file)
        image_np = np.array(image)
        analysis_result = run_analysis(image_np)

        save_path = 'path/to/save/images'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        with open(os.path.join(save_path, image_file.name), 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        return JsonResponse(analysis_result)

    except Exception as e:
        return JsonResponse({'error_message': str(e), 'result': []})