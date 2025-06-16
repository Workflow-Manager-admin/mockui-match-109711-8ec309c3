# Design-to-Implementation Mapping Document

This document provides a pixel-perfect and exhaustive mapping of all design elements extracted from the UI implementation in this project. It includes a full organizational breakdown of pages/screens, navigation, layouts, color palette, and every UI component (including minor elements) as implemented in the codebase, referencing their structure, style, and exact page locations. This mapping is intended to serve as a definitive guide to match the design at both macro and micro levels for implementation and QA.

---

## Table of Contents

1. [Page and Navigation Structure](#page-and-navigation-structure)
2. [Color Palette and Style Variables](#color-palette-and-style-variables)
3. [Layout Structure](#layout-structure)
4. [Global UI Components](#global-ui-components)
5. [Page-by-Page Element Mapping](#page-by-page-element-mapping)
6. [Design System Details (Typography, Spacing, etc.)](#design-system-details-typography-spacing-etc)
7. [Component/Style Cross-Reference Table](#componentstyle-cross-reference-table)
8. [Appendix: Complete CSS Variable Reference](#appendix-complete-css-variable-reference)
9. [Mermaid Diagram: Page & Layout Structure](#mermaid-diagram-page--layout-structure)

---

## 1. Page and Navigation Structure

The application is a **single-page app** with one main screen.

- **Navbar**: Fixed at the top, present on all views (currently only one “Home/Welcome”).
    - Contains: app logo (symbol + text) left-aligned, template navigation button right-aligned.
- **Main Content**: Under navbar, vertically centered hero section.

#### Navigation Flow

```mermaid
flowchart LR
    Navbar --- MainContent
    Navbar -->|Logo Click| MainContent
    Navbar -->|Button Click| (Future Navigation)
```

- At this phase, all navigation is non-functional, with only a single page presented.

---

## 2. Color Palette and Style Variables

Defined in `src/App.css` as CSS custom properties, referenced throughout all layout and component styles:

| Variable               | Color Value        | Usage                                  |
|------------------------|-------------------|----------------------------------------|
| `--base-light`         | `#00ffff`         | Accent, logo, subtitle, buttons        |
| `--base-dark`          | `#00008b`         | Background, navbar                     |
| `--text-color`         | `#ffffff`         | Main text, headings                    |
| `--text-secondary`     | `rgba(255,255,255,0.7)` | Descriptions, lower contrast text |
| `--border-color`       | `rgba(255,255,255,0.1)` | Navbar border, subtle dividers     |

Typography font: `Inter, Roboto, Helvetica, Arial, sans-serif`.

---

## 3. Layout Structure

### Overall Hierarchy

- `body`: Dark background, white foreground, no margin/padding.
- `.app`: Flex column, min-height: 100vh.
- `.navbar`: Fixed, full width, horizontal flex container, dark background, subtle border.
    - Child: `.container`
        - Child: Flex block housing `.logo` and `.btn`
- `main`: Static section below navbar.
    - `.container`: Center-aligned, fixed max-width (900px), horizontal padding.
    - `.hero`: Vertically stacked, centered, with top/bottom padding to provide breathing space.

---

## 4. Global UI Components

### Navbar

- **Class**: `.navbar`
    - Fixed at top, z-index 100
    - Padding: 16px
    - Horizontal flex, justify-content: space-between

### Logo

- **Class**: `.logo`
    - Font-size: 1.25rem; font-weight: 600
    - Includes: `.logo-symbol` (color: base-light, symbol: `*`), brand text

### Button

- **Class**: `.btn`, `.btn-large` for large variant
    - Background: base-light (`#00ffff`)
    - Text color: white
    - Rounded corners, no border
    - Padding: 10px 20px (large: 12px 24px)
    - Hover: background-color `#7691ff`

### Container

- **Class**: `.container`
    - Max-width: 900px; horizontal padding; width 100%
    - Used in navbar and main for consistent content width

### Typography

- **Class**: `.title`: 3.5rem, bold, prominent
- **Class**: `.subtitle`: 1.1rem, medium weight, primary accent color
- **Class**: `.description`: 1.1rem, secondary text color, line-height 1.5, max-width 600px

### Hero Section

- **Class**: `.hero`
    - Vertically padded (120px top, 64px bottom)
    - Flex column, centered
    - Gap: 24px between elements

---

## 5. Page-by-Page Element Mapping

### Home/Welcome Page

- Present on: **all loads (only screen in current state)**
- Contains:
    - **Navbar** (fixed, always present)
        - Left: `* KAVIA AI` logo (see logo component)
        - Right: `Template Button` (`.btn`)
    - **Hero Section** (centered):
        - `.subtitle`: “AI Workflow Manager Template” (base-light color)
        - `.title`: `mockui_match` (large, prominent)
        - `.description`: “Start building your application.” (secondary tone)
        - `.btn.btn-large`: “Button”

#### Element Location Reference
| Section     | Component             | Class/Style                | Notes                                  |
|-------------|-----------------------|----------------------------|----------------------------------------|
| Navbar      | Logo symbol+text      | `.logo .logo-symbol`       | Symbol: `*`, color: base-light         |
| Navbar      | Nav Button            | `.btn`                     | Right side, text: "Template Button"    |
| Main/Hero   | Subtitle              | `.subtitle`                | Top of hero                            |
| Main/Hero   | Title                 | `.title`                   | Centered, after subtitle               |
| Main/Hero   | Description           | `.description`             | Under title, max-width 600px           |
| Main/Hero   | Primary Button        | `.btn.btn-large`           | Bottom, labeled: "Button"              |

---

## 6. Design System Details (Typography, Spacing, etc.)

| Element/Class    | Font Size/Weight      | Spacing      | Alignment    | Color/Background            |
|------------------|----------------------|--------------|--------------|-----------------------------|
| `.title`         | 3.5rem, 600          | 0            | center       | text-color                  |
| `.subtitle`      | 1.1rem, 500          | 0            | center       | base-light                  |
| `.description`   | 1.1rem, normal, 1.5x | margin-b:16  | center       | text-secondary              |
| `.btn`           | 1rem, 500            | p:10x20      | inline       | base-light + white text     |
| `.btn-large`     | 1.1rem, 500          | p:12x24      | inline       | inherits btn                |
| `.navbar`        | 1.25rem logo         | p:16         | flex h       | base-dark, border-color     |
| `.container`     | n/a                  | px: 0/24     | center max   | n/a                         |
| `.hero`          | n/a                  | pt:120, pb:64| flex v       | n/a                         |

---

## 7. Component/Style Cross-Reference Table

| CSS Class         | Used In          | Purpose/Notes                                          |
|-------------------|------------------|--------------------------------------------------------|
| `.app`            | App root         | Flex column layout, min 100vh                          |
| `.navbar`         | Navbar           | Top bar, fixed, nav, and branding                      |
| `.logo`           | Navbar           | Brand text & symbol                                    |
| `.logo-symbol`    | Navbar           | Accent symbol, base-light color                        |
| `.container`      | Navbar+Main      | Consistent horizontal bounds/centering                 |
| `.hero`           | Main             | Hero/center stage for call to action                   |
| `.subtitle`       | Hero             | Top-most, accent                                      |
| `.title`          | Hero             | Main title, extra large                               |
| `.description`    | Hero             | Supporting info, softer color                          |
| `.btn`            | Navbar+Main      | Main interactive element, bold color                   |
| `.btn-large`      | Hero/Main        | Larger call-to-action, extra padding                   |

---

## 8. Appendix: Complete CSS Variable Reference

From `src/App.css`:

```css
:root {
  --base-light: #00ffff;
  --base-dark: #00008b;
  --text-color: #ffffff;
  --text-secondary: rgba(255, 255, 255, 0.7);
  --border-color: rgba(255, 255, 255, 0.1);
}
```

---

## 9. Mermaid Diagram: Page & Layout Structure

```mermaid
graph TD
    App[.app (root)]
    App --> Navbar[.navbar (fixed)]
    Navbar --> Logo[.logo]
    Navbar --> NavButton[.btn (Template Button)]
    App --> Main[main]
    Main --> MainContainer[.container]
    MainContainer --> Hero[.hero]
    Hero --> Subtitle[.subtitle]
    Hero --> Title[.title]
    Hero --> Description[.description]
    Hero --> CtaBtn[.btn.btn-large]
```

---

## 10. Visual QA/Implementation Notes

- **Spacing/Padding**: Strict adherence to px values in hero, navbar, buttons for vertical rhythm and comfortable spacing.
- **Color Consistency**: All accent/UI color pulled from variables—no magic values.
- **Component Reuse**: `container`, `btn`, and typography classes are shared between sections for consistency.
- **Responsiveness**: While not fully demonstrated with breakpoints, containers and padding set foundation for responsive adaptation.
- **Pixel-Perfection Guide**: Inspect each section for alignment, spacing, color, and typography per specification above.

---

### Reference: File & Class Mapping

| Element      | File Location                  | CSS Class                |
|--------------|-------------------------------|--------------------------|
| App Wrapper  | src/App.js                     | .app                     |
| Navbar       | src/App.js, src/App.css        | .navbar, .logo, .btn     |
| Container    | src/App.js, src/App.css        | .container               |
| Hero/Main    | src/App.js, src/App.css        | .hero, .title, .subtitle, .description, .btn.btn-large |
| Colors/Vars  | src/App.css                    | :root                    |
| Global reset | src/index.css                  | *                        |

---

This mapping should enable exact implementation—every element (major or minor), its style, and how it fits into the page and navigation structure is catalogued above for both design integrity and engineering clarity.

---

## 11. Appendix: Build Troubleshooting — PUBLIC_URL Error

If you receive the error:

```
Template execution failed: ReferenceError: PUBLIC_URL is not defined
```

This is caused by certain environments (such as some CI/CD pipelines, linters, or manual use of `react-scripts build`) not automatically setting a `PUBLIC_URL` environment variable. This variable is required for Create React App builds/templates in order to generate correct asset links.

### Solution

You must set `PUBLIC_URL` to a valid value when building. Most projects can simply use the `.` (current directory) for local/dry builds, or an appropriate URL if deploying to a subdirectory.

**For local/test builds:**

```sh
PUBLIC_URL=. npm run build
```

**In CI/CD:**

Set an environment/export variable in the build step:
```sh
export PUBLIC_URL=.
npm run build
```
or (single-line)
```sh
PUBLIC_URL=. npm run build
```

### Notes

- This does NOT affect your runtime app, only the build artifacts.
- If you host on a public domain/subfolder, set `PUBLIC_URL` to the root relative path (e.g., `/`, `/app`, etc).
- Read more [in the official CRA docs on PUBLIC_URL](https://create-react-app.dev/docs/using-the-public-folder/#referencing-assets-using-public_url).

**By following this advice, you will avoid the ReferenceError and have a successful build.**
