# Total E-Clips

Race to produce the most paperclips before your fellow AI beat you to it!

## Development Setup
### Card Maker
Built using [Version 1.0.0.2](https://github.com/nhmkdev/cardmaker/releases/tag/v.1.0.0.2) of Card Maker by Tim Stair
1. Download the .zip file after following the link above
2. Extract and run `CardMaker.exe`
3. Go to `File` | `Open Project...` and open `eclips/totaleclips.cmp`

### VSCode
VSCode is used to edit the `.md` files and produces a PDF of the Rules
1. Download `Markdown PDF` by "yzane" in the VS Code Marketplace

## Development
### Export the project
1. Click `File` | `Export Project to PDF...`
2. Click `OK`

### Create the Rules .pdf
1. See "Development Setup" for VSCode setup
2. `Ctrl` + `Shift` + `P` to open the command prompt
3. Type `"export"` and select `Markdown PDF: Export (PDF)`

### Build 'Bonus Token' Images
1. Click `Tools` | `Settings...` and disable `Print/Export Layout Border`. Click `OK`.
2. Right-click the "Bonuses" Layout and select `Export Card Layout as Images...`
3. Set the `File Name Format` to `@[filename]`
4. Set the output folder to `totaleclips\eclips\res`
5. Click `OK`
6. Press `F6` to "Refresh the Image Cache" to load the new images
7. Click `Tools` | `Settings...` and re-enable `Print/Export Layout Border`. Click `OK`.

## Troubleshooting
#### Guide
A copy of the guide has been source controlled with the project and is located in the `docs/` folder (Download link needed, where did I find this??).

#### Images showing up as `BAD NAME` or `BAD REFERENCE`
Ensure that the layout type is set to `FormattedText` and not `Text`

#### Additional Resources:
[Card Maker User's Guild](https://www.boardgamegeek.com/guild/2250)
