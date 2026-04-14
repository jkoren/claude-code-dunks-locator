# 🍩 Dunkin' Donuts Remote Work Locator

An interactive map application showcasing 45 Dunkin' Donuts locations scouted for remote work, complete with WiFi speed ratings and location details.

## Features

✨ **Interactive Map**

- OpenStreetMap-based interactive map with zoom and pan
- Marker clustering for area overview
- Color-coded markers by WiFi speed

🔍 **Search & Filter**

- Search locations by name, address, or notes
- Filter by minimum WiFi speed (0-100 Mbps)
- Real-time statistics

📊 **Location Details**

- WiFi speed ratings displayed in parentheses (e.g., "Dunks 65 JFK (39)" = 39 Mbps)
- Address information
- Notes about seating, amenities, and atmosphere
- Image count for each location
- Side-by-side sidebar with all locations

🎨 **Visual Design**

- Responsive design (desktop and mobile optimized)
- Dunkin' Donuts brand color scheme (orange/brown)
- Smooth animations and transitions
- Dark scrollbars for better aesthetics

## WiFi Speed Classification

- 🟢 **Excellent**: 60+ Mbps
- 🟡 **Good**: 30-59 Mbps
- 🔴 **Poor**: 0-29 Mbps
- ⚫ **No Data**: WiFi speed not recorded

## Quick Start

### Option 1: Using Python (Recommended)

```bash
cd /path/to/claude-code-dunks-locator
python3 server.py
```

Then open **http://localhost:8000** in your browser

### Option 2: Using Node.js

```bash
cd /path/to/claude-code-dunks-locator
npx http-server -p 8000 -o
```

### Option 3: Open directly

Simply open `index.html` in your browser (limited functionality)

## Files

- **index.html** - Main application interface
- **locations.json** - Extracted location data from XML
- **server.py** - Simple Python HTTP server
- **Remote work DD-jpg.xml** - Original data with HEIC image references
- **Remote work DD-heic.xml** - Original data (HEIC format)

## Data Source

This app displays data from scouted Dunkin' Donuts locations across the Massachusetts area, with WiFi quality ratings for remote work productivity.

## Technologies Used

- **Leaflet.js** - Interactive mapping
- **Leaflet MarkerCluster** - Intelligent marker clustering
- **Bootstrap 5** - Responsive UI components
- **Font Awesome** - Icons
- **OpenStreetMap** - Map tiles
- Vanilla JavaScript - No frameworks required

## Filters & Features

**Search**: Find locations by name, address, or notes
**WiFi Filter**: Use the slider to show only locations meeting your speed requirements
**Map Interactions**:

- Click markers to see details
- Click locations in sidebar to jump to that spot
- Use mouse to zoom/pan
- Double-click to zoom in

**Statistics**: View total locations, filtered count, and average WiFi speed

---

Made with ☕ and 📍 for remote workers
