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
   - Cover (editorial layout, no photo): Highlands logo (230px), hairline, address as the focal point in serif (Cormorant, `1001 Lake Cypress Ln.` with the period, `<b>` street line) with `Little Elm, Texas` (no zip) in small tracked sans capitals beneath, then "Prepared for" with the agent's name large in italic serif and "REALTOR® · Brokerage" (Title · Brokerage, add License # when known), then Devin Kampa / Loan Officer, NMLS #2532480 at the bottom. Cover swaps: street+period, city+Texas, agent name, agent title/brokerage line. The browser title, share text and Save name keep the full address with zip
   - Inside cards are titled "The listing agent's business card" and "The loan officer's business card"; end CTAs are "Call agent" and "Call lender"
   - Flyer images (data URIs in `const IMG`): `neigh` (Neighborhood highlights), `home` (Home highlights), `num` (The Numbers), `w53` / `w5` / `w20` (pre-application worksheets: 5% down + 3% seller credit, 5% down, 20% down). Include only the keys the listing has (1, 2 or 3); delete the others from `IMG`. The folder, the worksheet lift, the scene captions and "The numbers" caption adapt automatically, and `tools/make_pdf.py` skips missing keys
3. Constant for every folder (leave alone): the two trifolds (`proc1`, `proc2`, `high1`, `high2`), the Highlands logo, Devin's business card, Devin's contact buttons.
4. Rebuild the downloadable PDF: `python3 tools/make_pdf.py <address-slug> "<Address> - Listing Folder"` (needs `pip install img2pdf`). This writes `<address-slug>/folder.pdf`, which the Save button downloads.
5. Commit and push. The link is `devinkampa.com/folder/<address-slug>/`.

## Behavior
- Cover tap or "Open the folder" starts a guided tour: Neighborhood, Home, The Numbers, the two trifolds (inside and outside). The worksheets are skipped in the tour.
- When the folder is fully open the tour ends. Tapping any worksheet lifts all of them side by side. "Close folder" returns to the closed cover.
- Page is `noindex`.

- Share button: opens the phone's share sheet (or copies the link on desktop). Save button: downloads `folder.pdf`, one Letter page per flyer.
