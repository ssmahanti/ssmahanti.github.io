# Sankha Subhra Mahanti’s website

Personal academic website for GitHub Pages, built with static HTML, Bootstrap 3, and jQuery. No build step is required.

## Editing

- `index.html`: biography, education, and news.
- `projects.html`: research projects.
- `publication.html`: publications and presentations.
- `outreach.html`: talks and videos.
- `vitae.html`: CV viewer and download link. Update both PDF references when replacing the CV.
- `navbar.html` and `footer.html`: shared navigation and footer, loaded by `js/main.js`.
- `css/main.css`: shared styling.

The `extra/` directory preserves an older research page and is excluded from publication by `_config.yml`. Unused personal images are retained for future use.

## Preview and checks

From this directory, run `python3 -m http.server 8000`, then open `http://localhost:8000`. Use an HTTP server so navigation and footer fragments can load.

Run `python3 scripts/check_site.py` and `git diff --check` before committing. Check all five pages at desktop and mobile widths, including the mobile menu, active navigation, back-to-top link, CV, and embedded videos. Third-party styles, scripts, fonts, and videos require an internet connection.

## Credits

Originally adapted from Randal Sean Harrison’s [academic website template](https://github.com/randal-sean-harrison/academic-website-template-bs3). Original design credits are retained in `humans.txt`; respect the original template’s license when reusing it.
