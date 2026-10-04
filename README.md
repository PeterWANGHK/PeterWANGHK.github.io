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

Open `http://localhost:4000/`.

The production homepage is published from `PeterWANGHK/PeterWANGHK.github.io` at [peterwanghk.github.io](https://peterwanghk.github.io/).

To preview compatibility with the original project URL:

```bash
bundle exec jekyll serve --config _config.yml,_config.project.yml
```

Open `http://localhost:4000/peterzianwang.github.io/`.

GitHub Actions builds and validates both URL configurations on `main` and pull requests, with downloadable previews. Deployment publishes the root homepage from `main` using GitHub Pages Actions.
