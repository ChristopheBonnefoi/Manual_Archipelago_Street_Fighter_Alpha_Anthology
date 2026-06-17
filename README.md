# Manual_Archipelago_Street_Fighter_Alpha_Anthology

## Welcome!
Welcome to the official repository for the Archipelago Manual for Street Fighter Alpha Anthology on PlayStation 2. This game collection includes multiple versions of the three Street Fighter Alpha games.

## Project:

The project is currently in ***Beta***. The goal is to combine all 5 games available in the collection and the 2 secret games into one, creating a total of 7 games in 1. I am also providing the option to play each game individually. Here is the list of games:

The 5 base games:
- **Street Fighter Alpha**
- **Street Fighter Alpha 2**
- **Street Fighter Alpha 2 Gold**
- **Street Fighter Alpha 3**
- **Super Gem Fighter Mini Mix**

The 2 secret games:
- **Street Fighter Alpha 3 Upper**
- **Hyper Street Fighter Alpha**

Currently, I am treating the games individually before starting work on the unified version. I am still considering how to manage items. For example, for characters like Ryu, who appear in all games, should I make them available across all games with the item name "Ryu," or should players need to collect them for each game with items named "Ryu Alpha 1," "Ryu Alpha 2," etc.? I also provide the option to play the games individually for those who prefer to play only one or two games from the list (although later on, I plan to configure the YAML to allow game selection in the pool. However, for that, I would need to use hooks, which I do not currently know how to implement).

## Current Features

The other games will be added in future updates.

### Street Fighter Alpha 1:

#### Goal:
**Token**: The Shadaloo Emblem goal can be configured in the YAML to require any amount from 1 to 100 tokens, or randomized for a surprise objective. Tokens are only added to the item pool when the selected goal needs them.

#### Mode:
- **Arcade Mode:** The classic game mode.
- **Survival Mode:** Survival mode where the current goal is to win 10 battles.
- **Dramatic Battle Mode:** A very difficult mode where you fight 2 vs 1 and must finish 4 battles.

#### Other Rules:
- Super combos are progressive items and are not available at the beginning of the seed.
- Speed is in the item pool, so be careful with that.
- In Dramatic Battle Mode, the NPC that accompanies you must be chosen based on the characters you have unlocked, as you can validate checks such as getting stunned, perfect wins, winning with a super combo, and first attack in this mode.

## Future Features (not guaranteed)
The other games will be added in future updates.

### Street Fighter Alpha 1:
I would like to add more goals and make the YAML configuration as flexible as possible. Perhaps a system where you need to collect each character's techniques in the item pool, but that will be when I learn how to implement hooks to still give players the option to enable or disable this feature.

## Patch Notes

### Version 0.3.0: Yaml + Token Update
- Added the `shadaloo_emblems_required` YAML option for the Shadaloo Emblem goals.
- Players can now choose any Shadaloo Emblem token amount between 1 and 100.
- Added support for random token values in the YAML for a surprise objective.
- Updated the Shadaloo Emblem goal logic to use the YAML value instead of a fixed token requirement.
- Added a hook so Shadaloo Emblem tokens are only added to the item pool when the selected goal needs them.
- Updated the default YAML template with the new token option.
- Updated the README files to explain the new token behavior.
- Rebuilt the manual_sfa1_narusnake.apworld file.

### Version 0.2.2: Correctif Update
- Fixed Street Fighter Alpha 1 issues after the Manual Archipelago update.
- Removed leftover template events and regions that could block YAML generation, including Marvel event, Capcom event, Stars%, ExampleRegion, and Example_Range.
- Cleaned the optional game settings so disabled options now remove both their items and their checks.
- Added YAML option conditions to optional starting items.
- Removed the unused DLC_enabled option from the Street Fighter Alpha 1 project.
- Updated the default YAML with the new include options.
- Cleaned the web documentation and meta information for Street Fighter Alpha 1.
- Removed the unused UltimateMarvelVsCapcom3 template documentation file.
- Fixed several location names and typos, including Shadowloo, Deafeat, and the Sodom apostrophe issue.
- Rebuilt the manual_sfa1_narusnake.apworld file.

### Version 0.2.1: Migration to the New Archipelago Version
- Updated all folders to the new Archipelago version for all projects.

### Version 0.2.0: Street Fighter Alpha 1 New Logic Update
- Rewrote the requires syntax.
- Improved the logic.
- Removed the Other Game Mode and Other Character categories.
- Reorganized characters in alphabetical order in item.json and location.json.
- Added checks for Survival Mode.
- Added the Max_Rounds, Speed_Select, Timer_Speed, Damage_Levels, and Difficulty options to the item pool. These are grouped under the Game_Options category in the client.
- Added several new goals.
- Added rivalry checks for each character.
- Modified the requires conditions for checks involving super combos.
- Added special checks.
- Modified Option.json.
- Created checks for the Option category.
- Added starting items in Game.json.

### Version 0.1.0: Street Fighter Alpha 1 Update
- Initial Beta release.
- Creation of all item types: Characters, Game Mode, Token, Super, etc.
- Added checks for each story mode sorted by character.
- Added checks for Survival Mode.
- Added checks for Dramatic Super Battle Mode.
- Added checks for first attack, stun, perfect win, and winning with a super combo.
- Super combos set as progressive items during the randomization of the list.
- The Game Speed is currently either normal or speed on.
- Added all characters for Arcade Mode.
- Added Dan, Akuma, and M. Bison for Survival and Dramatic Battle modes. To ensure seed generation is not blocked, these three characters have their own category.
- Goal set to 100 tokens.

## How to Contribute
We welcome contributions from everyone. Here are a few ways you can help:
- **Feedback**: Play through the scenarios and provide feedback on gameplay and manual instructions.
- **Code Contributions**: Submit pull requests with bug fixes or feature suggestions.
- **Documentation**: Help improve this README or add other documentation.

## Contact
If you are a streamer or have any queries, do not hesitate to reach out on our Archipelago Discord or submit an issue here on GitHub. I will make an effort to respond when available.

We are excited to see how you will help shape the future of this project!
