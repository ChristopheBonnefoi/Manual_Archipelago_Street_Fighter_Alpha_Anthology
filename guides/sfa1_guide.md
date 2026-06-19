# Street Fighter Alpha 1 Guide

This guide explains the Street Fighter Alpha 1 manual for Archipelago. It is meant to help players understand the characters, game modes, goals, checks, tokens, and YAML options used by this manual.

Street Fighter Alpha 1 is currently the most complete game in this project. The other games from Street Fighter Alpha Anthology are planned for later updates.

## Characters

Street Fighter Alpha 1 uses character items to decide which characters the player is allowed to use for checks.

The current character items are:

- Adon
- Akuma
- Birdie
- Charlie Nash
- Chun Li
- Dan
- Guy
- Ken
- M.Bison
- Rose
- Ryu
- Sagat
- Sodom

### Arcade Mode Characters

The Arcade Mode checks are built around the characters that are playable in Street Fighter Alpha 1 Arcade Mode:

- Adon
- Birdie
- Charlie Nash
- Chun Li
- Guy
- Ken
- Rose
- Ryu
- Sagat
- Sodom

Dan, M.Bison, and Akuma are not used as Arcade Mode playable characters in this manual. They are still part of the manual because they can matter for other modes such as Survival Mode and Dramatic Battle Mode.

If only Arcade Mode is enabled, the generator can remove character items that no longer have active checks.

### Character Usage

When you receive a character item, you may use that character for checks that require them.

For example:

- `Ryu - Fight 01 Clear` requires Ryu.
- `Ken - Win Arcade Mode` requires Ken.
- `Akuma - Fight 01 in Survival Mode` requires Akuma and Survival Mode.

In Dramatic Battle Mode, your partner character should also be chosen based on the characters you have unlocked.

## Game Modes

The manual currently supports three main game modes.

### Arcade Mode

Arcade Mode is the classic Street Fighter Alpha 1 mode.

Most Arcade checks are based on clearing fights with a specific character, winning Arcade Mode, and completing character-specific or rivalry-style objectives.

### Survival Mode

Survival Mode is based on clearing Survival fights with unlocked characters.

The checks are written by character and fight number, such as:

- `Adon - Fight 01 in Survival Mode`
- `Ryu - Fight 10 in Survival Mode`
- `M.Bison - Fight 13 in Survival Mode`

If Survival Mode is disabled in the YAML, Survival checks and the Survival Mode item are removed from the seed.

### Dramatic Battle Mode

Dramatic Battle Mode is a difficult 2 vs 1 mode.

The manual uses special checks in this mode, such as perfect rounds, stuns, first attacks, and winning with a Super Combo.

Because this mode uses a partner character, the partner should be selected from the characters you have unlocked whenever possible.

## Game Speed and Speed Select

`Game Speed - Normal` and `Game Speed - Turbo` are separate from the `speed_select` YAML option.

Game Speed is treated as a basic gameplay choice that can be given at the start of the seed.

Speed Select is an optional game setting category. If `speed_select` is enabled in the YAML, extra checks and related items for Speed Select are added to the seed.

## Goals

The manual currently has five goals.

### Shadaloo Emblem Cleared

Collect the required number of Shadaloo Emblems.

The amount is controlled by the `shadaloo_emblems_required` YAML option. This goal is a token-based goal.

### All Arcade Modes Cleared

Clear the Arcade Mode objective.

This goal requires Arcade Mode to stay enabled in the YAML.

### All Survival Modes Cleared

Clear the Survival Mode objective.

This goal requires Survival Mode to stay enabled in the YAML.

### Full Game Cleared

Clear the full game objective using the active game modes.

For the intended full experience, Arcade Mode, Survival Mode, and Dramatic Battle Mode should all stay enabled.

### Full Game + Shadaloo Emblem Cleared

Clear the full game objective and collect the required number of Shadaloo Emblems.

This is also a token-based goal.

## Shadaloo Emblem Tokens

Shadaloo Emblems are token items used by token-based goals.

The number of required tokens can be configured in the YAML from 1 to 100. It can also be randomized for a surprise objective.

Tokens are only added to the item pool when the selected goal needs them.

Token goals:

- `Shadaloo Emblem Cleared`
- `Full Game + Shadaloo Emblem Cleared`

Non-token goals ignore the Shadaloo Emblem requirement during generation, even if the option is still visible in the YAML.

## Filler Items

When a seed has more active checks than real items to place, the manual fills the empty checks with filler items.

Street Fighter Alpha 1 uses custom cosmetic filler items instead of only using the generic `Points` fallback.

These filler items:

- are selected dynamically during generation;
- use the `Filler` category;
- have `count: 0` in `items.json`;
- do not unlock anything;
- do not affect progression.

## YAML Guide

The YAML file controls the options for your seed.

Archipelago YAML options are weighted. The value with the highest active weight is more likely to be chosen. If you want one exact choice, set it to `50` and set the others to `0`.

### Choosing One Goal

Example for an Arcade goal:

```yaml
goal:
  shadaloo emblem cleared: 0
  all arcade modes cleared: 50
  all survival modes cleared: 0
  full game cleared: 0
  full game + shadaloo emblem cleared: 0
```

Example for a token goal:

```yaml
goal:
  shadaloo emblem cleared: 50
  all arcade modes cleared: 0
  all survival modes cleared: 0
  full game cleared: 0
  full game + shadaloo emblem cleared: 0
```

### Setting Token Amount

Example for exactly 50 Shadaloo Emblems:

```yaml
shadaloo_emblems_required:
  50: 50
  random: 0
  random-low: 0
  random-high: 0
  random-range-1-100: 0
```

Example for a random amount between 1 and 100:

```yaml
shadaloo_emblems_required:
  100: 0
  random: 0
  random-low: 0
  random-high: 0
  random-range-1-100: 50
```

This option only matters when the selected goal requires Shadaloo Emblems.

### Game Mode Options

At least one game mode must stay enabled.

```yaml
arcade_mode:
  true: 50
  false: 0

survival_mode:
  true: 50
  false: 0

dramatic_battle_mode:
  true: 50
  false: 0
```

To disable a mode, swap the weights:

```yaml
dramatic_battle_mode:
  true: 0
  false: 50
```

If a mode is disabled, its item and checks are removed from the seed.

### Optional Game Settings

These options are disabled by default:

- `difficulty`
- `damage_levels`
- `timer_speed`
- `speed_select`
- `max_rounds`

When enabled, they add extra items and checks related to Arcade Mode settings.

Example:

```yaml
difficulty:
  true: 50
  false: 0
```

If you are testing the manual for the first time, it is recommended to keep these optional settings disabled until you are comfortable with the main logic.

### Invalid YAML Combinations

Some YAML combinations are blocked during generation.

For example:

- `All Arcade Modes Cleared` cannot be used if `arcade_mode` is disabled.
- `All Survival Modes Cleared` cannot be used if `survival_mode` is disabled.
- At least one game mode must stay enabled.
- The seed must have enough active checks for the selected item pool.

If generation fails, check your selected goal, enabled modes, optional settings, and token amount.

## Check Explanations

Most checks follow a simple pattern.

### Fight Clear Checks

Example:

```text
Ryu - Fight 01 Clear
```

Use Ryu and clear the listed fight.

### Win Arcade Mode Checks

Example:

```text
Ken - Win Arcade Mode
```

Use Ken and complete Arcade Mode.

### Survival Fight Checks

Example:

```text
Rose - Fight 10 in Survival Mode
```

Use Rose in Survival Mode and clear the listed Survival fight.

### Perfect Round Checks

Example:

```text
Chun Li - Get Perfect Round
```

Use Chun Li and win a round without taking damage.

### Stun Checks

Example:

```text
Guy - Get Stun
```

Use Guy and stun the opponent during the fight.

### First Attack Checks

Example:

```text
Adon - Get First Attack
```

Use Adon and land the first hit of the round.

### Super Combo Checks

Example:

```text
Sagat - Win Round With Super
```

Use Sagat and win a round with a Super Combo.

Super Combos are progressive items and are not available at the beginning of the seed unless your YAML or multiworld settings give them early.

### Rivalry and Special Checks

Some checks are based on specific character matchups or special objectives.

Example:

```text
Ken - Rival's Pride - Defeat Ryu
```

Use the named character and complete the objective described by the location name.

### Option Checks

Option checks are only active if the matching YAML option is enabled.

Example:

```text
Win Arcade Mode with Free Speed Select
```

This requires the `speed_select` YAML option to be enabled and the matching Speed Select item to be available.

## Special Notes

- This manual is still in beta.
- Logic can still be adjusted in future versions.
- If a seed seems impossible, check the selected goal, enabled modes, optional settings, and spoiler log.
- Hyper Street Fighter Alpha is not planned for this manual because it is mainly a 2-player versus mode without CPU progression.
