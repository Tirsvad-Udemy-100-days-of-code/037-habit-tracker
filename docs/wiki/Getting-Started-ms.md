[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Mula di sini

## Keperluan

- Python 3.13 atau lebih baharu.
- `requests` (dipasang bersama projek).
- Pilihan: [Doxygen](https://www.doxygen.nl/) untuk membina dokumentasi kod sumber.

## Cipta dan guna .venv setempat

Klon repositori, cipta persekitaran maya di akarnya, naik taraf `pip` dan pasang projek bersama alat pembangunan.

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Keluar daripada persekitaran dengan `deactivate`. Folder `.venv` diabaikan oleh git.

## Pilih nama pengguna dan token

Pilih nama pengguna Pixela anda sendiri (huruf kecil dahulu, kemudian 2 hingga 33 huruf kecil, digit atau sengkang) dan token rahsia (8 hingga 128 aksara boleh cetak tanpa ruang). Pixela tidak menjana token; anda memilihnya sendiri. Tetapkan kedua-duanya dalam shell anda:

```bash
export PIXELA_USERNAME="your-username"
export PIXELA_TOKEN="your-secret-token"
```

PowerShell:

```powershell
$env:PIXELA_USERNAME = "your-username"
$env:PIXELA_TOKEN = "your-secret-token"
```

## Larian pertama

Cuba dry run dahulu. Ia tidak menghantar apa-apa:

```bash
python -m habit_tracker --dry-run create-user --agree-terms --not-minor
```

Jika output menunjukkan `POST https://pixe.la/v1/users` dan token yang disembunyikan (`********`), semuanya sudah sedia. Teruskan dengan [Penggunaan](Usage-ms).

![Cipta pengguna dalam mod dry-run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/raw/branch/main/docs/images/create-user-dry-run.png)
