# The Arc So Far

A browser-based slide deck: a high-level overview of the AI landscape as it stands in 2026, written for a QA / quality-engineering audience. Runs entirely offline in any modern browser, no build step or internet required to view.

**Live preview:** https://arc-so-far.vercel.app

## View it

Open `index.html` in a browser (double-click, or drag it into a tab). That's it, everything is self-contained: the fonts (Inter) are embedded, and there are no external requests at runtime.

## Controls

| Key / action | Does |
|---|---|
| Right arrow, Space, PageDown, or click | Next slide |
| Left arrow, PageUp | Previous slide |
| Home / End | First / last slide |
| `s` | Toggle presenter notes (one paragraph per slide) |
| `f` | Fullscreen (Esc to exit) |

Works with a presentation clicker (they send PageUp/PageDown).

## Structure

21 slides in four acts. The deck alternates **light** working slides with **deep-green** statement slides for rhythm; each slide's light/dark identity is fixed, so it looks the same on any screen regardless of the viewer's system theme.

- **I - Foundations** (2-5): what AI was before ChatGPT, the moment, what an LLM is, why it hallucinates
- **II - The Three Eras** (6-13): prompting, context, and loop/agents, each with a QA example, then human-in-the-loop
- **III - Landscape & Trajectory** (14-17): the tool landscape, the model landscape, AI in BI/QA, where it's heading
- **IV - What This Means** (18-21): three shifts in the QA role, the build, and the close

Deep (dark) slides: 1, 6, 13, 18, 21. Everything else is light.

## Edit it

Two ways:

1. **Quick content tweaks** - edit `index.html` directly. It's one file. Slide text lives in `<section class="slide">` blocks; presenter notes are the `<aside class="notes" hidden>` inside each.

2. **Cleaner source editing** - edit `src/deck-template.html` instead (same file, but the embedded fonts are `@@INTER...@@` placeholders, so it's ~30 KB instead of ~215 KB and easy to search). Then regenerate:

   ```sh
   python3 src/build.py
   ```

   That rewrites `index.html` with the fonts inlined.

### Design system (fixed)

- Background (light slides) `#fafaf9`, ink `#0f172a`, accent emerald `#059669`, mint cards `#d1fae5`
- Deep slides `#022c22` with white ink and bright-mint `#6ee7b7` accents
- One lone amber accent (`#c2740c`) marks the "always" horizon on slide 17
- Type: Inter (all weights embedded). Headings 700/800, body 400/500
- Colors are CSS custom properties; deep slides just redefine the tokens locally, so any slide can be made light or dark by adding/removing `class="... deep"`

## Deploy

Any static host works (it's a single file). For Vercel:

```sh
vercel --prod
```

## Notes

- Factual claims are sourced; citations live in the presenter notes (`s`) of the relevant slides.
- Slides 19-20 (the build) are intentionally generic and hand off to a separate live demo.
