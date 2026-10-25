# Contributing

Thanks for taking a look. This planner runs on a spare iPad in my kitchen, so reports from other
devices and other families' setups help a lot.

## Reporting a problem

Open an [issue](https://github.com/nicedreamzapp/Family-Planner/issues/new/choose). The things that
make it quick to fix:

- the device and browser you view it on (for example an iPad running it as a home screen app)
- your Python version and the OS the server runs on
- which part it is about (calendar, chores, meals, shopping, voice, OCR, Fia chat, screensaver)
- what the server printed, and any errors from the browser console

Please leave out real names, events and other family data from screenshots and logs.

## Running it locally

```bash
git clone https://github.com/nicedreamzapp/Family-Planner.git
cd Family-Planner
python3 -m venv .venv
source .venv/bin/activate
pip install anthropic openai  # For AI features

export OPENAI_API_KEY="your-key"      # For Whisper voice transcription
export ANTHROPIC_API_KEY="your-key"   # For OCR and Fia chat

python3 server.py
```

Then open `http://localhost:8766`. `PORT`, `WEATHER_LAT`, `WEATHER_LON`, `WEATHER_TZ` and
`FP_DATA_DIR` can go in the environment or a `.env` file next to `server.py`.

## Tests

There are no automated tests. Check changes by hand: start the server, open the dashboard on a
desktop browser and on a phone or tablet, and try the parts you changed. Data is stored in JSON
files, so point `FP_DATA_DIR` at a scratch folder if you do not want to touch your real data.

## Pull requests

Small and focused is easiest to review. The frontend is plain JavaScript and CSS with no
frameworks, so please keep it that way. For big changes, open an issue first so we can talk it
through.

Please follow the [code of conduct](CODE_OF_CONDUCT.md).
