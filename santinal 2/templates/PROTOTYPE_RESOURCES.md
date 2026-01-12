# Sentinal2 Prototype Resources

This document outlines the core technologies, libraries, and features implemented in this prototype.

## 🚀 Core Tech Stack
- **Backend Framework**: [Flask](https://flask.palletsprojects.com/) (Python 3.x)
- **Frontend Layer**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Custom CSS with **Glassmorphism** design patterns and **Dark Mode** support.

## 🗺️ Geospatial & Mapping
- **Map Engine**: [Leaflet.js](https://leafletjs.com/)
- **Tile Provider**: [OpenStreetMap](https://www.openstreetmap.org/)
- **Geocoding API**: [Nominatim (OSM)](https://nominatim.org/) for address search and reverse geocoding.

## 📊 Data Visualization
- **Charts**: [Chart.js](https://www.chartjs.org/) for displaying NDVI vegetation trends and market data.

## 🛠️ Key Features & Logic
- **NDVI Simulator**: A Python-based mocked logic in `app.py` for calculating vegetation changes.
- **Interactive Map**: Drag-and-drop markers with automatic radius calculation and English reverse geocoding on click.
- **English Search Engine**: Location searches are powered by **Nominatim** (OSM), results are forced to **English**, and searches are triggered explicitly by the **Enter** key for a clean, non-intrusive experience.
- **Carbon Credit Calculator**: A client-side tool to estimate potential carbon offsets based on tree species and age.
- **Theme Engine**: A robust dark/light mode toggle with persistence using `localStorage`.
- **Responsive Navigation**: A modern hamburger menu for mobile and desktop fluidity.

## 📂 Project Structure
- `app.py`: Main Flask application and backend logic.
- `templates/`: HTML structures using Jinja2 templating.
- `static/`:
    - `styleapp.css`: Premium UI components and layout.
    - `theme-toggle.js`: Theme switching logic.
    - Component-specific CSS (e.g., `calculator.css`, `history.css`).
