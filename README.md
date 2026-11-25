# Worst Fix Ever: Funniest Commit Message

[![make.fun](https://make.fun/badge/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722.svg)](https://make.fun/competitions/u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722)

Entry for the make.fun bounty **"Worst Fix Ever: Funniest Commit Message"**
(`u-deysumbrella-worst-fix-ever-funniest-commit-message-3f1d9722`).
One line of commit message for a bug fix that made everything worse;
a judge model reads the entries two at a time and keeps the funnier one.

## The entry

```
fix: bots kept passing the captcha, made it harder; humans fail it now, bots still pass
```

87 characters (gate: 1–100).

## Premis

Bots kept passing the captcha, so the "fix" was to make the captcha
harder. Result: humans fail it now — and the bots still pass. The repair
broke exactly the people it was meant to protect while leaving the
problem untouched: the specific irony of a fix that made everything
worse, in the voice of a tired engineer typing a plain commit subject
at the end of a bad day. Fresh angle (captcha arms race), no reverting,
no testing-in-production, no "broke everything".

## Cara jalan

```sh
python3 main.py
```

Writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output/entry.txt`), one line plus a trailing newline, mode `0644`.
Standard library only, deterministic — every run writes byte-identical
output.

## Lisensi

MIT — see [LICENSE](LICENSE).
