Environment Variables needed to be set is in `.env.template`.
Copy the mentioned environment variables inside `env.template` into a separate `.env` to successfully run the program.

# Steps

Preferable if you use tmux, or Windows Terminal so that you can run two terminals at the same time

- Create your first terminal, and run `docker compose up`
- Create your second terminal, and run `docker compose exec python manage.py migrate`
  (if this doesnt work you can try running `docker compose exec python manage.py makemigrations sitecat`, but it should work hopefully)

- Then you can freely go through `localhost:8000/polls` and use the web app!
