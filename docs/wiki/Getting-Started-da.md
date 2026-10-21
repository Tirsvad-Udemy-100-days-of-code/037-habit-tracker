[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

## Krav

- Python 3.13 eller nyere.
- `requests` (installeres sammen med projektet).
- Valgfrit: [Doxygen](https://www.doxygen.nl/) til at bygge kildedokumentationen.

## Opret og brug et lokalt .venv

Klon repositoriet, opret det virtuelle miljø i roden, opgradér `pip` og installér projektet med udviklingsværktøjerne.

Linux og macOS:

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

Forlad miljøet med `deactivate`. Mappen `.venv` ignoreres af git.

## Vælg brugernavn og token

Vælg dit eget Pixela-brugernavn (først et lille bogstav, derefter 2 til 33 små bogstaver, cifre eller bindestreger) og en hemmelig token (8 til 128 tegn, der kan udskrives, uden mellemrum). Pixela laver ikke token for dig; du vælger den selv. Sæt begge i din shell:

```bash
export PIXELA_USERNAME="your-username"
export PIXELA_TOKEN="your-secret-token"
```

PowerShell:

```powershell
$env:PIXELA_USERNAME = "your-username"
$env:PIXELA_TOKEN = "your-secret-token"
```

## Første kørsel

Prøv først dry run. Den sender ingenting:

```bash
python -m habit_tracker --dry-run create-user --agree-terms --not-minor
```

Hvis udskriften viser `POST https://pixe.la/v1/users` og en skjult token (`********`), er alt klar. Fortsæt med [Brug](Usage-da).

![Opret bruger i dry-run-tilstand](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/raw/branch/main/docs/images/create-user-dry-run.png)
