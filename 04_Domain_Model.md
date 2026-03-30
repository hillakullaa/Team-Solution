# Prototype Domain

Because this is the domain of a prototype, only the concepts related to profiles and synchronization are included.

The prototype demonstrates that:
- profiles can be created
- profiles can be edited
- profiles can be stored
- profiles have a mode (sleep, work, relax, welcome)
- profiles can include seasonal versions (spring, summer, autumn, winter)

Additionally, the prototype:
- simulates rooms
- updates a single profile to all rooms at once, when needed by room type
- does not include any physical hardware

Therefore, the essential concepts from the prototype’s perspective are:
- Room
- RoomType
- LightingProfile
- SeasonalProfile
- Mode
- SyncService

# Domain Model

## 1. LightingProfile
A profile that defines the settings of a specific lighting state. Includes parameters such as brightness, color temperature, and mode.

**Attributes:**
- name (Sleep, Work, Relax, Welcome, Custom)
- brightness
- colorTemperature
- season (optional)

## 2. SeasonalProfile
A season based base lighting profile. Provides default values for different lighting modes depending on the time of year (e.g., brighter in winter).

**Attributes:**
- season (Summer, Winter, Autumn, Spring)
- baseBrightness
- baseColorTemperature

## 3. Mode
The purpose or ambiance of the lighting.

**Attributes:**
- name (Work, Sleep, Relax, Welcome)

## 4. Room
Simulates a hotel room to which lighting profiles are synchronized. A room has a room type and one lighting profile at a time.

**Attributes:**
- roomId
- roomType
- activeProfile (LightingProfile)

## 5. RoomType
A room type describes what kinds of rooms the hotel has, e.g., Standard, Deluxe, Suite.  
Room types allow rooms to be grouped so that the same lighting settings can easily be synchronized to all rooms of the same type.  
RoomType acts as a classification that helps target synchronization to the correct rooms.

**Attributes:**
- typeName (Standard, Deluxe, Suite)

## 6. SyncService
A service that updates lighting profiles to rooms with a single command. Implements the prototype’s key promise: “configure once, sync everywhere”.

**Operations:**
- syncAllRooms(profile)
- syncRoomsByType(roomType)

# Domain Relationships

- SeasonalProfile 1:N LightingProfile
- LightingProfile 1:N Room  
  Many rooms can use the same profile.
- Room 1:1 LightingProfile  
  A room always has one active profile.
- Room N:1 RoomType
- SyncService → (LightingProfile, Room)
- Mode 1:1 LightingProfile

# Statement About AI Assistance
AI was used to assist in translating the product requirements from Finnish to English and in generating the final Markdown-formatted requirements table.
Additionally, AI helped refine and filter the domain concepts to include only those essential for the prototype, ensuring that the domain model focuses strictly on profiles and synchronization features as required by the prototype scope.
