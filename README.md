# expatrimo.com

Static website for expatrimo.com. Articles are Markdown files, and the site is rebuilt automatically on every change.

```
content/actualites/   one .md file per article (URL = /actualites/<file name>/)
static/               files copied as-is: images (wp-content/uploads), CSS/JS (assets), editor (admin)
src/build.py          builds the site into public/ (Python 3, no packages needed)
src/pages.py          text of the fixed pages (home, about, contact, guides…)
vercel.json           build settings and redirects for Vercel
api/                  GitHub login for the editor (Vercel functions)
```

## Adding an article without Claude: expatrimo.com/admin

Once the setup below is done:

1. Go to **https://expatrimo.com/admin** and click **Login with GitHub**.
2. Click **Actualités** and then **Nouveau Article**.
3. Fill in the title, date and categories, then add a main image (upload it from your computer) and write the text.
   You can add images inside the text with the **+** button.
4. Click **Publier → Publier maintenant**. The article is online about a minute later at `expatrimo.com/actualites/<title>/`.

Tick **Brouillon** to save an article without publishing it. You can edit or delete existing articles in the same way.

## One-time setup on Vercel (about 20 minutes)

The editor saves each article into the GitHub repository, and Vercel rebuilds the site from it.
So the site must be deployed **from GitHub**, not uploaded as a zip.

1. **GitHub**: create a repository (it can be private), for example `expatrimo-site`, and put the contents of this folder in it
   (on github.com: *Add file → Upload files*, drag the folders in, *Commit*).
   Claude can push it for you once GitHub is connected and you tell it the repository name.
2. **Vercel**: *Add New → Project → Import Git Repository* and pick the repository.
   Leave *Framework Preset* on *Other*; the build settings are read from `vercel.json`. Click *Deploy*.
3. **Domain**: in the Vercel project, *Settings → Domains → Add* `expatrimo.com` and follow the DNS instructions at your registrar.
4. **Editor login**:
   - On GitHub: *Settings → Developer settings → OAuth Apps → New OAuth App*.
     Homepage URL `https://expatrimo.com`, Authorization callback URL `https://expatrimo.com/api/callback/`.
     Copy the *Client ID* and generate a *Client secret*.
   - On Vercel: *Project → Settings → Environment Variables*, add `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET`
     with those two values, then *Deployments → Redeploy*.
5. `static/admin/config.yml` already points to `mayuguo/expatrimo`.

Anyone who should be able to publish needs a GitHub account with write access to the repository.
Editor login is configured on Vercel (GITHUB_CLIENT_ID / GITHUB_CLIENT_SECRET set on 12 Oct 2026).

## Building locally (optional)

    python3 src/build.py          # creates public/
    python3 -m http.server -d public
