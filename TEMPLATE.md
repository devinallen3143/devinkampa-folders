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
   - Flyer images (data URIs in `const IMG`): `neigh` (Neighborhood highlights), `home` (Home highlights), `num` (The Numbers), `w53` / `w5` / `w20` (three pre-application worksheets)
3. Constant for every folder (leave alone): the two trifolds (`proc1`, `proc2`, `high1`, `high2`), the Highlands logo, Devin's business card, Devin's contact buttons.
4. Commit and push. The link is `devinkampa.com/folder/<address-slug>/`.

## Behavior
- Cover tap or "Open the folder" starts a guided tour: Neighborhood, Home, The Numbers, the two trifolds (inside and outside). The three worksheets are skipped in the tour.
- When the folder is fully open the tour ends. Tapping any worksheet lifts all three side by side. "Close folder" returns to the closed cover.
- Page is `noindex`.
