# VMS Store — PostgreSQL + Cloudinary

This version uses **PostgreSQL** for all app records and **Cloudinary** for new product image uploads. Existing product images stored as local filenames will still need migration to Cloudinary.

## Setup in VS Code (PowerShell)

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` with your real Neon PostgreSQL `DATABASE_URL`, Cloudinary `CLOUDINARY_URL`, strong `SECRET_KEY`, and admin credentials. **Never commit `.env`.**

```powershell
python app.py
```

Open http://127.0.0.1:5000. First startup creates PostgreSQL tables and demo products. Admin is created only when the users table is empty and `ADMIN_USERNAME` and `ADMIN_PASSWORD` are set. If users already exist, create an admin through a secure manual procedure.

### Cloudinary

Create a Cloudinary account and copy the `CLOUDINARY_URL` credentials from your dashboard. Admin → Products → Add/Edit → Upload image. New images are uploaded to Cloudinary, and the resulting HTTPS URL is stored in PostgreSQL.

### Existing SQLite data

The bundled SQLite database is **not automatically imported**. To keep existing customers, products and orders, run a reviewed SQLite-to-PostgreSQL migration before using this version in production. Existing local images also need separate upload and URL updates. Avoid exposing test admin passwords or real credentials in GitHub.

### Production notes

Use HTTPS and an appropriately secured hosting platform; configure PostgreSQL SSL; use `gunicorn app:app` on Linux. Change passwords, implement CSRF protection and secure cookies, and test order/stock consistency before accepting real payments. PostgreSQL and Cloudinary are persistent hosted services, subject to account and service retention.
