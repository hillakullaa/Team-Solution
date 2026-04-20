from models import (
    Room,
    RoomType,
    LightingProfile,
    Mode,
    SeasonalSettings,
)


def seed_room_types():
    return {
        "standard": RoomType("standard"),
        "deluxe": RoomType("deluxe"),
        "suite": RoomType("suite"),
    }


def seed_profiles():
    return {
        "Work": LightingProfile("Work", Mode.WORK, 80, 4500),
        "Relax": LightingProfile("Relax", Mode.RELAX, 40, 3000),
        "Sleep": LightingProfile("Sleep", Mode.SLEEP, 0, 0),
        "Welcome": LightingProfile("Welcome", Mode.WELCOME, 60, 3500),
    }


def seed_rooms(room_types):
    return [
        Room(101, room_types["standard"]),
        Room(102, room_types["standard"]),
        Room(201, room_types["deluxe"]),
        Room(301, room_types["suite"]),
    ]


def seed_seasonal_settings():
    return SeasonalSettings()
