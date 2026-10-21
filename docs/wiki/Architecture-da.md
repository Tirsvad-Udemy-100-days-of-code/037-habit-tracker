[English](Architecture) · **Dansk** · [Bahasa Malaysia](Architecture-ms)

# Arkitektur

Koden følger Clean Architecture. Afhængighederne peger indad: `presentation` kender `application` og `domain`; `infrastructure` kender `application` og `domain`; `domain` kender kun `constants`.

```text
src/habit_tracker/
  constants.py
  domain/            value_objects/ (Username, Token, Credentials, GraphId, ...), errors/
  application/       use_cases/ (create_user, create_graph, post_pixel), ports/, dto/, errors/
  infrastructure/    http/ (requests and dry-run gateways), config/ (environment)
  presentation/      cli.py (composition root), commands/, shared/
tests/               unit/, integration/, e2e/
```

| Lag | Indeholder |
| --- | --- |
| `domain` | Værdiobjekter, der håndhæver Pixelas regler (`Username`, `Token`, `GraphId`, `PixelDate`, `Quantity`, ...) og `InvalidInputError` |
| `application` | Use cases `create_user`, `create_graph` og `post_pixel`, porten `PixelaGateway`, `ApiResponse` og API'ets stier |
| `infrastructure` | Adapterne: `RequestsPixelaGateway`, `DryRunPixelaGateway` og læsning af miljøet |
| `presentation` | Kommandolinjen: én kommando pr. use case, og `cli.py`, composition root, der bygger adapterne |

## Beslutninger

- **`requests` er den eneste runtime-afhængighed** (ADR-0001). Den bruges kun i infrastrukturlaget bag porten `PixelaGateway`, så de andre lag testes med en falsk gateway.
- **Ingen use cases eller designdiagrammer** (ADR-0002). Projektet er tre POST-kald; milepælenes Go/No-Go-kriterier og Doxygen-kommentarerne beskriver adfærden.
- **Hemmeligheder holdes ude af koden.** Værdiobjektet `Token` skjuler sin tekst i `str` og `repr`, dry run maskerer den, og token sendes kun i headeren (aldrig i en URL eller i body på et graf- eller pixelkald).
- **Konstanter ligger i `constants.py`**, én gang.

Beslutningerne og planen ligger i `docs/` i repositoriet.
