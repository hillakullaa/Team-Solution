from services import SyncService
from data import (
    seed_room_types,
    seed_profiles,
    seed_rooms,
    seed_seasonal_settings,
)


# ---------- MAIN LOOP ----------

def run_cli():
    room_types = seed_room_types()
    profiles = seed_profiles()
    rooms = seed_rooms(room_types)
    seasonal_settings = seed_seasonal_settings()

    sync_service = SyncService(rooms, seasonal_settings)

    while True:
        choice = main_menu()

        if choice == "1":
            lighting_profiles_menu_loop(
                profiles, seasonal_settings, sync_service
            )

        elif choice == "2":
            rooms_menu_loop(rooms)

        elif choice == "3":
            sync_menu_loop(sync_service, profiles)

        elif choice == "0":
            print("Exiting application.")
            break

        else:
            print("Invalid selection.")


# ---------- MAIN MENU ----------

def main_menu():
    print("\nMAIN MENU")
    print("1 - Lighting Profiles")
    print("2 - Rooms")
    print("3 - Sync")
    print("0 - Exit")
    return input("Select option: ")


# ---------- LIGHTING PROFILES ----------

def lighting_profiles_menu_loop(profiles, seasonal_settings, sync_service):
    while True:
        print("\nLIGHTING PROFILES")
        print("1 - Edit Profile")
        print("2 - Seasonal Settings")
        print("3 - Sync now")
        print("0 - Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            edit_profile_menu(profiles)

        elif choice == "2":
            seasonal_menu_loop(seasonal_settings)

        elif choice == "3":
            sync_from_profiles(sync_service, profiles)

        elif choice == "0":
            return

        else:
            print("Invalid selection.")


def edit_profile_menu(profiles):
    profile = select_profile(profiles)
    if not profile:
        return

    while True:
        print(f"\nEditing Profile: {profile.name}")
        print(f"Brightness: {profile.base_brightness}")
        print(f"Color temperature: {profile.base_color_temperature}")

        print("1 - Edit brightness")
        print("2 - Edit color temperature")
        print("0 - Back")

        choice = input("Select option: ")

        if choice == "1":
            profile.base_brightness = ask_int(
                "New brightness (0–100): ", 0, 100
            )

        elif choice == "2":
            profile.base_color_temperature = ask_int(
                "New color temperature (K): ", 1500, 6500
            )

        elif choice == "0":
            return

        else:
            print("Invalid selection.")


# ---------- SEASONAL SETTINGS ----------

def seasonal_menu_loop(seasonal_settings):
    while True:
        print("\nSEASONAL SETTINGS")
        print(f"Active season: {seasonal_settings.active_season}\n")

        seasons = list(seasonal_settings.profiles.keys())

        for i, season in enumerate(seasons, start=1):
            profile = seasonal_settings.profiles[season]
            print(
                f"{i} - {season} "
                f"(B:{round(profile.brightness_factor*100)}%, "
                f"CT:{round(profile.color_temp_factor*100)}%)"
            )

        print("5 - Change active season")
        print("0 - Back")

        choice = input("Select option: ")

        if choice in ["1", "2", "3", "4"]:
            season = seasons[int(choice) - 1]
            edit_single_season(seasonal_settings.profiles[season])

        elif choice == "5":
            seasonal_settings.active_season = select_season()

        elif choice == "0":
            return

        else:
            print("Invalid selection.")


def edit_single_season(season_profile):
    while True:
        print(f"\n{season_profile.season} SETTINGS")
        print(
            f"Brightness factor: {round(season_profile.brightness_factor*100)}%"
        )
        print(
            f"Color temperature factor: "
            f"{round(season_profile.color_temp_factor*100)}%"
        )

        print("1 - Edit brightness factor")
        print("2 - Edit color temperature factor")
        print("0 - Back")

        choice = input("Select option: ")

        if choice == "1":
            season_profile.brightness_factor = ask_percentage(
                "Enter brightness percentage: "
            )
            print("DEBUG stored brightness_factor =", season_profile.brightness_factor)

        elif choice == "2":
            season_profile.color_temp_factor = ask_percentage(
                "Enter color temperature percentage: "
            )

        elif choice == "0":
            return

        else:
            print("Invalid selection.")


def select_season():
    seasons = ["Spring", "Summer", "Autumn", "Winter"]

    print("\nSelect active season:")
    for i, s in enumerate(seasons, start=1):
        print(f"{i} - {s}")

    try:
        return seasons[int(input("Choice: ")) - 1]
    except (ValueError, IndexError):
        print("Invalid selection. Keeping current season.")
        return seasons[-1]


# ---------- ROOMS ----------

def rooms_menu_loop(rooms):
    print("\nROOMS")
    for room in rooms:
        if room.profile_name:
            print(
                f"Room {room.room_id} | {room.room_type.type_name} | "
                f"{room.profile_name} | "
                f"B:{room.brightness} | CT:{room.color_temperature} | "
                f"{room.season} | "
                f"Synced:{room.synced_at.strftime('%H:%M:%S')}"
            )
        else:
            print(
                f"Room {room.room_id} | {room.room_type.type_name} | NOT SYNCED"
            )

    input("\nPress ENTER to return to main menu.")


# ---------- SYNC ----------

def sync_menu_loop(sync_service, profiles):
    while True:
        print("\nSYNC")
        print("1 - Sync profile to all rooms")
        print("0 - Main Menu")

        choice = input("Select option: ")

        if choice == "1":
            profile = select_profile(profiles)
            if profile:
                sync_service.sync_all_rooms(profile)
                print("Profile synced to all rooms.")

        elif choice == "0":
            return

        else:
            print("Invalid selection.")


def sync_from_profiles(sync_service, profiles):
    profile = select_profile(profiles)
    if profile:
        sync_service.sync_all_rooms(profile)
        print("Profile synced to all rooms.")


# ---------- HELPERS ----------

def select_profile(profiles):
    print("\nSelect profile:")
    names = list(profiles.keys())

    for i, name in enumerate(names, start=1):
        print(f"{i} - {name}")
    print("0 - Back")

    choice = input("Select option: ")

    if choice == "0":
        return None

    try:
        return profiles[names[int(choice) - 1]]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return None


def ask_int(prompt, min_val, max_val):
    try:
        value = int(input(prompt))
        if min_val <= value <= max_val:
            return value
    except ValueError:
        pass

    print("Invalid value.")
    return min_val


def ask_percentage(prompt):
    try:
        value = int(input(prompt))
        return value / 100
    except ValueError:
        print("Invalid value.")
        return 1.0
