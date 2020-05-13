from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, "count.html")

def result(request):
    text = request.POST['text']
    total_len = len(text)
    len_without_blank = len(text.replace(" ",""))
    word = len(text.split(" "))

    return render(request, "result.html", {
        'text' : text,
        'total_len' : total_len,
        'len_without_blank' : len_without_blank,
        'word' : word,
    })