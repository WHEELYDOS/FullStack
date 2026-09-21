# Frontend Engineering & UI Components

This directory contains frontend modules covering foundational to advanced web development, including **semantic HTML5**, modern **CSS3** layout techniques (Flexbox, Grid, Subgrid), **Tailwind CSS v4** styling workflows, and core **JavaScript**.

---

## Directory Architecture

```text
frontend/
├── css/
│   ├── bem_methodology/      # Block Element Modifier naming conventions
│   ├── blog_card/            # Responsive blog preview card component
│   ├── box_model/            # CSS Box Model: margins, borders, padding, sizing
│   ├── box_shadow/           # Layered shadows and elevation design
│   ├── css_variables/        # CSS custom properties and theming
│   ├── dashboard_ui/         # Sidebar, metric widgets, and responsive dashboard layout
│   ├── forms/                # Form controls, input states, and user interaction styling
│   ├── gradients/            # Linear/radial gradients and dynamic progress indicators
│   ├── grid/                 # CSS Grid experiments, area layouts, and subgrid implementations
│   ├── login_page/           # Centered authentication layout and form aesthetics
│   ├── mustache_art/         # Pure CSS illustration and shapes
│   ├── navbar/               # Responsive header navigation component
│   ├── practice_layouts/     # Flexbox container and multi-item wrapping practice
│   ├── product_card/         # E-commerce product card with responsive image sizing
│   ├── selectors/            # CSS combinators, pseudo-classes, and specificity hierarchy
│   ├── specificity/          # Selector weight calculations and cascade resolution
│   └── typography/           # Custom font loading (@font-face) and typography hierarchy
├── javascript/
│   ├── index.html            # JavaScript playground HTML harness
│   └── intro.js              # JavaScript fundamentals and logic
├── saas_dashboard/           # Modern SaaS dashboard project workspace
└── tailwind/
    ├── intro/                # Tailwind CSS CDN integration and utility-first basics
    ├── tailwind_starter/     # Tailwind CSS build process with PostCSS configuration
    └── tailwind_components/  # Modern Tailwind cards and component composition
```

---

## Getting Started

### Static HTML/CSS Pages
All exercises in `css/`, `javascript/`, and `tailwind/intro/` are self-contained and run directly in any modern browser.
You can open them directly or use the VS Code **Live Server** extension.

### Tailwind CLI Projects (`tailwind_starter`, `tailwind_components`)
For projects utilizing the Tailwind CLI build pipeline:

```bash
cd tailwind/tailwind_starter  # or tailwind/tailwind_components

# Install dependencies (only required once)
npm install

# Build / watch styles
npx @tailwindcss/cli -i ./src/input.css -o ./dist/output.css --watch
```
Open `src/index.html` in your browser to view live updates.
