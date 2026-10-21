[English](Home) · [Dansk](Home-da) · **Bahasa Malaysia**

# Habit Tracker

Projek Python kecil yang menjejak tabiat dengan API HTTP [Pixela](https://docs.pixe.la/). Ia ialah tugasan Pixela daripada kursus Udemy "100 Days of Code: The Complete Python Pro Bootcamp", ditulis untuk peserta kursus yang mahukan kod yang mudah dibaca dan boleh dijalankan, dan untuk pelawat yang mencari idea.

Projek ini mengikut tiga langkah dalam kuliah, masing-masing satu permintaan POST kepada Pixela:

1. **Cipta pengguna** dengan `create_user` (token dan nama pengguna dalam body).
2. **Cipta graf** dengan `create_graph` (token dihantar dalam header `X-USER-TOKEN`).
3. **Hantar piksel** dengan `post_pixel` (tarikh `YYYYMMDD` dan kuantiti sebagai teks, contohnya `"9.74"`).

![Hantar piksel dalam mod dry-run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/raw/branch/main/docs/images/post-pixel-dry-run.png)

## Halaman

- [Mula di sini](Getting-Started-ms): keperluan, `.venv` dan pemboleh ubah persekitaran.
- [Penggunaan](Usage-ms): tiga arahan, kod keluar dan fungsi Python.
- [Seni bina](Architecture-ms): lapisan dan keputusan di sebaliknya.
- [Pembangunan](Development-ms): ujian, semakan kualiti, Doxygen dan workflow.

## Perlu diketahui

- Nama pengguna dan token anda tidak pernah ada dalam kod sumber. Ia dibaca daripada persekitaran, dan projek ini tidak membaca fail `.env`.
- `--dry-run` mencetak permintaan dengan token disembunyikan dan tidak menghantar apa-apa.
- Satu-satunya kebergantungan runtime ialah `requests`, kerana tugasan ini mengajar modul tersebut.
- Repositori berada di https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker.
