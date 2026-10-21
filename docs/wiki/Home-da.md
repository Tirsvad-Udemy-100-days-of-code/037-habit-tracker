[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Habit Tracker

Et lille Python-projekt, der sporer en vane med HTTP-API'et fra [Pixela](https://docs.pixe.la/). Det er Pixela-opgaven fra Udemy-kurset "100 Days of Code: The Complete Python Pro Bootcamp", skrevet til kursister, der vil have læsbar kode, som kan køres, og til besøgende, der søger inspiration.

Projektet følger de tre trin fra forelæsningerne, hvert et POST-kald til Pixela:

1. **Opret en bruger** med `create_user` (token og brugernavn i body).
2. **Opret en graf** med `create_graph` (token sendes i headeren `X-USER-TOKEN`).
3. **Send et pixel** med `post_pixel` (en dato som `YYYYMMDD` og en mængde som tekst, fx `"9.74"`).

![Send pixel i dry-run-tilstand](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/raw/branch/main/docs/images/post-pixel-dry-run.png)

## Sider

- [Kom i gang](Getting-Started-da): krav, `.venv` og miljøvariabler.
- [Brug](Usage-da): de tre kommandoer, exitkoderne og Python-funktionerne.
- [Arkitektur](Architecture-da): lagene og beslutningerne bag dem.
- [Udvikling](Development-da): test, kvalitetstjek, Doxygen og workflows.

## Godt at vide

- Dit brugernavn og din token står aldrig i kildekoden. De læses fra miljøet, og projektet læser ikke en `.env`-fil.
- `--dry-run` udskriver kaldet med skjult token og sender ingenting.
- Den eneste runtime-afhængighed er `requests`, fordi opgaven handler om det modul.
- Repositoriet ligger på https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker.
