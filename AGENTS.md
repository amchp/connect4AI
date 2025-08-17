# Repository Guidelines

## Project Structure & Module Organization
- `main.py`: Game entrypoint (starts Pygame loop and screen controller).
- `connect4.py`: Core game rules and board state (no UI).
- `screens/`: UI screens (`game_screen.py`, `menu.py`, `victory_screen.py`).
- `colors.py`, `choices.py`: Shared UI constants and enums.
- `Connect_4_AI.ipynb`: Notebook for experiments; not required to run the game.
- `requirements.txt`: Python dependencies (Pygame).

## Build, Test, and Development Commands
- Create venv: `python3 -m venv .venv && source .venv/bin/activate` (Windows: `.venv\Scripts\activate`).
- Install deps: `pip install -r requirements.txt`.
- Run locally: `python main.py` (opens a 420x361 window).
- Lint/format (optional, if installed): `ruff .` and `black .`.

## Coding Style & Naming Conventions
- Python 3 with type hints where practical.
- Indentation: 4 spaces; line length 88–100 chars.
- Names: `snake_case` for functions/vars/modules, `CapWords` for classes, UPPER_SNAKE for constants.
- Screens live in `screens/` and expose `controls()` and `draw()` methods.

## Testing Guidelines
- No formal test suite yet. Add unit tests under `tests/` using `pytest`.
- Name tests `test_*.py` and focus on pure logic in `connect4.py` (e.g., `Connect4.move`, `connect_4`).
- Example: `pytest -q` (after `pip install pytest`).

## Commit & Pull Request Guidelines
- Messages: Use imperative present tense; prefer Conventional Commits (e.g., `feat: add drop logic`, `fix: prevent out-of-bounds move`).
- Scope small, focused commits; reference issues (`Closes #12`).
- PRs: include summary, motivation, before/after notes or screenshots (if UI), and test notes. Ensure `python main.py` runs without errors.

## Security & Configuration Tips
- Pygame requires an active display; run locally (not headless CI) or use SDL virtual display if needed.
- Avoid committing local virtualenvs (`.venv/`) or large assets; `.gitignore` already covers common cases.
- For new dependencies, pin versions in `requirements.txt` and verify window opens on macOS/Linux/Windows.

