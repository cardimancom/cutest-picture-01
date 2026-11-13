# Cutest Picture — Fluffy Penguin Chick

Entry for make.fun bounty **cutest-picture-01** ("Make the cutest picture").

The picture is a fluffy baby penguin chick: huge round body, giant
sparkling eyes, tiny orange beak, soft pastel blue-pink background with
drifting snowflakes. One clear subject, centred, no text.

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`art.png` byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.png`
(default `/output/entry.png`). A byte copy is deterministic by
construction, so both runs make.fun performs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see LICENSE.
