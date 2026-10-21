[English](Usage) · **Dansk** · [Bahasa Malaysia](Usage-ms)

# Brug

Hver kommando læser `PIXELA_USERNAME` og `PIXELA_TOKEN` fra miljøet. Skriv `--dry-run` før kommandonavnet for at se kaldet uden at sende det.

## De tre kommandoer

```bash
python -m habit_tracker create-user --agree-terms --not-minor
python -m habit_tracker create-graph --id cycling --name "Cycling Graph" --unit Km --type float --color ajisai
python -m habit_tracker post-pixel --graph-id cycling --date 2026-10-22 --quantity 9.74
```

| Kommando | Valgmuligheder | Hvad der sendes |
| --- | --- | --- |
| `create-user` | `--agree-terms`, `--not-minor` | POST `users` med token, username, `agreeTermsOfService` og `notMinor` |
| `create-graph` | `--id`, `--name`, `--unit` (påkrævet); `--type` `int` eller `float` (standard `float`); `--color` (standard `ajisai`) | POST `users/<username>/graphs`, token i headeren `X-USER-TOKEN` |
| `post-pixel` | `--graph-id`, `--date`, `--quantity` (påkrævet) | POST `users/<username>/graphs/<graph id>`, token i headeren |

Farverne er Pixelas navne `shibafu` (grøn), `momiji` (rød), `sora` (blå), `ichou` (gul), `ajisai` (lilla) og `kuro` (sort). Datoen er `YYYY-MM-DD` eller `YYYYMMDD`; Pixela modtager altid `YYYYMMDD`. Mængden sendes som tekst.

![Opret graf i dry-run-tilstand](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/raw/branch/main/docs/images/create-graph-dry-run.png)

## Exitkoder

| Kode | Betydning |
| --- | --- |
| 0 | Pixela accepterede kaldet (eller dry run blev gennemført) |
| 1 | Pixela afviste det, fx `Rejected (409)` for et optaget brugernavn |
| 2 | Ugyldigt input eller en manglende miljøvariabel; der blev intet sendt |
| 3 | Pixela kunne ikke nås |

## Fra Python

Opgavens funktioner tager en gateway, loginoplysningerne og trinnets data. Eksemplet udskriver de tre kald i stedet for at sende dem:

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

Brug `RequestsPixelaGateway()` i stedet for `DryRunPixelaGateway(sys.stdout)` for at sende for alvor. En afvisning fra Pixela returneres som et `ApiResponse`, hvor `is_success` er falsk; en server, der ikke kan nås, giver `GatewayError`; en værdi, der bryder en regel, giver `InvalidInputError`, før noget kald sendes.
