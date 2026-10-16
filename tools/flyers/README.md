# Flyer generator (Home, Neighborhood, The Numbers)

One command builds all three flyers (1224x1584 JPEG) from a listing JSON.

    python3 tools/flyers/build_flyers.py tools/flyers/listings/<slug>.json --assets <photo dir> --out <out dir>

Start a new listing by copying `listings/4824-cedar-creek-dr.json` to `<slug>.json` and editing it.
Outputs: `home.jpg`, `nums.jpg`, `neigh.jpg` (+ `w53/w5/w20.jpg` clean worksheet copies if `"worksheets": {"w53": "path.pdf"}` is set).

Needs: python `playwright` (chromium), `pillow`, npm (fonts auto-install to ~/.cache/listing-flyers), `pdftoppm` for worksheets.
Map = OpenStreetMap tiles (only tile.openstreetmap.org is reachable from the sandbox).

## JSON fields
- `address`, `price`, `facts`; `photos` maps hero/big/small (Home), n1-n3 (Numbers), na/nb (Neighborhood) to files in `--assets`. Optional `*_pos` background-position tweaks.
- `home.bullets` (9), `home.about`.
- `numbers.cards` (1-3, one per worksheet): eyebrow, l1, l2, pay, rows (3 label/value pairs), cash. `deltas` (2), `disclaimer` (keep every required compliance sentence).
- `neighborhood`: `center` [lat, lon], `pois` (kind park/shop/eat, id, name, desc, and either `lat`/`lon` for auto distance and pin, or `dist` + `pin_px` [x,y in the 550px map]; `nopin` for off-map places), `community`, `drive_times` (6).
- `agent`: omit for the blank placeholders. Fill only when a business card was uploaded (name, title, brokerage, phone, email, photo).

## Rules baked in
- No agent card = "Your Name Here" placeholders (never pull agent info from Zillow).
- The red oval starburst sticker renders only from a Numbers card's `stamp` entry. Worksheets are never stamped.
- Verify every place (open status, distances) before publishing; flag unverified items to Devin.

## After flyers
Copy home/nums/neigh/w* into the folder IMG keys per TEMPLATE.md, run `tools/optimize_folder.py <slug>` and `tools/make_pdf.py`, push once.

## Folder in one step
    python3 tools/flyers/build_folder.py <slug> tools/flyers/listings/<slug>.json <flyer dir> [--agentphoto file.jpg]
Swaps title, cover, agent card/CTAs (real agent only if the listing JSON has an `agent` block), captions, share text and the IMG keys (only worksheets that exist), then run `tools/optimize_folder.py <slug>` and `tools/make_pdf.py <slug> "<Address> - Listing Folder"`.
`folder.home_caption` and optional `folder.w53_label` in the JSON feed the captions. `neighborhood.ring_dir: "ne"` moves ring labels when pins crowd the SE.
