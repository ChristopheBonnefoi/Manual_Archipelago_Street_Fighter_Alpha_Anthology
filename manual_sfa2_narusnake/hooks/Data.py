import re


_GOAL_CATEGORY = "Goal"
_DRAMATIC_BATTLE_CATEGORY = "Dramatic Battle"
_OPTIONS_CATEGORY = "Options"
_SPECIAL_CATEGORY = "Special"
_OPTION_CATEGORY_ORDER = {
    "Difficulty": 10,
    "Damage_Levels": 20,
    "Timer_Speed": 30,
    "Speed_Select": 40,
    "Max_Rounds": 50,
}
_NON_CHARACTER_REQUIREMENTS = {
    "Arcade Mode",
    "Survival Mode",
    "Dramatic Battle Mode",
}


def _categories(location: dict) -> list[str]:
    categories = location.get("category", [])

    if isinstance(categories, str):
        return [categories]

    return categories


def _primary_category(location: dict) -> str:
    categories = _categories(location)
    return categories[0] if categories else ""


def _build_option_sort_key(location: dict, location_index: int) -> str:
    name = location.get("name", "")
    categories = _categories(location)

    for category in categories:
        if category in _OPTION_CATEGORY_ORDER:
            return f"{_OPTIONS_CATEGORY} {_OPTION_CATEGORY_ORDER[category]} {location_index} {name}"

    return f"{_OPTIONS_CATEGORY} 99 {location_index} {name}"


def _count_required_characters(location: dict) -> int:
    required_items = {
        item_name
        for item_name in re.findall(r"\|([^|]+)\|", str(location.get("requires", "")))
        if not item_name.startswith("@") and item_name not in _NON_CHARACTER_REQUIREMENTS
    }
    return len(required_items)


def _build_special_sort_key(location: dict, location_index: int) -> str:
    name = location.get("name", "")
    character_count = _count_required_characters(location)
    return f"{_SPECIAL_CATEGORY} {character_count:02d} Characters {location_index} {name}"


def _build_location_sort_key(location: dict, location_index: int) -> str:
    name = location.get("name", "")
    category = _primary_category(location)

    if category == _GOAL_CATEGORY or location.get("victory"):
        return f"{_GOAL_CATEGORY} {location_index} {name}"

    if category == _OPTIONS_CATEGORY:
        return _build_option_sort_key(location, location_index)

    if category == _SPECIAL_CATEGORY:
        return _build_special_sort_key(location, location_index)

    if category == _DRAMATIC_BATTLE_CATEGORY:
        match = re.match(r"^Fight (\d+) - .* in Dramatic Battle Mode$", name)
        if match:
            return f"{_DRAMATIC_BATTLE_CATEGORY} 10 Fight {int(match.group(1)):02d}"
        return f"{_DRAMATIC_BATTLE_CATEGORY} 99 {location_index} {name}"

    if not category:
        return f"Other {location_index} {name}"

    match = re.match(rf"^{re.escape(category)} - Fight (\d+) Clear$", name)
    if match:
        return f"{category} 10 Arcade Fight {int(match.group(1)):02d}"

    if name == f"{category} - Win Arcade Mode":
        return f"{category} 10 Arcade Fight 99 Win Arcade Mode"

    match = re.match(rf"^{re.escape(category)} - Fight (\d+) in Survival Mode$", name)
    if not match:
        match = re.match(rf"^{re.escape(category)} - Survival Fight (\d+) - Defeat .+$", name)
    if match:
        return f"{category} 20 Survival Fight {int(match.group(1)):02d}"

    if name in {f"{category} - Finish the Survival Mode", f"{category} - Finish Survival Mode"}:
        return f"{category} 21 Finish Survival Mode"

    if name.startswith(f"{category} - ") and " - Defeat " in name:
        return f"{category} 30 Rivalry {location_index} {name}"

    if name == f"{category} - Get Perfect Round":
        return f"{category} 40 Perfect Round"

    if name == f"{category} - Get Stun":
        return f"{category} 41 Stun"

    if name == f"{category} - Get First Attack":
        return f"{category} 42 First Attack"

    if name == f"{category} - Win Round With Super":
        return f"{category} 43 Win With Super"

    return f"{category} 50 Special {location_index} {name}"


# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table
# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:
    for location_index, location in enumerate(location_table):
        location.setdefault("sort-key", _build_location_sort_key(location, location_index))

    return location_table

# called after the events.json file has been loaded, before any processing has occurred
# If you need access to the events after processing, you should use the hooks in World.py
def after_load_event_file(event_table: list) -> list:
    return event_table

# called after the regions.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    return category_table

# called after the categories.json file has been loaded
def after_load_option_file(option_table: dict) -> dict:
    # option_table["core"] is the dictionary of modification of existing options
    # option_table["user"] is the dictionary of custom options
    return option_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table
