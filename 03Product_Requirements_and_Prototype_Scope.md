# RoomLight
## 3.a) Product Requirements

| REQ-ID | Requirement Description | Type | Pri |
|--------|--------------------------|--------|------|
| 001 | When the guest enters the room for the first time, all lights are on. If arrival is late, the lighting is dimmer. | Functional | Must |
| 002 | Each season must support its own custom lighting mood. | Functional | Must |
| 003 | Lighting setting updates must be applied to all rooms at once without entering the rooms. | Functional | Must |
| 004 | Room lighting must remain consistent across all rooms of the same type. | Functional | Must |
| 005 | System must support four lighting modes (Work, Sleep, Relax, Welcome), adjustable to hotel needs. | Functional | Must |
| 006 | The system must not require additional staff training to operate. | Non-functional | Must |
| 007 | The room control panel must contain as few buttons as possible, maximum of three. | Usability | Must |
| 008 | Buttons must be physically large enough for easy operation. | Usability | Must |
| 009 | Each button must have one clearly defined function, labeled with clear text or symbols. | Usability | Must |
| 010 | All lights must be switchable off from a bedside control. | Functional | Must |
| 011 | A second bedside control panel may provide full lighting controls. | Functional | Should |
| 012 | The system must use existing lighting fixtures where possible. | Technical | Must |
| 013 | The system must provide a centralized dashboard showing device status. | Functional | Must |
| 014 | The dashboard must include room-level diagnostics. | Functional | Should |
| 015 | The system must meet electrical and fire safety requirements. | Non-functional | Must |
| 016 | The system must remain safe and operable during power outages or network failures. | Non-functional | Must |
| 017 | The device exterior must follow a Scandinavian minimal design with neutral colors and matte finishes. | Non-functional | Should |
| 018 | Glossy plastic surfaces must not be used, as they show fingerprints. | Non-functional | Should |

---

## 3.b) Prototype Scope

### 1. Prototype description
The prototype is a lightweight software version that runs on a laptop using a command line tool. It allows the user to create and modify lighting profiles and synchronize them to multiple “rooms” with a single command. The prototype is designed to convince company leadership and potential buyers that the promise “Configure once, sync everywhere” truly works in practice. It demonstrates how simple the system is to use and how it can significantly reduce time spent on maintenance and room-by-room configuration tasks.

### 2. Demonstrate (Which REQ-IDs the prototype proves and why)

**REQ 002 — Each season must support its own custom lighting mood.**  
The prototype allows creating and modifying different profiles.

**REQ 003 — Lighting setting updates must be applied to all rooms at once without entering the rooms.**  
This is the core functionality of the prototype. A single command (or later one button) synchronizes the settings to all “rooms.”

**REQ 004 — Room lighting must remain consistent across all rooms of the same type.**  
When a lighting profile is updated, all rooms receive the update.

**REQ 005 — System must support four lighting modes (Work, Sleep, Relax, Welcome).**  
The prototype includes modes (welcome, sleep) that can be adjusted and synchronized to rooms.

**REQ 006 — The system must not require additional staff training to operate.**  
The prototype works with a single command, making synchronization simple.

---

## Statement About AI Assistance
AI was used to assist in translating the product requirements from Finnish to English and in generating the final Markdown-formatted requirements table.
