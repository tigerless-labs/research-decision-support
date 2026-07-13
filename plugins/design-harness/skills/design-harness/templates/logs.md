# logs — append-only change ledger (covers both the ideas and output layers)

Convention: each line is `- date · card/doc · action · delta (minimal old → new) · reason`;
record the **delta itself**, not just the action and reason; once output exists, the same
change gets one line per layer (one idea line + one output line); append only, never rewrite
old lines — the docs stay out of git, so this ledger is the only way back.
