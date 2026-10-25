# Security policy

## Reporting a vulnerability

Please do not open a public issue for security problems.

Report them privately through GitHub: go to the **Security** tab of this repo and click **Report a vulnerability** ([direct link](https://github.com/nicedreamzapp/Family-Planner/security/advisories/new)). Only the maintainer sees the report.

Helpful details: what you found, how to reproduce it, which commit, your Python version, and whether the server was behind nginx or reached directly.

I aim to reply within 3 days and to ship a fix or a clear plan within 30 days, depending on severity. You will be credited in the advisory unless you ask not to be.

## Supported versions

Fixes go into the latest code on `main`. Please update before reporting if you are on an older commit.

## What matters most here

The parts where a mistake could hurt someone:

- the HTTP server in `server.py`, which listens on all interfaces on port 8766 by default and holds family data (calendar, chores, meals, notes)
- the password gate in `fp_auth.py`, which only applies to requests that come through nginx with `X-Real-IP`
- the upload endpoints `/api/transcribe` and `/api/ocr` in `server.py`, which take audio and images and forward them to a helper on `localhost:8765`
- the `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` read from the environment or `.env`
