from enum import Enum
from datetime import datetime


# ---------- MODES ----------

class Mode(Enum):
    WORK = "Work"
    RELAX = "Relax"
    SLEEP = "Sleep"
    WELCOME = "Welcome"


# ---------- SEASONAL PROFILES ----------

class SeasonalProfile:
    def __init__(self, season, brightness_factor=1.0, color_temp_factor=1.0):
        self.season = season
        self.brightness_factor = brightness_factor
        self.color_temp_factor = color_temp_factor


class SeasonalSettings:
    def __init__(self):
        self.profiles = {
            "Spring": SeasonalProfile("Spring", 1.0, 1.0),
            "Summer": SeasonalProfile("Summer", 0.85, 1.05),
            "Autumn": SeasonalProfile("Autumn", 1.0, 1.0),
            "Winter": SeasonalProfile("Winter", 1.15, 0.95),
        }
        self.active_season = "Winter"

    def get_active_profile(self):
        return self.profiles[self.active_season]


# ---------- LIGHTING PROFILES ----------

class LightingProfile:
    def __init__(self, name, mode, base_brightness, base_color_temperature):
        self.name = name
        self.mode = mode
        self.base_brightness = base_brightness
        self.base_color_temperature = base_color_temperature


# ---------- ROOM TYPES ----------

class RoomType:
    def __init__(self, type_name):
        self.type_name = type_name


# ---------- ROOMS ----------

class Room:
    def __init__(self, room_id, room_type):
        self.room_id = room_id
        self.room_type = room_type

        # Synced state (snapshot)
        self.profile_name = None
        self.brightness = None
        self.color_temperature = None
        self.season = None
        self.synced_at = None

    def apply_lighting(self, profile_name, brightness, color_temperature, season):
        self.profile_name = profile_name
        self.brightness = brightness
        self.color_temperature = color_temperature
        self.season = season
        self.synced_at = datetime.now()
