# Folder catalog (devinkampa.com/folder)

One-page portfolio of every listing folder. `index.html` at the repo root is generated; do not hand-edit it.

## Add a new folder
1. Screenshot the folder in its open state, crop to the folder, save as `thumbs/<slug>.webp` (1000x720, white background).
2. Add a row to the list `L` in `build_catalog.py`: (slug, address, city, bedrooms). Add the slug to `CR` if its The Numbers flyer shows a percentage seller credit (gets the "Seller Credits" tag).
3. Run it from a folder holding `template.html`, `site/thumbs/`, `site/highlands-logo.png` (paths are relative to where it runs), then copy the generated `site/index.html` to the repo root. Commit and push.

Page stays `noindex`. Cards link to the live folder pages. No agent names appear on the page.
