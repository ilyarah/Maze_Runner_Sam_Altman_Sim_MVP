
# Maze Runner × Teenage Sam Altman Simulation MVP

**A 16-year-old Sam Altman wakes up in the Box. The Glade awaits.**

> “Sometimes the best way out of a maze… is to become the one who maps it.”  
> — teenage Sam Altman (probably)

<p align="center">
  <img src="https://via.placeholder.com/800x300/111827/ffffff?text=Maze+Runner+×+Teen+Sam+Altman" alt="Maze Runner meets teenage Sam Altman" width="720"/>
</p>

## 🎮 What is this?

A compact, single-file Python simulation that drops a teenage version of **Sam Altman** straight into the world of *The Maze Runner*.

Using **fixed Big Five (OCEAN) personality traits**, probabilistic decision-making, health tracking, evolving Glader relationships, and short LLM-generated narratives, watch Sam survive (or not) the early days in the Glade.

It’s psychological agent simulation meets interactive fan-fiction with a very particular sense of humor.

## ✨ Highlights

- Personality-driven choices (high Openness → explores everything, high Agreeableness → instant friend-maker)
- Scripted events inspired by the book's first act
- Health & relationship tracking with sensible bounds
- Extremely token-efficient OpenAI narratives (gpt-3.5-turbo) + perfect fallback text
- Beautiful console output + summary table
- Automatic Matplotlib health progression plot
- Bulletproof error handling everywhere

## 🎥 Example Output (shortened)

```
════════════════════════════════════════════════════════════
      MAZE RUNNER SIM MVP  -  Sam Altman (age 16)
════════════════════════════════════════════════════════════
OCEAN: {'O': 0.82, 'C': 0.75, 'E': 0.65, 'A': 0.88, 'N': 0.48}
════════════════════════════════════════════════════════════

Day  1  |  Sam wakes in the dark rising Box, heart pounding.
   → Decision: default
   → Outcome:  positive

   Sam defaulted during the arrival event. Result: positive. Health now 100.

   Health: 100   |   Relationships: Newt:0.50  Thomas:0.30  Chuck:0.40

[...dramatic days later...]

════════════════════════════════════════════════════════════
                     SUMMARY TABLE
════════════════════════════════════════════════════════════
Day | Event (short)              | Dec    | Out    | Health | Relations
────────────────────────────────────────────────────────────
  1 | Sam wakes in the dark ri... | default| pos    |  100 | N:0.5 T:0.3 C:0.4
  3 | A Griever is seen crawli... | explore| neg    |   88 | N:0.6 T:0.4 C:0.5
  6 | Tensions rise during the... | befriend| pos   |  100 | N:0.7 T:0.5 C:0.6

[Matplotlib health plot appears here]
```

## 🚀 Quick Start

```bash
git clone https://github.com/ilyarah/Maze_Runner_Sam_Altman_Sim_MVP.git
cd Maze_Runner_Sam_Altman_Sim_MVP

pip install -r requirements.txt

# Set your key (very light usage)
export OPENAI_API_KEY="sk-..."

python simulation/main.py
```

**Dependencies** (that's all):
```txt
openai>=1.0.0
matplotlib>=3.5.0
```

## 🛠️ Current Structure (MVP – single file)

```
.
├── simulation/
│   └── main.py           ← everything lives here for now
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚡ Easy Tweaks

- Edit Sam's OCEAN profile in `main()`
- Add/expand events in `SCRIPTED_EVENTS`
- Tune health & relationship deltas
- Switch to `gpt-4o-mini` for richer (but more expensive) prose

## ⚠️ Disclaimer

This is a **humorous creative experiment** and **not** an official depiction of any real person.  
Made for fun, learning, and because the concept was too absurd to ignore.

## 📜 License

[MIT License](LICENSE) — fork, modify, meme, enjoy.

---

**Created with love, randomness, and a healthy dose of existential dread**  
Merry Christmas 2025 🎄
```

Just replace the placeholder image URL with a real screenshot when you add one (highly recommended).  

Happy holidays and happy simulating! 🚀
