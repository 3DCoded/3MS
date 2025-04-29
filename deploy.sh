#!/bin/bash
git add .
git commit -m "chore: Update documentation"
mkdocs gh-deploy
git stash
git checkout gh-pages
echo "3ms.3dcoded.xyz" > CNAME
git add .
git commit -m "Add CNAME"
git push origin gh-pages
git stash
git checkout docs
git add .
git commit -m "chore: Deploy documentation"
git push origin docs