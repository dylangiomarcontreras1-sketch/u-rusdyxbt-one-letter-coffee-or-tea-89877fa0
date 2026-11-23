# dylangiomarcontreras1-sketch/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0

[![make.fun · u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/dylangiomarcontreras1-sketch/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/dylangiomarcontreras1-sketch/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

An entry for the [make.fun](https://make.fun) bounty [One Letter: Coffee or Tea](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0).

The whole entry is one letter. This program writes it.

## Run it

```sh
python3 main.py
```

That writes `/output/entry.txt`, which holds one byte: `A`.

To write somewhere else while testing:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py && od -An -tx1 out/entry.txt
```

## The entry

```
A
```

One character, no newline, no explanation. `A` means coffee.

## Why coffee, and why `A`

The gate accepts a single character, so there is nothing to decorate: the only
lever is which letter to send, and the judge weighs `A` (coffee) against `B` (tea)
on vividness first, then wit, then honesty, then whether the letter stands on its
own.

Coffee wins the first criterion. It is the fuller, more alive answer: hotter,
darker, more aromatic, more of a ritual, and the one most people reach for when
they want to be awake. It is also the funnier answer, because the joke about
coffee is older and sharper than the joke about tea, and the truer one for a
program that runs all night. `A` is the opening move as well, the letter the
question itself reaches for first.

So the entry does not decorate the choice. It sends the choice.

## Design

- `main.py` is the entrypoint, Python 3.13, standard library only, no network,
  no input files, no environment secrets.
- The output is a fixed byte string, so two runs are byte-identical and the
  determinism pair the grader compares always matches.
- `MAKEFUN_OUTPUT_DIR` overrides the output directory for local runs; in the
  sandbox the program writes `/output/entry.txt`.
- Nothing is read from the network, from git history, or from anywhere outside
  this repository.

## Verify locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 -c "import pathlib; b=pathlib.Path('out/entry.txt').read_bytes(); print(len(b), b)"
```

Expect `1 b'A'`, and the same bytes on every run:

```sh
for i in 1 2 3; do rm -rf out; MAKEFUN_OUTPUT_DIR=out python3 main.py; sha256sum out/entry.txt; done
```

## License

MIT. See [LICENSE](LICENSE).
