# Submission Dicoding "Belajar Analisis Data dengan Python"

## Struktur Direktori

- **/data**: Direktori ini berisi data yang digunakan dalam proyek, dalam format .csv yaitu day.csv dan hour.csv
- **/dashboard**: Direktori ini berisi dashboard.py yang digunakan untuk membuat dashboard hasil analisis data dan juga berisi data yang sudah clean.
- **notebook.ipynb**: File ini yang digunakan untuk melakukan analisis data.


## Extract Zip
## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```