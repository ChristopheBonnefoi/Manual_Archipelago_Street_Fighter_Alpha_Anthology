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
**Token**: The current goal is to collect 25 tokens.

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
- Goal set to 25 tokens.

## How to Contribute
We welcome contributions from everyone. Here are a few ways you can help:
- **Feedback**: Play through the scenarios and provide feedback on gameplay and manual instructions.
- **Code Contributions**: Submit pull requests with bug fixes or feature suggestions.
- **Documentation**: Help improve this README or add other documentation.

## Contact
If you are a streamer or have any queries, do not hesitate to reach out on our Archipelago Discord or submit an issue here on GitHub. I will make an effort to respond when available.

We are excited to see how you will help shape the future of this project!
