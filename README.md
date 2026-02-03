# Simple Feedback Collector

A minimal feedback collector using Django (Frontend) and Node.js (Backend).

## Files
- `server.js`: Node.js backend (Port 3000)
- `manage.py`: Django entry point
- `feedback_project/`: Django settings
- `feedback_app/`: Django app (views, URLs, templates)

## How to Run

1. **Start Node.js Backend**
   Open a terminal:
   ```bash
   node server.js
   ```

2. **Start Django Frontend**
   Open another terminal:
   ```bash
   python manage.py runserver
   ```

3. **Use the App**
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.
