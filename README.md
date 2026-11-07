# PHIDS
### Portable Hunting Intelligence & Data System

**Developed by Metz Forge**

**A Python-based wildlife intelligence and hunting management platform.**

PHIDS is a personal software development project designed to combine wildlife observation, data analytics, database management, and cybersecurity principles into a centralized hunting intelligence platform.

The goal is to help hunters organize wildlife sightings, analyze movement patterns, monitor environmental conditions, and make informed decisions using historical data.

---

## Project Status

**Phase 1 — Initial Development**

PHIDS is currently in the early development stage. The initial Python application, SQLite database functionality, and graphical startup screen have been implemented.

### Completed Features

- Python application foundation.
- SQLite database creation and connection.
- Wildlife sightings table with structured records.
- Wildlife sighting insertion and retrieval.
- Basic duplicate-checking functionality.
- Parameterized SQL queries.
- Graphical startup screen using Tkinter.
- Custom deer skull branding.
- Git version control and GitHub repository integration.
- Git configuration to exclude local wildlife databases.

### Initial Test Case: Bradleytown Bruiser

The first wildlife observation used to test PHIDS is a mature white-tailed buck nicknamed **Bradleytown Bruiser**.

The observation was recorded on November 7, 2026, in Venango County, Pennsylvania.

This initial record demonstrates the ability to create, store, and retrieve wildlife sightings using SQLite.

The nickname is an observation label and does not establish that future sightings represent the same animal.

For privacy, local database files and detailed hunting-location records are excluded from GitHub.

---

## Technologies

| Technology | Application |
|---|---|
| Python | Application development |
| SQLite | Wildlife database |
| SQL | Database creation, insertion, and retrieval |
| Tkinter | Graphical user interface |
| Git | Version control |
| GitHub | Source code management |
| VS Code | Development environment |

---

## Planned Development

### Phase 2 — Wildlife Observation Database

- Expand the SQLite database to support multiple observation categories.
- Record deer, coyotes, bears, turkeys, and other wildlife.
- Record rubs, scrapes, tracks, scat, bedding areas, food sources, water sources, and game trails.
- Record hunter activity and hunting pressure observations.
- Automatically capture GPS coordinates when available.
- Distinguish confirmed wildlife sightings from discovered evidence.
- Separate observation timestamps from estimated animal activity dates.
- Track observation confidence and location accuracy.
- Add, edit, delete, search, and filter observations.
- Preserve historical observations and existing database records.

### Phase 3 — PHIDS Mobile Field Recorder

- Develop an iPhone-compatible field recording interface.
- Create a PHIDS home-screen shortcut.
- Automatically capture GPS coordinates, date, and time.
- Support quick selection of observation categories.
- Allow photographs and field notes.
- Develop secure synchronization with the PHIDS database.
- Support offline observation recording and later synchronization.
- Develop a mobile-friendly interface using Progressive Web App technology.

### Phase 4 — Trail Camera Intelligence

- Register trail cameras with geographic coordinates.
- Support Tactacam REVEAL, Stealth Cam, and additional manufacturers.
- Import trail camera photographs and available metadata.
- Associate photographs with camera locations and capture timestamps.
- Support camera clock corrections and relocation history.
- Retrieve historical weather corresponding to photograph timestamps.
- Group related photographs into wildlife detection events.
- Investigate automated wildlife identification using computer vision.
- Identify potentially empty triggers and monitor camera performance.
- Investigate supported methods for automatic cellular camera synchronization.

### Phase 5 — Environmental Intelligence

- Integrate current and historical weather information.
- Record temperature, wind speed, wind direction, humidity, precipitation, and barometric pressure.
- Incorporate sunrise, sunset, moon phase, and elevation data.
- Track changes in environmental conditions over time.
- Distinguish discovery weather from conditions associated with confirmed wildlife activity.
- Compare wildlife observations against historical environmental conditions.
- Develop configurable alerts for significant weather changes.

### Phase 6 — Geographic Wildlife Intelligence

- Develop interactive maps for Windows and mobile devices.
- Display satellite imagery and topographic information.
- Integrate available public hunting land boundaries.
- Support Pennsylvania, New York, and additional hunting locations.
- Organize observations by property and hunting area.
- Display different map symbols for wildlife, deer sign, habitat, equipment, and hunter activity.
- Support geographic points, trails, and defined areas.
- Develop geographic filters and historical activity visualizations.
- Protect sensitive hunting locations and private property information.

### Phase 7 — Hunting Intelligence

- Develop a dedicated Hunting tab.
- Support hunting modes for deer, coyotes, turkey, bear, and other species.
- Record complete hunting sessions, including unsuccessful hunts.
- Compare current conditions with historical wildlife observations.
- Develop a historical timeline and Rewind feature.
- Analyze potential relationships between hunting pressure and wildlife movement.
- Develop wildlife activity heat maps.
- Provide evidence-based observations with confidence indicators.
- Develop configurable hunting condition notifications.
- Support historical analysis without presenting correlations as guaranteed predictions.

### Phase 8 — Security, Reliability, and Advanced Analytics

- Implement user authentication and access controls.
- Develop a secure Python API for mobile and desktop synchronization.
- Protect sensitive geographic information.
- Implement database backup and recovery.
- Develop data validation and duplicate detection.
- Expand wildlife movement and environmental analytics.
- Evaluate database scalability as observation volume increases.
- Develop secure deployment options using private network connectivity.
- Continue improving application reliability and performance.

### Long-Term Development

- Automated trail camera data ingestion where supported.
- Advanced wildlife image classification.
- Potential individual-animal identification with confidence tracking.
- Historical movement pattern analysis.
- Improved offline mapping and field navigation.
- Cross-platform access through Windows and iPhone.
- Additional hunting and equipment management capabilities.

---

## PHIDS Branding

The PHIDS graphical startup screen features a custom deer skull design.

A future animated startup sequence is planned in which a realistic white-tailed buck's head gradually transforms from flesh into a clean European skull mount as the application initializes.

The finished skull will match the PHIDS branding artwork.

---

## Development Objectives

PHIDS serves as both a personal hunting management project and a practical environment for developing technical skills in:

- Python programming
- Relational database design
- SQL queries
- Data analytics
- Application development
- Secure software development
- Version control
- Technical documentation

The project is being developed incrementally, with functionality tested before additional features are introduced.

---

## Current Limitations

PHIDS is an early-stage prototype.

The SQLite functionality currently operates through a Python script. The graphical startup screen is a separate prototype and is not yet connected to the wildlife database.

The application does not currently provide a complete graphical interface for managing wildlife observations.

Planned capabilities are documented separately from implemented functionality.

---

## Development Philosophy

**Build. Test. Understand. Improve.**

PHIDS is intended to grow through practical development, testing, and continuous learning.

---

## Development

**Metz Forge**

PHIDS is an independent software development project
created under Metz Forge.

The project combines practical Python programming,
database management, data analytics, and secure
software development with real-world hunting applications.