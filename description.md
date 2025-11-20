# Milestone 3 Project by Bayu Putradana  , FTDS 032 Hacktiv8 Pondok Indah, Jakarta Selatan
# Analisis Data Penerbangan di Bandara JFK New York Menggunakan Airflow, Great Expectations, dan Kibana

---

## Repository Outline  
```
1. README.md – Gambaran umum project Milestone yang dikerjakan
2. description.md – Deskripsi singkat mengenai latar belakang, metode, dan output project  
3. P2M3_Bayu_Putradana_data_raw.csv – Dataset mentah yang diambil dari Kaggle (Flight Take Off Data - JFK Airport)  
4. P2M3_Bayu_Putradana_data_clean.csv – Dataset hasil pembersihan (cleaning) setelah proses normalisasi dan handling missing values  
5. P2M3_Bayu_Putradana_GX.ipynb – Notebook untuk validasi kualitas data menggunakan Great Expectations  
6. P2M3_Bayu_Putradana_DAG.py – Script DAG Apache Airflow untuk otomasi pipeline (fetch, clean, post)  
7. P2M3_Bayu_Putradana_DAG_graph.jpg – Screenshot hasil eksekusi DAG di Airflow  
8. P2M3_Bayu_Putradana_conceptual.txt – Jawaban conceptual problem terkait NoSQL, Airflow, Great Expectations, dll  
9. P2M3_Bayu_Putradana_ddl.txt – Berisi definisi tabel (DDL) untuk pembuatan schema database PostgreSQL  
10. Folder `/images/` – Berisi screenshot hasil visualisasi dan insight pada dashboard Kibana (total 8 visualisasi: 6 plot + 2 markdown berisi identitas & kesimpulan)
```

---

## Problem Background  
Bandara internasional seperti JFK memiliki volume penerbangan yang sangat tinggi setiap harinya. Data penerbangan ini penting untuk dianalisis guna memahami pola keberangkatan, waktu delay, serta tren aktivitas bandara.  
Proyek ini bertujuan untuk melakukan *Exploratory Data Analysis (EDA)* terhadap data penerbangan JFK menggunakan alur kerja yang terstruktur mulai dari pengambilan data, pembersihan, validasi kualitas data, hingga visualisasi hasil analisis.

---

## Project Output  
Output dari proyek ini meliputi:  
- **Pipeline otomatis** menggunakan **Apache Airflow** untuk proses *fetch → cleaning → post* ke Elasticsearch.  
- **Validasi data** menggunakan **Great Expectations** agar data yang digunakan sudah bersih dan sesuai standar kualitas.  
- **Dashboard visualisasi** menggunakan **Kibana**, menampilkan 6 visualisasi data dan 2 markdown insight.  
- **Hasil analisis (insight & kesimpulan)** terkait pola penerbangan dan faktor yang memengaruhi jadwal keberangkatan.

---

## Data  
Dataset yang digunakan berasal dari Kaggle:  
[Flight Take Off Data - JFK Airport](https://www.kaggle.com/datasets/deepankurk/flight-take-off-data-jfk-airport)

**Deskripsi singkat:**  
- Dataset berisi informasi penerbangan yang berangkat dari Bandara JFK di New York, Amerika Serikat.    
- Kolom mencakup: tanggal, waktu keberangkatan, maskapai, tujuan, waktu tunda (delay), status penerbangan, dan lain-lain.  
- Proses data mencakup:
  - Menghapus duplikasi
  - Normalisasi nama kolom (huruf besar kecil, underscore, dll.)
  - Penanganan missing values
- Data dibagi menjadi dua tahap: **data_raw** dan **data_clean**.

---

## Method  
Metode utama dalam proyek ini terdiri dari tiga bagian:
1. **Data Pipeline**  
   Dibangun menggunakan *Apache Airflow* dengan tiga task utama:
   - **Fetch from PostgreSQL**  
     Mengambil data mentah dari database lokal.  
   - **Data Cleaning**  
     Melakukan pembersihan data sesuai kriteria.  
   - **Post to Elasticsearch**  
     Mengunggah data bersih ke Elasticsearch untuk kebutuhan visualisasi di Kibana.  

2. **Data Validation**  
   Menggunakan *Great Expectations* untuk memastikan:
   - Nilai unik pada kolom tertentu
   - Rentang nilai valid
   - Tipe data sesuai harapan
   - Tidak ada nilai kosong
   - Dan beberapa expectation tambahan (total 7 expectations)

3. **Exploratory Data Analysis (EDA)**  
   Dilakukan melalui *Kibana Dashboard* dengan 6 visualisasi berbeda serta narasi insight untuk setiap grafik.

---

## Stacks  
**Bahasa & Tools:**
- **Python** – untuk scripting data pipeline dan cleaning  
- **PostgreSQL** – sebagai sumber data awal (menggunakan PGAdmin)
- **Apache Airflow** – untuk mengatur alur otomatis pipeline  
- **Great Expectations** – untuk validasi dan pengujian kualitas dataset  
- **Elasticsearch & Kibana** – untuk penyimpanan dan visualisasi data  
- **VS Code** – sebagai salah satu aplikasi utama yang digunakan dalam pengerjaan  

**Library Python:**
- `pandas`, `psycopg2`, `datetime`, `great_expectations`, `airflow`, `elasticsearch`

---

## Reference  
- Dataset: [Flight Take Off Data - JFK Airport](https://www.kaggle.com/datasets/deepankurk/flight-take-off-data-jfk-airport)  
- Dokumentasi Airflow: [https://airflow.apache.org/docs/](https://airflow.apache.org/docs/)  
- Dokumentasi Great Expectations: [https://greatexpectations.io/](https://greatexpectations.io/)  
- Dokumentasi Elasticsearch & Kibana: [https://www.elastic.co/](https://www.elastic.co/)  

---

Keterangan:  
Seluruh proses visualisasi dilakukan menggunakan **Kibana Dashboard** berdasarkan data yang telah diproses dan dimasukkan ke **Elasticsearch**.
