# D8Acapture API Tools

This is a set of Python utilities for interacting with the [D8Acapture](https://d8acapture.com) API.

These scripts are designed for engineers, integrators, and technical users who need to programmatically:
- Authenticate via the API
- Create projects and poles
- Import/export pole metadata
- Automate data population using dynamic form structures

⚠️ **Disclaimer:** This repository is provided by D8Averse and is not part of the D8Acapture platform source code. It offers standalone tools for interacting with the public D8Acapture API.

---

## ⚙️ Requirements

- Python 3.7+
- `pip install -r requirements.txt`

Required Python packages:
```
python-dotenv
requests
```

---

## 📁 Project Structure

```
d8a_client/
├── api.py             # Main API client (projects, poles, forms)
├── auth.py            # Login handler
├── config.py          # Loads credentials from .env
├── form_utils.py      # Builds structured form update payloads

scripts/
├── create_project_add_poles.py  # Creates project and loads poles from JSON
├── export_poles.py              # Exports poles from an existing project
├── list_my_company_id.py        # Lists accessible companies (for .env setup)
├── run_fake_projects.py         # Loads fake projects from JSON

*.json                  # Example input files (e.g., poles or projects)
```

---

## 🔐 .env Example

Create a `.env` file in the project root with the following:

```env
EMAIL=you@example.com
PASSWORD=your-password
X_COMPANY=your-company-uuid
```

To discover your company ID, run:
```bash
python scripts/list_my_company_id.py
```

---

## 🚀 Usage

### 1. Export Poles from an Existing Project
```bash
python scripts/export_poles.py
```
> 📄 Requires editing the hardcoded project ID in the script.

### 2. Create a New Project & Import Poles
```bash
python scripts/create_project_add_poles.py
```
> 📄 Make sure `example_poles.json` is populated with `name`, `lat`, and `lng`.

### 3. Run Example Fake Projects (Dev/Testing)
```bash
python scripts/run_fake_projects.py
```

---

## 📥 Example JSON Format

### Poles Input (`example_poles.json`)
```json
[
  {
    "name": "Pole 101",
    "lat": 33.719201,
    "lng": -78.927865
  },
  {
    "name": "Pole 102",
    "lat": 33.720301,
    "lng": -78.928100
  }
]
```

---

## 🧠 Notes

- All pole updates use a form-aware payload builder from `form_utils.py`
- Forms are referenced by name and resolved to ID via the API
- Form structure is only fetched once per batch job for efficiency

---

## 🛡 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
