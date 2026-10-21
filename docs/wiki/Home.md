**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Habit Tracker

A small Python project that tracks a habit with the [Pixela](https://docs.pixe.la/) HTTP API. It is the Pixela assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", written for course participants who want readable, runnable code and for visitors who want an idea.

The project follows the three lecture steps, each a POST request to Pixela:

1. **Create a user** with `create_user` (token and username in the body).
2. **Create a graph** with `create_graph` (the token travels in the `X-USER-TOKEN` header).
3. **Post a pixel** with `post_pixel` (a `YYYYMMDD` date and a quantity string such as `"9.74"`).

![Post pixel in dry-run mode](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker/raw/branch/main/docs/images/post-pixel-dry-run.png)

## Pages

- [Getting started](Getting-Started): requirements, the `.venv`, the environment variables.
- [Usage](Usage): the three commands, the exit codes and the Python functions.
- [Architecture](Architecture): the layers and the decisions behind them.
- [Development](Development): tests, quality checks, Doxygen and the workflows.

## Good to know

- Your username and token are never in the source. They are read from the environment, and the project does not read a `.env` file.
- `--dry-run` prints the request with the token hidden and sends nothing.
- The only runtime dependency is `requests`, because the assignment teaches it.
- The repository is at https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/037-habit-tracker.
