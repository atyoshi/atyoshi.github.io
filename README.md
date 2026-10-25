# Albert Yoshimoto

Personal research and music portfolio: https://atyoshi.github.io

M.S. in Artificial Intelligence student at the University of Texas at El Paso, expected May 2027. Graduate GPA: 4.0. Violin performer and teacher; B.M. in Instrumental Performance, NMSU (May 2023).

## Content

- `_pages/about.md`: homepage and featured work
- `_pages/projects.md`: ModelScope, SpecGuard, Blue Cheese, LLM uncertainty research, and evacuation simulation
- `_pages/teaching.md`: music section
- `_pages/cv.md`, `_data/cv.yml`, `assets/json/resume.json`: résumé and structured data
- `assets/pdf/albert-yoshimoto-resume.pdf`: current one-page downloadable résumé

Project descriptions distinguish implemented work from ongoing development and planned evaluation. No unpublished performance results are claimed.

## Local development

Use Ruby 3.3.5 and Bundler, matching `.github/workflows/deploy.yml`.

```sh
bundle install
bundle exec jekyll serve
```

`bundle install` installs the locked Ruby dependencies. `bundle exec jekyll serve` builds the site and serves it locally for review.

Before publication, run `JEKYLL_ENV=production bundle exec jekyll build` to build with production settings, check homepage, projects, résumé, and music on desktop and mobile, and verify the PDF download.

## Publishing

Continue changes on `portfolio-cleanup-2026-10` and open a pull request into `main`. The Deploy site workflow builds pull requests without publishing. Merging into `main` triggers the production build and publishes `_site` to `gh-pages`. Confirm both the Actions result and the live site.

## Contact

ayoshimoto@miners.utep.edu · (915) 731-4379

Built with Jekyll and the MIT-licensed [al-folio theme](https://github.com/alshedivat/al-folio). See LICENSE.
