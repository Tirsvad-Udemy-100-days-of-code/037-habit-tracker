[English](Usage) · [Dansk](Usage-da) · **Bahasa Malaysia**

# Penggunaan

Setiap arahan membaca `PIXELA_USERNAME` dan `PIXELA_TOKEN` daripada persekitaran. Letakkan `--dry-run` sebelum nama arahan untuk melihat permintaan tanpa menghantarnya.

## Tiga arahan

```bash
python -m habit_tracker create-user --agree-terms --not-minor
python -m habit_tracker create-graph --id cycling --name "Cycling Graph" --unit Km --type float --color ajisai
python -m habit_tracker post-pixel --graph-id cycling --date 2026-10-22 --quantity 9.74
```

| Arahan | Pilihan | Apa yang dihantar |
| --- | --- | --- |
| `create-user` | `--agree-terms`, `--not-minor` | POST `users` dengan token, username, `agreeTermsOfService` dan `notMinor` |
| `create-graph` | `--id`, `--name`, `--unit` (wajib); `--type` `int` atau `float` (lalai `float`); `--color` (lalai `ajisai`) | POST `users/<username>/graphs`, token dalam header `X-USER-TOKEN` |
| `post-pixel` | `--graph-id`, `--date`, `--quantity` (wajib) | POST `users/<username>/graphs/<graph id>`, token dalam header |

Warna ialah nama Pixela `shibafu` (hijau), `momiji` (merah), `sora` (biru), `ichou` (kuning), `ajisai` (ungu) dan `kuro` (hitam). Tarikh ialah `YYYY-MM-DD` atau `YYYYMMDD`; Pixela sentiasa menerima `YYYYMMDD`. Kuantiti dihantar sebagai teks.

![Cipta graf dalam mod dry-run](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/raw/branch/main/docs/images/create-graph-dry-run.png)

## Kod keluar

| Kod | Maksud |
| --- | --- |
| 0 | Pixela menerima permintaan (atau dry run selesai) |
| 1 | Pixela menolaknya, contohnya `Rejected (409)` untuk nama pengguna yang sudah digunakan |
| 2 | Input tidak sah atau pemboleh ubah persekitaran tiada; tiada apa-apa dihantar |
| 3 | Pixela tidak dapat dihubungi |

## Daripada Python

Fungsi tugasan mengambil gateway, kelayakan dan data langkah itu. Contoh ini mencetak tiga permintaan dan tidak menghantarnya:

```python
import sys
from datetime import date

from habit_tracker import create_graph, create_user, post_pixel
from habit_tracker.domain.value_objects.credentials import Credentials
from habit_tracker.domain.value_objects.graph import Graph
from habit_tracker.domain.value_objects.graph_color import GraphColor
from habit_tracker.domain.value_objects.graph_id import GraphId
from habit_tracker.domain.value_objects.graph_type import GraphType
from habit_tracker.domain.value_objects.pixel import Pixel
from habit_tracker.domain.value_objects.pixel_date import PixelDate
from habit_tracker.domain.value_objects.quantity import Quantity
from habit_tracker.infrastructure.http.dry_run_pixela_gateway import DryRunPixelaGateway

gateway = DryRunPixelaGateway(sys.stdout)  # RequestsPixelaGateway() sends for real
credentials = Credentials.of("your-username", "your-secret-token")
graph = Graph(GraphId("cycling"), "Cycling Graph", "Km", GraphType.FLOAT, GraphColor.AJISAI)
pixel = Pixel(PixelDate(date(2026, 10, 22)), Quantity("9.74"))

create_user(gateway, credentials)
create_graph(gateway, credentials, graph)
post_pixel(gateway, credentials, GraphId("cycling"), pixel)
```

Gunakan `RequestsPixelaGateway()` sebagai ganti `DryRunPixelaGateway(sys.stdout)` untuk menghantar sebenarnya. Penolakan oleh Pixela dikembalikan sebagai `ApiResponse` dengan `is_success` palsu; pelayan yang tidak dapat dihubungi menimbulkan `GatewayError`; nilai yang melanggar peraturan menimbulkan `InvalidInputError` sebelum sebarang permintaan dihantar.
