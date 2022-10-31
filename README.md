echo "# TestOne" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Georgy-Chachava/TestOne.git
git push -u origin main
git config user.name "Georgy Chachava"
git config user.email ga.chachava@mail.ru
