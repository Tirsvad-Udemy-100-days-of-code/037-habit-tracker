[English](Architecture) · [Dansk](Architecture-da) · **Bahasa Malaysia**

# Seni bina

Kod mengikut Clean Architecture. Kebergantungan menghala ke dalam: `presentation` mengenali `application` dan `domain`; `infrastructure` mengenali `application` dan `domain`; `domain` hanya mengenali `constants`.

```text
src/habit_tracker/
  constants.py
  domain/            value_objects/ (Username, Token, Credentials, GraphId, ...), errors/
  application/       use_cases/ (create_user, create_graph, post_pixel), ports/, dto/, errors/
  infrastructure/    http/ (requests and dry-run gateways), config/ (environment)
  presentation/      cli.py (composition root), commands/, shared/
tests/               unit/, integration/, e2e/
```

| Lapisan | Mengandungi |
| --- | --- |
| `domain` | Objek nilai yang menguatkuasakan peraturan Pixela (`Username`, `Token`, `GraphId`, `PixelDate`, `Quantity`, ...) dan `InvalidInputError` |
| `application` | Kes guna `create_user`, `create_graph` dan `post_pixel`, port `PixelaGateway`, `ApiResponse` dan laluan API |
| `infrastructure` | Penyesuai: `RequestsPixelaGateway`, `DryRunPixelaGateway` dan pembacaan persekitaran |
| `presentation` | Baris arahan: satu arahan bagi setiap kes guna, dan `cli.py`, composition root yang membina penyesuai |

## Keputusan

- **`requests` ialah satu-satunya kebergantungan runtime** (ADR-0001). Ia hanya digunakan dalam lapisan infrastruktur di sebalik port `PixelaGateway`, jadi lapisan lain diuji dengan gateway palsu.
- **Tiada kes guna atau rajah reka bentuk** (ADR-0002). Projek ini hanya tiga permintaan POST; kriteria Go/No-Go bagi pencapaian dan komen Doxygen menerangkan tingkah lakunya.
- **Rahsia dijauhkan daripada kod.** Objek nilai `Token` menyembunyikan teksnya dalam `str` dan `repr`, dry run menutupnya, dan token hanya dihantar dalam header (tidak pernah dalam URL atau dalam body permintaan graf atau piksel).
- **Pemalar berada dalam `constants.py`**, sekali sahaja.

Keputusan dan pelan berada dalam `docs/` repositori.
