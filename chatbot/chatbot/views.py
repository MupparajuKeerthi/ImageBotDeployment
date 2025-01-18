from django.shortcuts import render

def process(request):
    if request.method == 'POST' and 'uploaded_image' in request.FILES:
        uploaded_image = request.FILES['uploaded_image']
        # Save the image temporarily or process it here
        return render(request, 'process.html', {'uploaded_image_url': uploaded_image.name})
    return render(request, 'home.html')

def image_enhancement(request):
    return render(request, 'image_enhancement.html')

def image_captioning(request):
    return render(request, 'image_captioning.html')

def similar_images(request):
    return render(request, 'similar_images.html')

def visual_qa(request):
    return render(request, 'visual_qa.html')
