# Listing folder template

`template/index.html` is the master copy of the interactive 3D listing folder (grey folder, white page).
It is a single self-contained file: all flyers, fonts-free styling, and scripts are inside it.
It was built from the 1108 Salado Dr folder, so that listing's details are what is currently in it.

## To make a new listing folder
1. Copy `template/index.html` to `<address-slug>/index.html` (lowercase, hyphens, e.g. `2204-oak-hollow-ln`).
2. Swap the listing-specific content (search for these in the file):
   - `<title>`: "1108 Salado Dr Folder"
   - Cover address line: `1108 Salado Dr, Allen, TX 75013` (also in the first scene `SC[0]` caption and the "custom numbers" wording)
   - Agent line on the cover: `Jonathan Realtor · Real Estate Agent · License #12345`
   - Agent business card (left pocket): "Your Brokerage", Jonathan Realtor, Real Estate Agent, License #12345, (555) 555-5555, jonathan.realtor@example.com, www.example.com, initials "JR"
   - Agent CTA buttons at the end: `tel:+15555555555`, `sms:+15555555555`, `mailto:jonathan.realtor@example.com`
   - Home highlights caption: bedrooms, baths, square feet, features
   - Save button: the `download="..."` name on `#dlB` ("1108 Salado Dr - Listing Folder.pdf"), and the share text/title in the `#shareB` handler
   - Cover (editorial layout, no photo): Highlands logo (160px), hairline, address as the focal point in serif (Cormorant, `1001 Lake Cypress Ln.` with the period, `<b>` street line) with `Little Elm, Texas` (no zip) in small tracked sans capitals beneath, then "Prepared for" with the agent's name large in italic serif and "REALTOR® · Brokerage" (Title · Brokerage, add License # when known), then Devin Kampa / Loan Officer, NMLS #2532480 at the bottom. Cover swaps: street+period, city+Texas, agent name, agent title/brokerage line. The browser title, share text and Save name keep the full address with zip
   - Cover v3 (Oct 2026): Devin's name and NMLS are NOT on the cover face (the old `.sig` block is removed). The "Prepared for" agent block sits below the address, centered. The caption under the folder (first scene `SC[0]` `s:`) reads "A listing folder prepared for you by Devin Kampa at Highlands Residential Mortgage."
   - Inside cards are titled "The listing agent's business card" and "The loan officer's business card"; end CTAs are "Call agent" and "Call lender"
   - Flyer images (data URIs in `const IMG`): `neigh` (Neighborhood highlights), `home` (Home highlights), `num` (The Numbers), `w53` / `w5` / `w20` (pre-application worksheets: 5% down + 3% seller credit, 5% down, 20% down). Include only the keys the listing has (1, 2 or 3); delete the others from `IMG`. The folder, the worksheet lift, the scene captions and "The numbers" caption adapt automatically, and `tools/make_pdf.py` skips missing keys
   - Flyer footers (all 3 flyers): no "YOUR AGENT" / "YOUR LENDER" tag above the names. Just the photo, name, title, phone, email and brokerage/logo.
3. Constant for every folder (leave alone): the two trifolds (`proc1`, `proc2`, `high1`, `high2`), the Buy Before You Sell flyer (`bys`, Devin's branded FlexCap flyer with his newer headshot), the Highlands logo, Devin's business card, Devin's contact buttons.
4. Rebuild the downloadable PDF: `python3 tools/make_pdf.py <address-slug> "<Address> - Listing Folder"` (needs `pip install img2pdf`). This writes `<address-slug>/folder.pdf`, which the Save button downloads.
5. Commit and push. The link is `devinkampa.com/folder/<address-slug>/`.

## Behavior
- Cover tap or "Open the folder" starts a guided tour: Neighborhood, Home, then the right pocket front to back: the two trifolds (closed, cover faces only), The Numbers, Buy Before You Sell, and the pre-application worksheets side by side last. Trifolds still open when tapped in the explore view.
- When the folder is fully open the tour ends. Tapping any worksheet lifts all of them side by side. "Close folder" returns to the closed cover.
- Page is `noindex`.

- Share button: opens the phone's share sheet (or copies the link on desktop). Save button: downloads `folder.pdf`, one Letter page per flyer.


## Performance step (every folder)
After swapping the content and before `tools/make_pdf.py`, run `python3 tools/optimize_folder.py <folder-slug>`. It adds lighter `_s` copies of the flyers, worksheets and trifolds to `const IMG`; the 3D scene uses those (as blob URLs, decoded once), while "View full size" and `folder.pdf` keep the full-size images. This prevents phones from running out of memory and reloading. Re-running is safe.

## UI notes
- Top-right buttons (View full size, Skip, Replay, Close folder) and the Share/Save buttons are all 36px tall and aligned. Share/Save become icon-only at 480px wide and below so the top buttons never overlap on large iPhones (402-440px). Button heights are the original 40px; View full size has a blue gradient (no icon).
- End CTAs: agent button reads "Call the Agent", lender button reads "Call a Lender"; each button row is nudged 8px left.


## Right pocket order (Oct 2026)
Back to front: the pre-application worksheets (1 to 3), then **Buy Before You Sell** (`bys`), then The Numbers, then the two trifold stacks, then Devin's card. Every folder gets Buy Before You Sell; it is already in `template/index.html`, so copying the template is enough.
- Positions and hit zones are computed from the pieces present (`BYS_TOP`, `BYS_H`, `NUM_TOP` near the top of the script), so 1, 2 or 3 worksheets all stack cleanly. Buy Before You Sell has its own tap zone (56 px tall in folder units, directly above The Numbers); the worksheet zone sits above it.
- Tour dots are built from the scenes present (`DOTIDS`), and scene lookups are by id, so adding or removing a scene no longer needs index edits.
- Worksheet zone now opens the first worksheet the listing has (it used to assume `w5`).
- `tools/make_pdf.py` puts the page right after The Numbers; `tools/optimize_folder.py` makes the small `bys_s` copy.
- To refresh the flyer image later, replace `IMG.bys` (1224 px wide JPEG, about 390 KB) and re-run `optimize_folder.py` and `make_pdf.py`.
