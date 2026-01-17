# Quantum8Lines — Intro System

This repository contains the **intro animation system** for the *Quantum8Lines* channel.

This is **not a single video**.  
It is a reusable, high-density mathematical animation framework built with **Manim**.

The intro is treated as **visual infrastructure**, not content.

---

## Philosophy

- Target audience: **Intermediate → Advanced → Research → PhD**
- No dead frames
- No decorative motion
- Motion encodes mathematical meaning
- Density over accessibility

If a second feels empty, the system has failed.

---

## What This Repo Is

- A standalone intro engine
- A testbed for motion grammar and camera language
- A reusable asset across platforms:
  - YouTube (16:9)
  - Shorts / Reels (9:16)
  - Trailers / teasers

---

## Structure

src/
├── core/ # camera rules, motion grammar (do not touch lightly)
├── sequences/ # conceptual animation bursts (2–7 seconds each)
└── intro_master.py # timeline orchestration only


- `core/` defines **laws**
- `sequences/` define **ideas**
- `intro_master.py` defines **time**

---

## Output

- High frame-rate (60 FPS)
- Black background
- No baked-in narration
- Designed for aggressive visual pacing

---

## Development Status

Active.
Expect breaking changes while visual grammar is refined.

---

## Rendering

```bash
manim -pqh src/intro_master.py Quantum8LinesIntro
