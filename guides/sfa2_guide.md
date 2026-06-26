# Street Fighter Alpha 2 Guide

This guide explains the Street Fighter Alpha 2 manual for Archipelago. It is meant to help players understand the characters, hidden variants, game modes, goals, checks, Shadaloo Emblem tokens, and YAML options used by this manual.

Street Fighter Alpha 2 is currently being integrated into the Street Fighter Alpha Anthology manual project. Some logic may still be adjusted in later updates.

## Characters

Street Fighter Alpha 2 uses character items to decide which characters the player is allowed to use for checks.

The current character items are:

- Adon
- Akuma
- Birdie
- Charlie Nash
- Chun Li
- Chun Li Classic/SF2
- Dan
- Dhalsim
- Dhalsim EX
- Evil Ryu
- Gen
- Guy
- Ken
- M.Bison
- Rolento
- Rose
- Ryu
- Sagat
- Sakura
- Shin Akuma
- Sodom
- Zangief
- Zangief EX

### Character Notes

The names below match the item names used by the manual.

- **Adon**
  - Conditional rival: M.Bison
  - Final boss: Sagat
- **Akuma**
  - Conditional rival: Ryu
  - Final boss: Gen
- **Birdie**
  - Conditional rival: Dhalsim
  - Final boss: M.Bison
- **Charlie Nash**
  - Conditional rival: Rolento
  - Final boss: M.Bison
- **Chun Li**
  - Conditional rival: Gen
  - Final boss: M.Bison
- **Chun Li Classic/SF2**
  - How to play: highlight Chun Li, hold Start for about 5 seconds, then confirm.
  - Conditional rival: Gen
  - Final boss: M.Bison
- **Dan**
  - Conditional rival: Guy
  - Final boss: Sagat
- **Dhalsim**
  - Conditional rival: Zangief
  - Final boss: M.Bison
- **Dhalsim EX**
  - How to play: highlight Dhalsim, hold Start, press Left, Down, Right, Up, then confirm.
  - Conditional rival: Zangief
  - Final boss: M.Bison
- **Evil Ryu**
  - How to play: highlight Ryu, hold Start, press Right, Up, Down, Left, then confirm.
  - Conditional rival: Sakura
  - Final boss: Akuma
- **Gen**
  - Conditional rival: Chun Li
  - Final boss: Akuma
- **Guy**
  - Conditional rival: Rose
  - Final boss: M.Bison
- **Ken**
  - Conditional rival: Dan
  - Final boss: Ryu
- **M.Bison**
  - Conditional rival: Charlie Nash
  - Final boss: Ryu
- **Rolento**
  - Conditional rival: Sodom
  - Final boss: Guy
- **Rose**
  - Conditional rival: Akuma
  - Final boss: M.Bison
- **Ryu**
  - Conditional rival: Sakura
  - Final boss: Akuma
- **Sagat**
  - Conditional rival: Adon
  - Final boss: Ryu
- **Sakura**
  - Conditional rival: Sagat
  - Final boss: Ryu
- **Shin Akuma**
  - How to play: highlight Akuma, hold Start for about 5 seconds, then confirm.
  - Conditional rival: Ryu
  - Final boss: Gen
- **Sodom**
  - Conditional rival: Ken
  - Final boss: Guy
- **Zangief**
  - Conditional rival: Birdie
  - Final boss: Ken
- **Zangief EX**
  - How to play: highlight Zangief, hold Start, press Down, Left four times, Up twice, Right four times, Down, then confirm.
  - Conditional rival: Birdie
  - Final boss: Ken

### Character Usage

When you receive a character item, you may use that character for checks that require them.

For example:

- `Ryu - Fight 01 Clear` requires Ryu.
- `Chun Li Classic/SF2 - Win Arcade Mode` requires Chun Li Classic/SF2.
- `Evil Ryu - Survival Fight 18 - Defeat Akuma` requires Evil Ryu and Survival Mode.

Hidden variants such as Evil Ryu, Shin Akuma, Dhalsim EX, Zangief EX, and Chun Li Classic/SF2 should only be used for checks that specifically require their own item.

## Game Modes

The manual currently supports three main game modes.

### Arcade Mode

Arcade Mode is the classic Street Fighter Alpha 2 mode.

Most Arcade checks are based on clearing fights with a specific character, winning Arcade Mode, and completing character-specific rivalry or special objectives.

### Survival Mode

Survival Mode is based on clearing Survival fights with unlocked characters.

The checks are written by character, fight number, and opponent name, such as:

- `Adon - Survival Fight 01 - Defeat Ken`
- `Ryu - Survival Fight 10 - Defeat Rolento`
- `Chun Li Classic/SF2 - Survival Fight 18 - Defeat Akuma`

If Survival Mode is disabled in the YAML, Survival checks and the Survival Mode item are removed from the seed.

### Dramatic Battle Mode

Dramatic Battle Mode is a difficult 2 vs 1 mode.

The manual can use checks in this mode, including objectives based on clearing fights or validating combat actions. Because this mode uses a partner character, the partner should be selected from the characters you have unlocked whenever possible.

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

Street Fighter Alpha 2 uses custom cosmetic filler items instead of only using the generic `Points` fallback.

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

### Setting Extra Available Tokens

The `shadaloo_emblems_available_percentage` option controls how many Shadaloo Emblems are placed in the item pool compared to the required amount.

Example: if the goal requires 25 Shadaloo Emblems and this option is set to 200, the seed will place 50 Shadaloo Emblems total.

```yaml
shadaloo_emblems_available_percentage:
  200: 50
  random: 0
  random-low: 0
  random-high: 0
  random-range-100-400: 0
```

The total amount is capped at 100 Shadaloo Emblems.

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
Chun Li Classic/SF2 - Win Arcade Mode
```

Use the named character or variant and complete Arcade Mode.

### Survival Fight Checks

Example:

```text
Rose - Survival Fight 10 - Defeat Rolento
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
Ken - The Rival Finally Smiles - Defeat Dan
```

Use the named character and complete the objective described by the location name.

Rival match notes for Street Fighter Alpha 2:

- Rival checks are performed in Arcade Mode.
- To trigger the rival, do not lose any round.
- Win at least 5 rounds with a Super Combo Finish or a Custom Combo Finish.
- The rival then replaces a normal opponent before the end of the route.

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
- Hidden variants should use the exact character item name shown in this guide.
- If a seed seems impossible, check the selected goal, enabled modes, optional settings, and spoiler log.
- Hyper Street Fighter Alpha is not planned for this manual because it is mainly a 2-player versus mode without CPU progression.
