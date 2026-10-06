# Adding content

## Publications and graphical abstracts

Edit `_bibliography/papers.bib`. Use the author's family name first, separated by `and`; keep publication status explicit. Use `category={lead}` for first-authored or co-first-authored work, or `category={collaborative}` for other collaborations.

Place approved artwork in `assets/img/publication_preview/`, then add `preview={filename.png}` to the matching entry. Images are optional. Clicking an image opens al-folio's zoom view. DREAM and DRIFT use existing method figures. SAFE-AD and the pipeline diagnosis paper use supplied graphical abstracts. Sources are documented in `docs/migration/figure-sources.md`.

Supported fields include `abstract`, `doi`, `arxiv`, `code`, `pdf`, `video`, `website`, `slides`, and `poster`. Add only verified information and available files. `selected={true}` places the paper on the homepage. `bibtex_show={true}` enables the BibTeX button; use it only for work with a publicly available preprint. Omit this field for work without a preprint. Put status text in `note`; al-folio displays it below the venue.

```bibtex
@misc{your_unique_key,
  title = {Your manuscript title},
  author = {Wang, Zian and Collaborator, Given Name},
  category = {lead},
  note = {Under review},
  preview = {your_graphical_abstract.png}
}
```

Omit `year` for undated manuscripts. Add the publication year, DOI, venue, and bibliographic details once confirmed. The bibliography can search by title, author, and status. Do not put an unpublished result in an accepted venue.

Work undergoing double-blind review should stay outside the published bibliography, projects, repository lists, and assets until disclosure is appropriate.

## News

Add a Markdown file under `_news/` with `layout: post`, an actual `date`, and `inline: true` in front matter. The homepage shows the five most recent items; the news page shows all. Migrated month-only announcements use the first day of their source month as a sorting value; the homepage and news page display month and year.

## Projects

Add a Markdown file under `_projects/` with `layout: page`, `title`, `description`, `importance`, and `category: research`. Optional `img` sets the card image. Link to its publication and code, and add approved diagrams or videos to its page. Additional categories go in `_pages/projects.md`.

## CV, teaching, talks, and awards

Education and positions live in `_data/cv.yml`; the CV page uses the native al-folio CV renderer. Teaching, talks, awards, and contact information live in the corresponding `_pages/*.md` files. Academic profiles live in `_data/socials.yml`.

## Navigation and future sections

Create a page in `_pages/`, with a unique `permalink`, `title`, `nav: true`, and `nav_order` to put it on the main bar. For a submenu, add its title and permalink to the `children` list in `_pages/more.md`. Current top-level pages are About, Publications, Projects, CV, Album, and More.

Search, dark mode, image zoom, reading progress, and back-to-top are controlled by `_config.yml`. To start a blog, add real posts to `_posts/` and a blog page using the upstream guide in `docs/CUSTOMIZE.md`. The demo blog and external feeds were removed during migration.

## Album: uploading photos through GitHub

The album at `/album/` discovers photos from folders under `assets/album/`. The folder name is the category, and each photo's filename becomes its caption. There is no photo list or Markdown to update for individual uploads. The homepage also shows a preview of three photos from the most recent categories. Empty categories are hidden, including `undated` when it has no photos.

1. Open [the album folders on GitHub](https://github.com/PeterWANGHK/PeterWANGHK.github.io/tree/main/assets/album).
2. Open the appropriate year folder, such as `2022`, `2023`, or `2026`.
3. Select **Add file → Upload files**, then drag your photos into the page.
4. Enter a commit message, such as `Add 2026 conference photos`, and commit to **main**.
5. Wait for **Build and deploy academic site** in the repository's **Actions** tab to finish. Refresh the album; the new images will appear automatically.

Use JPG, JPEG, PNG, WebP, GIF, HEIC, or HEIF. Both upper-case and lower-case extensions work. During deployment, HEIC/HEIF uploads are converted into browser-readable JPEG copies; the originals remain in GitHub. These generated copies are deployed but are not committed back to the repository. Use descriptive filenames such as `paris-arc-de-triomphe.jpg`; this displays as “Paris arc de triomphe.” Photos sort alphabetically by filename within each category, so prefixes such as `01-`, `02-` control their order. Images retain their full frame, and visitors can click them to zoom.

Resize large photos to roughly 1600–2400 pixels on the long edge and aim for under 2 MB each for faster loading. GitHub's browser upload limit is 25 MiB per file; see [GitHub's upload instructions](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository).

To add a new year or separate category, select **Add file → Create new file** in the repository and name it `assets/album/2027/.gitkeep` (or `assets/album/2026-travel/.gitkeep`). Commit it, then upload photos inside that new folder. Categories with photos appear automatically, with hyphens and underscores displayed as spaces. Keep photos inside a category folder, rather than directly under `assets/album/`.

Removing all photos from a category hides it on the site after the next deployment. If recent uploads do not appear, check **Actions** for a successful deployment and refresh the page with **Ctrl+F5**. The workflow checks that every supported album upload appears on the rendered album page, including HEIC/HEIF conversions.

## Appearance

`assets/css/main.scss` adds the blue accent, navigation underline transitions, quick links, image sizing, and project hover effects. It retains the base styles from `al_folio_core` 1.0.15. Motion respects the visitor's reduced-motion preference. Review this intentional override when upgrading the core gem:

```bash
bundle exec al-folio upgrade overrides diff assets/css/main.scss
bundle exec al-folio upgrade overrides accept assets/css/main.scss
bundle exec al-folio upgrade overrides audit
```
