# Sing Out

A simple karaoke queue manager for Scrimba Module 3: Python Functions and Error Handling.

## Run

Download and unzip the project. Open Terminal in that folder and type:

```bash
python3 sing_out.py
```

Python 3 is required. No extra packages are needed. The app starts with two example singers.

## Commands

- `add`: enter a name and song to add a singer to the end.
- `next`: announce and remove the first singer.
- `top`: enter a singer's displayed number to move them to the front.
- `remove`: enter a name to remove the first matching singer.
- `quit`: close the app.

The numbered queue appears after each command. Blank names or songs, invalid numbers, unknown commands, and empty queues show a message instead of crashing. Names and songs are trimmed and title-cased. If two singers have the same name, `remove` removes the first match.

The queue lasts only while the app is running. Restarting restores the two example singers.

The code uses functions, parameters, return values, lists of tuples, loops, guard clauses, and `try`/`except ValueError`.
