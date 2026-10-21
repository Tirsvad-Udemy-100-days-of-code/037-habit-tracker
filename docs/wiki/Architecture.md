**English** · [Dansk](Architecture-da) · [Bahasa Malaysia](Architecture-ms)

# Architecture

The code follows Clean Architecture. Dependencies point inward: `presentation` knows `application` and `domain`; `infrastructure` knows `application` and `domain`; `domain` knows only `constants`.

```text
src/habit_tracker/
  constants.py
  domain/            value_objects/ (Username, Token, Credentials, GraphId, ...), errors/
  application/       use_cases/ (create_user, create_graph, post_pixel), ports/, dto/, errors/
  infrastructure/    http/ (requests and dry-run gateways), config/ (environment)
  presentation/      cli.py (composition root), commands/, shared/
tests/               unit/, integration/, e2e/
```

| Layer | Holds |
| --- | --- |
| `domain` | Value objects that enforce the Pixela rules (`Username`, `Token`, `GraphId`, `PixelDate`, `Quantity`, ...) and `InvalidInputError` |
| `application` | The use cases `create_user`, `create_graph` and `post_pixel`, the `PixelaGateway` port, `ApiResponse` and the paths of the API |
| `infrastructure` | The adapters: `RequestsPixelaGateway`, `DryRunPixelaGateway` and the reading of the environment |
| `presentation` | The command line: one command per use case, and `cli.py`, the composition root that builds the adapters |

## Decisions

- **`requests` is the one runtime dependency** (ADR-0001). It is used only in the infrastructure layer, behind the `PixelaGateway` port, so the other layers are tested with a fake gateway.
- **No use cases or design diagrams** (ADR-0002). The project is three POST requests; the Go/No-Go criteria of the milestones and the Doxygen comments describe the behaviour.
- **Secrets stay out of the code.** The `Token` value object hides its text in `str` and `repr`, the dry run masks it, and the token travels only in the header (never in a URL or in the body of a graph or pixel request).
- **Constants live in `constants.py`**, once.

The decisions and the plan are in `docs/` of the repository.
