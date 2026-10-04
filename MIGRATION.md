# Migration to al-folio v1

## Source and destination

- Original: `PeterWANGHK/peterzianwang.github.io`, commit `0cf2d52d4fa91fc5e5f3032186442f06fdeeefe1`.
- Starter: `alshedivat/al-folio`, commit `40c06007dab344970b681ba63b2241b1a8209ec1`.
- Runtime: `al_folio_core` 1.0.15 and the starter's pinned plugin set.
- Migration work is on a separate branch. The original default branch remains available during review.

## Content transfer

Biography, research timeline, academic profiles, six news items, eight publication records, education, positions, teaching and mentorship, invited talks, presentations, and nine awards were transferred. Publications retain their authorship markers and stated acceptance or review statuses. Selected publications show existing method figures for DREAM, DRIFT, and MAVCO, plus the supplied SAFE-AD graphical abstract. SAFE-AD is listed as under revision at Communications in Transportation Research and links to its public code. The displayed journal impact factors (TR-C 8.4; COMMTR 12.7) were provided by the site owner on 2026-10-04.

The original page and configuration are archived under `docs/migration/` for comparison. The old theme's layouts, includes, Sass, fonts, JavaScript, citation crawler, and redundant demo assets were replaced by al-folio's gem-managed runtime. The citation-counter integration is not carried over; the Google Scholar profile remains linked.

## Source issues retained for review

- The original HKU-SAIL URL, `https://hku-.hku.hk/`, appears malformed. The biography now links to the group's existing `https://github.com/SAS-HKU` organization.
- The original SAFE-AD repository URL returned 404. It has been replaced with the verified public repository `https://github.com/SAS-HKU/SAFE-AD`; the original URL remains in the archived source.
- The original teaching repository links are preserved. They may require access or later correction.
- Month-only news dates use day 01 to provide a stable sort. Site-owned page content displays only the source month and year, so no exact announcement day is claimed.
- The original DRIFT September presentation is still described as scheduled, because the source did not confirm its completion. Update that status when appropriate.
- Undated manuscripts have no invented publication year, DOI, abstract, or venue.
- Current previews are method figures, not newly designed or publisher-approved graphical abstracts. Add approved replacement artwork via each record's `preview` field.

## Local override

Only `assets/css/main.scss` shadows a core runtime asset. It retains the exact published gem's imports and adds site appearance rules. `.al-folio-overrides.yml` records the original gem file and local file checksums. No local layouts, includes, or Sass partials are copied from the old theme.

## Clean URL

GitHub's account homepage convention is a repository named `PeterWANGHK.github.io`, published at `https://peterwanghk.github.io/`. This removes the repeated repository path. The account homepage repository did not exist when checked on 2026-10-04. See [GitHub Pages site types](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#types-of-github-pages-sites).

The migration includes `_config.root.yml` with an empty baseurl and builds both URL variants in CI. For the clean homepage, create a separate account homepage repository using this prepared source and change `_config.yml` to `baseurl: ""`. The workflow automatically validates the configured baseurl. Set its Pages source to GitHub Actions. Keep the old project site available until the new homepage is verified; then replace it with a redirect to preserve old incoming links.

For deployment at the current project address, set the existing repository's Pages source to GitHub Actions before merging the migration. Otherwise GitHub's legacy builder cannot load the al-folio gem plugins.

## Validation

```bash
npm ci
npm run lint:prettier
npm run lint:style-contract
bundle exec al-folio upgrade audit --no-fail
bundle exec al-folio upgrade overrides audit
JEKYLL_ENV=production bundle exec jekyll build
python bin/check_site.py _site /peterzianwang.github.io
JEKYLL_ENV=production bundle exec jekyll build --config _config.yml,_config.root.yml --destination _site_root
python bin/check_site.py _site_root ""
```

The rendered checks verify ten routes, all eight publication records, four previews, status labels, and all generated local links and assets in both configurations. GitHub Actions also provides downloadable built previews for visual inspection. Demo fixture tests under `test/` remain upstream reference material; their Einstein/demo-content expectations are not migration acceptance tests.
