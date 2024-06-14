# Django Data Analysis Project

## Overview

This Django-based web application allows users to upload CSV files, perform data analysis using pandas and numpy, and display the results and visualizations on the web interface.

## Features

1. **File Upload**: Users can upload CSV files.
2. **Data Processing**: Uses pandas to read and analyze the uploaded CSV file.
   - Displays the first few rows of the data.
   - Calculates summary statistics (mean, median, standard deviation) for numerical columns.
   - Identifies and handles missing values.
3. **Data Visualization**: Generates basic plots using matplotlib or seaborn.
   - Histograms for numerical columns.
4. **User Interface**: Simple and user-friendly interface using Django templates.
   - Displays the data analysis results and visualizations in a clear and organized manner.

## Project Structure
```bash
  data_analysis_project/
│
├── analysis/
│ ├── migrations/
│ ├── templates/
│ │ └── analysis/
│ │ ├── upload.html
│ │ └── results.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
│
├── data_analysis_project/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── media/
│
├── manage.py
└── requirements.txt
```
