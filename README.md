## run query CREATE table untuk menampung data API guruFocus

```bash
USE keloola_db;

CREATE TABLE IF NOT EXISTS level_pengguna (
    id_level INT NOT NULL AUTO_INCREMENT,
    nama_level VARCHAR(255) NOT NULL,
    PRIMARY KEY (id_level)
);

CREATE TABLE IF NOT EXISTS data_industri_company (
    id_industri INT NOT NULL AUTO_INCREMENT,
    jenis_industri VARCHAR(50) NOT NULL,
    PRIMARY KEY (id_industri)
);

CREATE TABLE IF NOT EXISTS future_growth_forecasts_competitor (
    id_analyst_future_growth_forecast INT NOT NULL AUTO_INCREMENT,
    AVG_industri_earning_growth_rate FLOAT DEFAULT 0,
    AVG_industri_revenue_growth_rate FLOAT DEFAULT 0,
    AVG_market_earning_growth_rate FLOAT DEFAULT 0,
    AVG_market_revenue_growth_rate FLOAT DEFAULT 0,
    jenis_industri_competitor VARCHAR(50),
    create_at TIMESTAMP,
    PRIMARY KEY (id_analyst_future_growth_forecast)
);

CREATE TABLE IF NOT EXISTS data_company (
    id_company INT NOT NULL AUTO_INCREMENT,
    id_user INT NOT NULL,
    id_industri INT NOT NULL,
    nama_perusahaan VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_company),
    FOREIGN KEY (id_industri)
        REFERENCES data_industri_company (id_industri)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS data_pengguna (
    id_user INT NOT NULL AUTO_INCREMENT,
    id_level INT NOT NULL,
    id_company INT NOT NULL,
    nama_akun VARCHAR(15) NOT NULL,
    kata_sandi VARCHAR(50) NOT NULL,
    nama_pengguna VARCHAR(30) NOT NULL,
    alamat VARCHAR(200) NOT NULL,
    no_ktp VARCHAR(15) NOT NULL,
    no_hp VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    PRIMARY KEY (id_user),
    FOREIGN KEY (id_level)
        REFERENCES level_pengguna (id_level)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY (id_company)
        REFERENCES data_company (id_company)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS ratio_competitor (
    id_ratio INT NOT NULL AUTO_INCREMENT,
    id_user INT NOT NULL,
    nama_kompetitor INT,
    PE_ratio FLOAT DEFAULT 0.0,
    PS_ratio FLOAT DEFAULT 0.0,
    PB_ratio FLOAT DEFAULT 0.0,
    AVG_industri_ROE_3Y FLOAT DEFAULT 0.0,
    ROA FLOAT DEFAULT 0.0,
    ROCE FLOAT DEFAULT 0.0,
    jenis_industri_competitor VARCHAR(50),
    created_at TIMESTAMP,
    PRIMARY KEY (id_ratio),
    FOREIGN KEY(id_user)
        REFERENCES data_pengguna (id_user)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS past_earnings_growth_analysis (
    id_past_earning INT NOT NULL AUTO_INCREMENT,
    id_user INT NOT NULL,
    AVG_industri_5Y_EBITDA FLOAT DEFAULT 0,
    AVG_industri_1Y_EBITDA FLOAT DEFAULT 0,
    jenis_industri_competitor VARCHAR(50),
    create_at TIMESTAMP,
    PRIMARY KEY (id_past_earning),
    FOREIGN KEY (id_user)
        REFERENCES data_pengguna (id_user)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);


------------ belum masukin data ke masing-masing tabel di atas --------------------------


INSERT INTO level_pengguna
( 
 nama_level
)
VALUES
("karyawan"),
("pemilik perusahaan");


INSERT INTO data_industri_company
( 
 jenis_industri
)
VALUES
("Construction"),
("Farm & Heavy Construction Machinery");


INSERT INTO data_company
( 
 id_user, id_industri, nama_perusahaan
)
VALUES
(1, 2, "PT. Indotara Persada"),
(1, 1, "PT. HASTRA KARYA PERSADA");


INSERT INTO data_pengguna
( 
 id_level, id_company, nama_akun, kata_sandi, nama_pengguna, alamat, no_ktp, no_hp, email
)
VALUES
(1,1,"ridwan", "12345678", "ridwan45", "malaka jaya", "312221212121", "081212121212", "ridwan@gmail.com"),
(2,2,"saep", "1112223", "saep", "malaka sari", "321425121", "0812132432", "aep@gmail.com");


-- ----------------------- cek perusahaan user berjenis industri apa -----------------
-- SELECT 
--     dp.nama_akun AS nama_pengguna,
--     dc.nama_perusahaan AS user_company,
--     dic.jenis_industri AS jenis_industri
-- FROM data_company dc 
-- INNER JOIN data_pengguna dp ON dc.id_company = dp.id_company
-- INNER JOIN data_industri_company dic ON dc.id_industri = dic.id_industri

```


setelah itu lakukan langkah di bawah ini:

link tutorial untuk mempermudah deploy:

```bash
https://www.youtube.com/watch?v=Q4-k2E9Wb3w&t=3369s
```

Berikut adalah contoh README.md yang menjelaskan cara melakukan deploy aplikasi Python ke Heroku berdasarkan informasi yang diberikan dalam gambar:

```markdown
# Deploy Aplikasi Python ke Heroku

Panduan ini menjelaskan langkah-langkah untuk melakukan deploy aplikasi Python ke Heroku.

## Langkah 1: Buat Environment di Folder Aplikasi

Buat environment Python di folder aplikasi Anda. Gunakan perintah berikut:
```

```bash
conda create --name <namanya> python=3.?
```

Gantilah `<namanya>` dengan nama environment yang Anda inginkan dan saya menggunakan `python 3.8` dengan versi Python yang sesuai.

## Langkah 2: Aktifkan Environment

Setelah environment berhasil dibuat, aktifkan environment tersebut dengan perintah berikut:

```bash
conda activate <namanya>
```

Gantilah `<namanya>` dengan nama environment yang telah Anda buat.

## Langkah 3: Install Perangkat yang Dibutuhkan

Install semua dependencies atau perangkat yang diperlukan menggunakan perintah berikut:

```bash
pip install -r requirements.txt
```

Gantilah `<namafiledaftarperangkat>` dengan nama file yang berisi daftar dependencies (biasanya `requirements.txt`).

## Langkah 4: Test Aplikasi di Lokal

Sebelum melakukan deploy, pastikan aplikasi berjalan dengan baik di lokal. Jalankan aplikasi Anda dengan perintah berikut:

```bash
python app.py
```

## Langkah 5: Masuk ke Heroku dan Buat Aplikasi Baru

Masuk ke akun Heroku Anda, kemudian buat aplikasi baru melalui menu:

```plaintext
Create -> New App
```

## Langkah 6: Login ke CLI Heroku

Gunakan Heroku CLI untuk login ke akun Heroku Anda dengan perintah berikut:

```bash
heroku login -i
```

## Langkah 7: Proses Mengupload Aplikasi ke Server Heroku Lewat Git

Setelah login, ikuti langkah-langkah berikut untuk mengupload aplikasi Anda ke Heroku:

1. Inisialisasi Git di folder proyek Anda (jika belum dilakukan):

   ```bash
   git init heroku
   ```

2. Tambahkan remote Heroku ke Git:

   ```bash
   git remote add heroku <namaaplikasidiHeroku>
   ```

   Gantilah `<namaaplikasidiHeroku>` dengan nama aplikasi yang telah Anda buat di Heroku.

3. Tambahkan semua file ke Git:

   ```bash
   git add .
   ```

4. Commit perubahan:

   ```bash
   git commit -am "Deploy aplikasi python"
   ```

5. Push ke Heroku:

   ```bash
   git push heroku master
   ```

## Catatan Tambahan

- Pastikan file `Procfile` ada di root folder proyek Anda dengan format yang benar untuk menjalankan aplikasi di Heroku.
- Jika menggunakan database, pastikan konfigurasi environment variables (seperti `DATABASE_URL`) sudah diatur dengan benar di Heroku.

Setelah semua langkah di atas selesai, aplikasi Anda seharusnya sudah berhasil dideploy ke Heroku dan bisa diakses melalui URL aplikasi yang disediakan oleh Heroku.
```

Anda dapat menyesuaikan README.md ini sesuai dengan kebutuhan spesifik proyek Anda. Pastikan juga untuk menyertakan informasi tambahan jika ada pengaturan atau konfigurasi khusus yang diperlukan.



(stag-app-thrive) D:\Hari Ini\Semester 8\Tugas\Thrive\fix-app-finance-dashboard\backup\updateMasFrendi\OOP_flask>tree
Folder PATH listing for volume DATA
Volume serial number is FEE0-2270
D:.
├───app
│   ├───logs
│   ├───models
│   │   └───__pycache__
│   ├───resources
│   │   ├───css
│   │   ├───cssbundle
│   │   │   └───font
│   │   ├───fourth
│   │   │   └───vendor
│   │   │       └───fancybox
│   │   │           └───source
│   │   ├───js
│   │   │   └───bundle
│   │   ├───main
│   │   │   └───css
│   │   ├───second
│   │   │   └───cssbundle
│   │   │       └───font
│   │   ├───thridJS
│   │   │   └───js
│   │   │       └───bundle
│   │   └───vendor
│   │       └───fancybox
│   │           └───source
│   ├───routes
│   │   └───__pycache__
│   ├───services
│   │   └───__pycache__
│   ├───templates
│   └───__pycache__
└───logs

