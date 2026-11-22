# Folder styles (5 separate templates)

Each style is its OWN template with its own skeleton. Never blend them. Prompt: "<Style> at <address>" plus the pre-app sheets, photos and listing link.

| Style | Look | Flyer skeleton | Builder |
|---|---|---|---|
| Heirloom | navy / gold, serif, colored flyers (the only colored one) | editorial, hero fades into flyer | `t1_heirloom.py`, `real_heirloom.py` |
| Metropolitan | oxblood / ivory | NOT yet sent live (`t2_metropolitan.py`) | `t2_metropolitan.py` |
| Azure | dark grey / white, Poppins+Inter | left sidebar + right column, section chips | `lay_azure.py`, `real_azure.py` |
| Terra | espresso / cognac, Quicksand+Nunito | centered, rounded cards, floating title card | `real_terra_n.py` (`real_terra_c.py` supplies photo dict) |
| Evergreen | forest / bronze | its own editorial grid | `lay_evergreen.py`, `real_evergreen_c.py` + `real_evergreen_p.py` (plain) |

Live examples: devinkampa.com/folder/Heirloom, /Azure, /Terra, /Evergreen.
`templates/<style>/folder.html` = the empty (sample-address) folder shell for each style.

## Setup in a fresh session
`sh tools/styles/setup.sh` (copies to /home/claude/work/styles, which the code hardcodes; restores the Heirloom source data).

## New listing recipe
1. Copy the style's `real_<style>.py` to `real_<slug>.py`; replace the data (S, NEIGH/TILES, MOVE/MONTHLY/SETUP, CARDS from the worksheets, DELTAS, DISC, map PINS, photo dict). Photos go through `pho()`/`pic()`; pick the right crop per photo.
2. Run it: renders 4 flyers (home, neigh, num, move) to a `real_*/` dir (1224x1584 JPEG).
3. Folder: copy the 4 JPEGs into `out/<style>/`, run `python3 build_folders.py <style>`, then swap sample text: scene captions (keep the customized ones), `Anytown, Texas` -> city, `123 Sample Street` -> address; confirm no "sample" remains outside base64. Write to `out/<style>_real/folder.html`.
4. Test (Playwright desktop 1440x900 + phone 390x844, no page errors). Show Devin a preview of the flyers first; push to `<Name>/index.html` only on his go-ahead (one push).

## The rules (apply to every style, keeping each style's own skeleton)
1. Color: the FOLDER carries the color; contrast should "feel" through the screen. The FLYERS themselves are plain white/black (except Heirloom, which is colored), with a marker highlight on key dollar figures.
2. Presentation: the four flyers flow into each other and complement each other.
3. Home Highlights: the main photo fades (gradient) into the flyer; the info complements it. No more than ~3 photos on Home.
4. Pictures: the home is the main highlight; use more and larger photos from the uploaded set, filling space.
5. Usage: every flyer well used, little dead space.
Also: each flyer uses a different photo SHAPE (curve, arch, oval, plain rounded), never the same shape repeated. Styles must not blend; keep uniqueness.

## Fixed content rules
- Unbranded example: agent = "Your Name Here / Your Brokerage / (555) 555-5555 / you@example.com", empty photo circle, unless Devin uploads that agent's card (then use the exact straightened card).
- No sign-in sheet unless requested in the initial request.
- The Numbers disclaimer must state: estimates only, not a loan approval; price/rate/APR/payment assumptions; actual costs could be higher, get an official Loan Estimate; Devin Kampa is a loan officer, not a licensed real estate agent or Realtor, and the listing is exclusive to the listing Realtor or builder; Highlands Residential Mortgage, Ltd., NMLS #134871 (www.nmlsconsumeraccess.org); Equal Housing Lender.
- "Digitally Altered" / "Virtually Staged" photo labels must stay visible; if staging cannot be verified, ask Devin.
- Finalize every section; if something is blocked or unverifiable, ask before leaving a gap.
- Neighborhood: parks/trails, errands, 3 verified restaurants, drive times, OSM map (pins approximate; tile.openstreetmap.org needs a User-Agent). Nominatim/Overpass/Google/Yelp are blocked.
- Remind Devin that Highlands compliance should review before printing or sharing.

## Deploy
Worktree off origin/main, copy folder.html to `<Name>/index.html`, commit, push to main. Add/replace the catalog card (tools/catalog; the catalog shows only the top 6). Never push the local favicon commit c2202ca.
