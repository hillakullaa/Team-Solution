class SyncService:
    def __init__(self, rooms, seasonal_settings):
        self.rooms = rooms
        self.seasonal_settings = seasonal_settings

    def sync_all_rooms(self, profile):
        season_profile = self.seasonal_settings.get_active_profile()

        for room in self.rooms:
            brightness, color_temp = self._calculate(profile, season_profile)
            room.apply_lighting(
                profile_name=profile.name,
                brightness=brightness,
                color_temperature=color_temp,
                season=season_profile.season
            )

    def _calculate(self, profile, season_profile):
        if profile.mode.name == "Sleep":
            return 0, 0

        b = int(profile.base_brightness * season_profile.brightness_factor)
        ct = int(profile.base_color_temperature * season_profile.color_temp_factor)

        return min(b, 100), ct
