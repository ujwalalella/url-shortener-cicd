# URL Shortener

A simple URL shortener REST API built with **Python** and **Flask**.

The application accepts a long URL and generates a short code for it.

## Features

* Create a shortened URL using `POST /shorten`
* Health check using `GET /health`
* Random 6-character short codes
* URL validation
* In-memory URL storage

> **Note:** URL mappings are stored in memory and are lost when the application stops. This is intentional for this learning project.

---

## Project Structure

```text
url-shortener/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .venv/
```

The `.venv/` directory is used only for local development and is excluded from Git.

---

## Requirements

* Python 3.x
* Flask

---

## Running the Application Locally

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

On Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

The application will run on:

```text
http://localhost:5000
```

---

## API Endpoints

### Create a Short URL

**Endpoint:**

```text
POST /shorten
```

**Request:**

```json
{
  "url": "https://www.example.com/some/very/long/url"
}
```

**Example response:**

```json
{
  "short_code": "aB72xK",
  "short_url": "http://localhost:5000/aB72xK",
  "original_url": "https://www.example.com/some/very/long/url"
}
```

The generated `short_code` will be different for each request.

---

### Health Check

**Endpoint:**

```text
GET /health
```

**Example response:**

```json
{
  "status": "healthy"
}
```

This endpoint will later be useful for verifying that the deployed application is running correctly.

---

## Example Request

Using PowerShell:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:5000/shorten `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"url":"https://www.example.com/some/very/long/url"}'
```

---

## How It Works

```text
Client
   │
   │ POST /shorten
   │
   │ { "url": "https://example.com/..." }
   ▼
Flask Application
   │
   ├── Validate URL
   │
   ├── Generate short code
   │
   ├── Store URL mapping
   │
   └── Return JSON response
   ▼
Client
```

The application stores mappings in memory:

```text
short code → original URL
```

For example:

```text
aB72xK → https://www.example.com/some/very/long/url
```

---

## CI/CD

This project will eventually be used to demonstrate a complete CI/CD pipeline using:

* GitHub
* GitHub Actions
* Self-hosted GitHub Actions runner
* Azure VM
* Podman/containerization
* Automated build and deployment

The planned flow is:

```text
Developer
    ↓
GitHub Repository
    ↓
GitHub Actions
    ↓
Self-hosted Runner
    ↓
Build / Package
    ↓
Container Image
    ↓
Deploy
    ↓
Running Application
```

The Azure VM will act as the self-hosted GitHub Actions runner and will eventually be used to deploy the application.

---

## Current Scope

This project intentionally keeps the application simple.

It does **not** currently include:

* Database
* User authentication
* URL expiration
* Analytics
* Automated application tests
* Persistent URL storage

These can be added later if the project needs to be expanded.
