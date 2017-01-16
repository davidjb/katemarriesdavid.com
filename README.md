# Readme

Yes, our wedding website is online and yeah, it's on GitHub.  So what?  Why not make an awesome wedding even more awesomer?

## Prereqs

```bash
brew tap homebrew/tex
brew install pdfjam
```

## Commands

Create single page with multiple copies of the same document:

```bash
# Portrait
pdfjam --a4paper --nup 1x2 --delta '4mm 4mm' --scale 0.98 --outfile save-the-date-pdfjam.pdf save-the-date.pdf save-the-date.pdf

# Landscape
pdf90 save-the-date.pdf
pdfjam --landscape --a4paper --nup 2x1 --delta '4mm 4mm' --scale 0.98 --outfile save-the-date-pdfjam.pdf save-the-date-rotated90.pdf save-the-date-rotated90.pdf
```
