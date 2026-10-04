# Zian Wang (Peter)'s academic website

An al-folio v1 site migrated from the original academic homepage. The site uses versioned al-folio gems, Markdown content, and BibTeX publication records.

Start with [CONTENT_GUIDE.md](CONTENT_GUIDE.md) to add papers, graphical abstracts, projects, news, or navigation items. See [MIGRATION.md](MIGRATION.md) for migration decisions, validation, and the clean homepage URL.

## Preview locally

Use Ruby 3.3.5 and Node 22:

```bash
bundle install
npm ci
bundle exec jekyll serve
```

Open `http://localhost:4000/peterzianwang.github.io/`.

To preview the account homepage instead:

```bash
bundle exec jekyll serve --config _config.yml,_config.root.yml
```

Open `http://localhost:4000/`.

GitHub Actions builds and validates both configurations on the migration branch and pull requests, with downloadable previews. Deployment runs on `main` after GitHub Pages is configured to use GitHub Actions.
