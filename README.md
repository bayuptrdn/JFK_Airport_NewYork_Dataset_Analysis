# Analisis Data Penerbangan Bandara JFK New York  
### Menggunakan Apache Airflow, Great Expectations, dan Kibana

## Gambaran Umum Proyek

Proyek ini berfokus pada **analisis data penerbangan Bandara Internasional John F. Kennedy (JFK), New York**, dengan pendekatan **data pipeline otomatis** dan **validasi kualitas data** sebelum dilakukan eksplorasi dan visualisasi.

Seluruh proses dirancang menyerupai **workflow data engineering & analytics di lingkungan industri**, dimulai dari pengambilan data, pembersihan, validasi, hingga visualisasi interaktif menggunakan Kibana.

---

## Latar Belakang Masalah

Bandara internasional seperti JFK memiliki volume penerbangan yang sangat tinggi setiap hari. Kompleksitas operasional ini menimbulkan berbagai tantangan seperti:
- Keterlambatan penerbangan
- Pola kepadatan jadwal pada jam tertentu
- Variasi performa antar maskapai

Analisis data penerbangan diperlukan untuk memahami **pola operasional bandara**, mengidentifikasi **tren keterlambatan**, serta menyediakan **insight berbasis data** yang dapat digunakan sebagai dasar pengambilan keputusan.

---

## Tujuan Proyek

Tujuan utama dari proyek ini adalah:

- Membangun **pipeline data otomatis** dari database ke sistem analitik
- Memastikan **kualitas data** melalui validasi terstruktur
- Melakukan **Exploratory Data Analysis (EDA)** terhadap data penerbangan JFK
- Menyajikan insight dalam bentuk **dashboard visual interaktif**
- Menghasilkan rekomendasi berbasis data terkait pola penerbangan

---

## Data

### Sumber Dataset
- **Flight Take Off Data – JFK Airport**
- Sumber: Kaggle  
  https://www.kaggle.com/datasets/deepankurk/flight-take-off-data-jfk-airport

### Deskripsi Dataset
- Dataset berisi data penerbangan yang berangkat dari Bandara JFK
- Informasi utama meliputi:
  - Tanggal & waktu keberangkatan
  - Maskapai penerbangan
  - Tujuan
  - Status penerbangan
  - Delay (keterlambatan)
- Dataset diproses melalui dua tahap:
  - **Data mentah (raw)**
  - **Data bersih (clean)** setelah normalisasi dan handling missing values

---

## Metodologi

### 1. Data Pipeline Otomatis
Pipeline dibangun menggunakan **Apache Airflow** dengan tiga proses utama:

1. **Fetch from PostgreSQL**  
   Mengambil data penerbangan dari database PostgreSQL.

2. **Data Cleaning**  
   Proses pembersihan data meliputi:
   - Penghapusan duplikasi
   - Normalisasi nama kolom
   - Penanganan missing values

3. **Post to Elasticsearch**  
   Data bersih dimasukkan ke Elasticsearch untuk kebutuhan analitik dan visualisasi.

---

### 2. Validasi Kualitas Data
Validasi dilakukan menggunakan **Great Expectations** untuk memastikan:
- Keunikan data pada kolom tertentu
- Rentang nilai yang valid
- Tipe data sesuai
- Tidak terdapat nilai kosong
- Konsistensi struktur dataset

Total digunakan **7 expectation berbeda** dengan hasil validasi berhasil.

---

### 3. Exploratory Data Analysis (EDA)
EDA dilakukan menggunakan **Kibana Dashboard**, terdiri dari:
- 6 visualisasi data (beragam jenis chart)
- Insight dan narasi pada setiap visualisasi
- 2 visualisasi markdown berisi:
  - Objective & identitas analisis
  - Kesimpulan dan rekomendasi

---

## Output Proyek

Output utama dari proyek ini meliputi:

- **Pipeline otomatis end-to-end** menggunakan Apache Airflow
- **Dataset tervalidasi** dengan Great Expectations
- **Dashboard Kibana interaktif** berisi visualisasi dan insight
- **Kesimpulan analitis** terkait pola penerbangan dan keterlambatan

---

## Struktur Repository

JFK-Flight-Data-Analysis
|
├── README.md
├── description.md
├── P2M3_Bayu_Putradana_data_raw.csv
├── P2M3_Bayu_Putradana_data_clean.csv
├── P2M3_Bayu_Putradana_GX.ipynb
├── P2M3_Bayu_Putradana_DAG.py
├── P2M3_Bayu_Putradana_DAG_graph.jpg
├── P2M3_Bayu_Putradana_conceptual.txt
├── P2M3_Bayu_Putradana_ddl.txt
└── images/
├── introduction_objective.png
├── plot_insight_01.png
├── plot_insight_02.png
├── plot_insight_03.png
├── plot_insight_04.png
├── plot_insight_05.png
├── plot_insight_06.png
└── kesimpulan.png


---

## Tech Stack

### Tools & Platform
- **Python**
- **PostgreSQL**
- **Apache Airflow**
- **Great Expectations**
- **Elasticsearch**
- **Kibana**
- **Visual Studio Code**

### Library Python
- `pandas`
- `psycopg2`
- `datetime`
- `great_expectations`
- `apache-airflow`
- `elasticsearch`

---

## Kesimpulan

Proyek ini menunjukkan bagaimana **data pipeline terotomasi** yang dikombinasikan dengan **validasi kualitas data** dapat menghasilkan analisis yang lebih andal dan terstruktur.  
Melalui visualisasi Kibana, pola penerbangan dan keterlambatan di Bandara JFK dapat diidentifikasi dengan lebih jelas, sehingga insight yang dihasilkan dapat digunakan sebagai dasar evaluasi operasional maupun perencanaan lanjutan.

---

## Referensi

- Dataset: Flight Take Off Data – JFK Airport (Kaggle)  
- Apache Airflow Documentation: https://airflow.apache.org/docs/  
- Great Expectations Documentation: https://greatexpectations.io/  
- Elasticsearch & Kibana Documentation: https://www.elastic.co/  
