import os
import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
import matplotlib.pyplot as plt
import seaborn as sns

def handle_uploaded_file(file):
    file_path = os.path.join('media', file.name)
    with open(file_path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return file_path

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = handle_uploaded_file(request.FILES['file'])
            data = pd.read_csv(file_path)

            # Perform data analysis here
            summary_stats = data.describe().to_html()
            first_rows = data.head().to_html()
            missing_values = data.isnull().sum().to_html()

            # Generate visualizations
            sns.set(style="darkgrid")
            fig, ax = plt.subplots()
            data.hist(ax=ax)
            fig.savefig('media/histogram.png')
            
            return render(request, 'analysis/results.html', {
                'summary_stats': summary_stats,
                'first_rows': first_rows,
                'missing_values': missing_values,
                'histogram': 'media/histogram.png',
            })
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})