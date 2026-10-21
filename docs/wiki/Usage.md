**English** · [Dansk](Usage-da) · [Bahasa Malaysia](Usage-ms)

# Usage

Every command reads `PIXELA_USERNAME` and `PIXELA_TOKEN` from the environment. Put `--dry-run` before the command name to see the request without sending it.

## The three commands

```bash
python -m habit_tracker create-user --agree-terms --not-minor
python -m habit_tracker create-graph --id cycling --name "Cycling Graph" --unit Km --type float --color ajisai
python -m habit_tracker post-pixel --graph-id cycling --date 2026-10-22 --quantity 9.74
```

| Command | Options | What it sends |
| --- | --- | --- |
| `create-user` | `--agree-terms`, `--not-minor` | POST `users` with token, username, `agreeTermsOfService` and `notMinor` |
| `create-graph` | `--id`, `--name`, `--unit` (required); `--type` `int` or `float` (default `float`); `--color` (default `ajisai`) | POST `users/<username>/graphs`, token in the `X-USER-TOKEN` header |
| `post-pixel` | `--graph-id`, `--date`, `--quantity` (required) | POST `users/<username>/graphs/<graph id>`, token in the header |

The colours are the Pixela names `shibafu` (green), `momiji` (red), `sora` (blue), `ichou` (yellow), `ajisai` (purple) and `kuro` (black). The date is `YYYY-MM-DD` or `YYYYMMDD`; Pixela always receives `YYYYMMDD`. The quantity is sent as a string.

![Create graph in dry-run mode](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/raw/branch/main/docs/images/create-graph-dry-run.png)

## Exit codes

| Code | Meaning |
| --- | --- |
| 0 | Pixela accepted the request (or the dry run finished) |
| 1 | Pixela refused it, for example `Rejected (409)` for a taken username |
| 2 | Invalid input or a missing environment variable; nothing was sent |
| 3 | Pixela could not be reached |

## From Python

The functions of the assignment take a gateway, the credentials and the data. This example prints the three requests instead of sending them:

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

Use `RequestsPixelaGateway()` instead of `DryRunPixelaGateway(sys.stdout)` to send for real. A refusal by Pixela is returned as an `ApiResponse` whose `is_success` is false; an unreachable server raises `GatewayError`; a value that breaks a rule raises `InvalidInputError` before any request.
