# Listing folder template

> **Reference build (approved Oct 2026):** `1001-lake-cypress-ln/` (https://devinkampa.com/folder/1001-lake-cypress-ln/) is the approved look and behavior for every new folder. `template/index.html` has identical code to it; only the listing details (address, agent, flyers, captions, share text) differ. If the two ever disagree, match Lake Cypress, and do not change layout, tour order, buttons or wording unless Devin asks.

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

## Updates from 4824 Cedar Creek Dr (Oct 15, 2026)
- **Highlands disclaimer footer:** `#legal` is now a centered line at the bottom of the page on desktop (12px, up to 920px wide) and phone (10px, full width, 2-3 lines); phone `#bar` and `#cap` sit higher so nothing overlaps. Already applied to `template/index.html` and the Cedar Creek folder. Lake Cypress, Salado and Greymoore still have the older small right-aligned version.
- **Seller-credit worksheet (`w53`):** its label is `WSL.w53` ("5% down with a 2.25% seller credit" for Cedar Creek; change the percent per listing, search for "seller credit"). The red "SELLER PAYS CLOSING COSTS" oval starburst sticker (solid bright red #F0140B, pointy edges on an oval outline, white border, white bold caps text, slight rotation) goes ONLY on The Numbers flyer (on the seller-credit / rate-buydown card, straddling the bottom of its cash-to-close box). Never put it on the pre-application worksheets. Same rule for a rate-buydown stamp.
- **Co-branding rule (Devin, Oct 15, 2026):** unless Devin uploads the listing agent's business card (explicit permission to co-brand), keep ALL agent info blank placeholders: "Your Name Here", "Your Brokerage", License #12345, (555) 555-5555, example email, empty photo circle/tile. That is what the template already holds, so only swap the listing details. Do not pull the agent's name, license, phone or brokerage from Zillow. Once a card is uploaded, fill in the real agent as before.
- Flyers for new listings are built as HTML at 1224x1584 (Cormorant + Montserrat) and rendered with Playwright; Numbers fine print also states HOA when the listing has one.

- **Rule (Devin, Oct 15, 2026):** red seller/closing-cost/rate-buydown stickers or stamps are applied only to The Numbers flyer, never to worksheets. If no agent business card is uploaded, fill agent fields with the examples and "Your Name Here".

## Flyer generator (Oct 15, 2026)
`tools/flyers/build_flyers.py` builds the three flyers from a listing JSON (see `tools/flyers/README.md`). Example: `tools/flyers/listings/4824-cedar-creek-dr.json`. Defaults to blank agent info; the sticker only appears on a Numbers card with a `stamp` entry.

## Lessons from 1008 10th St (Oct 15, 2026)
- Neighborhood flyer top photos: use a close photo of the home/lot and a community amenity (pool), not a wide neighborhood aerial; it crops better beside the title box.
- "In the Community" blurb is descriptive, lifestyle-style copy (what living there feels like: pools, trails, events, schools), not a bare list. Never state the HOA dollar amount in it.
- `build_folder.py` builds the folder from the listing JSON; agent info is real only when the JSON has an `agent` block (business card uploaded).
- End-of-tour grey line under the CTAs (Devin, Oct 15, 2026): "Listing your home and need a custom property folder? Text 320-241-5823!" (replaces "Want your own custom listing folder?"). Applied to the template and all existing folders.

## 1429 Macrae Ct (Oct 16, 2026)
- Three worksheets: map the keys to the order shown (w53 = 5% down no points, w5 = 5% down with points, w20 = 20% down) and set `folder.labels` in the listing JSON so the captions read correctly. `build_folder.py` handles it.
- Agent business cards can arrive as HEIC photos: `pip install pillow-heif`, convert, crop the headshot. Agent block in the JSON (`name`, `title`, `brokerage`, `phone`, `email`, `web`, `photo`) fills flyers and the folder.
- A virtually staged listing photo is fine on the Home flyer only if its "VIRTUALLY STAGED" label stays visible in the crop.

## Agent business card = the REAL uploaded card (rule from Devin, 1429 Macrae)
When an agent card is uploaded, the folder's left-pocket card must be THAT exact card, not a recreated look-alike.
1. `python3 tools/flyers/prep_card.py <card.heic|jpg> tools/flyers/listings/card-<slug>.jpg [--corners TLx,TLy,TRx,TRy,BRx,BRy,BLx,BLy]` straightens, whitens and sharpens it (1400x800). Check the result by eye; pass corners if the auto crop is off.
2. Set `"card": "card-<slug>.jpg"` in the listing's `agent` block. build_folder.py then shows the image full-bleed (IMG.agentcard) instead of the HTML recreation. Agent name/phone/email still drive the CTA buttons, cover and flyer footers.
3. No card uploaded: keep the blank "Your Name Here" HTML card.

## Sign-in card (test phase: 4824-cedar-creek-dr only)
`python3 tools/flyers/add_signin.py <slug> [--agent "Name"]` adds the grey sign-in card over a blurred screenshot of the open folder (idempotent; rerun after any rebuild). It posts to the Netlify endpoint (private repo devinkampa-signin, Resend email to agent + Devin). Register the folder's agent first with `tools/flyers/register_signin.py`. Do NOT add it to other folders until Devin approves. Gotchas learned: prefix every class with `so` (the folder has its own .panel/.f/.btn), never validate on blur (a layout shift mid-tap makes the tap miss the button), show errors on submit and clear on input. Add `?signin=1` to a folder URL to see the card again after signing in.
