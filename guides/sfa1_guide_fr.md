# Guide Street Fighter Alpha 1

Ce guide explique le manual Street Fighter Alpha 1 pour Archipelago. Il sert à aider les joueurs à comprendre les personnages, les modes de jeu, les objectifs, les checks, les tokens et les options YAML utilisées par ce manual.

Street Fighter Alpha 1 est actuellement le jeu le plus complet du projet. Les autres jeux de Street Fighter Alpha Anthology sont prévus pour de futures mises à jour.

## Personnages

Street Fighter Alpha 1 utilise des items de personnages pour décider quels personnages le joueur peut utiliser pour valider les checks.

Les items de personnages actuels sont :

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

### Personnages en Arcade Mode

Les checks Arcade Mode sont construits autour des personnages jouables dans le mode Arcade de Street Fighter Alpha 1 :

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

Dan, M.Bison et Akuma ne sont pas utilisés comme personnages jouables en Arcade Mode dans ce manual. Ils font tout de même partie du manual parce qu'ils peuvent servir dans d'autres modes comme Survival Mode et Dramatic Battle Mode.

Si seul l'Arcade Mode est activé, le générateur peut retirer les items de personnages qui n'ont plus de checks actifs.

### Utilisation des personnages

Quand vous recevez un item de personnage, vous pouvez utiliser ce personnage pour les checks qui le demandent.

Par exemple :

- `Ryu - Fight 01 Clear` demande Ryu.
- `Ken - Win Arcade Mode` demande Ken.
- `Akuma - Fight 01 in Survival Mode` demande Akuma et Survival Mode.

En Dramatic Battle Mode, le partenaire contrôlé par le jeu doit aussi être choisi en fonction des personnages que vous avez débloqués quand c'est possible.

## Modes de jeu

Le manual supporte actuellement trois modes de jeu principaux.

### Arcade Mode

Arcade Mode est le mode classique de Street Fighter Alpha 1.

La plupart des checks Arcade sont basés sur le fait de terminer des combats avec un personnage précis, finir l'Arcade Mode, et compléter des objectifs spécifiques ou des checks de rivalité.

### Survival Mode

Survival Mode est basé sur des combats de survie à terminer avec les personnages débloqués.

Les checks sont écrits par personnage et par numéro de combat, par exemple :

- `Adon - Fight 01 in Survival Mode`
- `Ryu - Fight 10 in Survival Mode`
- `M.Bison - Fight 13 in Survival Mode`

Si Survival Mode est désactivé dans le YAML, les checks Survival et l'item Survival Mode sont retirés de la seed.

### Dramatic Battle Mode

Dramatic Battle Mode est un mode difficile en 2 contre 1.

Le manual utilise des checks spéciaux dans ce mode, comme obtenir un perfect, provoquer un stun, obtenir le first attack ou gagner avec un Super Combo.

Comme ce mode utilise un partenaire, le partenaire doit être choisi parmi les personnages débloqués quand c'est possible.

## Game Speed et Speed Select

`Game Speed - Normal` et `Game Speed - Turbo` sont séparés de l'option YAML `speed_select`.

Game Speed est traité comme un choix de gameplay de base qui peut être donné au départ de la seed.

Speed Select est une catégorie d'option de jeu. Si `speed_select` est activé dans le YAML, des checks et items supplémentaires liés au Speed Select sont ajoutés dans la seed.

## Objectifs

Le manual possède actuellement cinq objectifs.

### Shadaloo Emblem Cleared

Récupérer le nombre demandé de Shadaloo Emblems.

Le nombre est contrôlé par l'option YAML `shadaloo_emblems_required`. Cet objectif est un objectif à tokens.

### All Arcade Modes Cleared

Terminer l'objectif lié à l'Arcade Mode.

Cet objectif demande que l'Arcade Mode reste activé dans le YAML.

### All Survival Modes Cleared

Terminer l'objectif lié au Survival Mode.

Cet objectif demande que le Survival Mode reste activé dans le YAML.

### Full Game Cleared

Terminer l'objectif complet avec les modes de jeu actifs.

Pour l'expérience complète prévue, Arcade Mode, Survival Mode et Dramatic Battle Mode doivent rester activés.

### Full Game + Shadaloo Emblem Cleared

Terminer l'objectif complet et récupérer le nombre demandé de Shadaloo Emblems.

C'est aussi un objectif à tokens.

## Tokens Shadaloo Emblem

Les Shadaloo Emblems sont des items de tokens utilisés par les objectifs à tokens.

Le nombre de tokens demandé peut être configuré dans le YAML de 1 à 100. Il peut aussi être randomisé pour créer un objectif surprise.

Les tokens sont ajoutés au pool d'items seulement quand l'objectif choisi en a besoin.

Objectifs à tokens :

- `Shadaloo Emblem Cleared`
- `Full Game + Shadaloo Emblem Cleared`

Les objectifs sans tokens ignorent la valeur Shadaloo Emblem pendant la génération, même si l'option reste visible dans le YAML.

## Items filler

Quand une seed possède plus de checks actifs que de vrais items à placer, le manual remplit les checks vides avec des items filler.

Street Fighter Alpha 1 utilise des items filler cosmétiques personnalisés au lieu d'utiliser seulement le fallback générique `Points`.

Ces items filler :

- sont choisis dynamiquement pendant la génération ;
- utilisent la catégorie `Filler` ;
- ont `count: 0` dans `items.json` ;
- ne débloquent rien ;
- n'affectent pas la progression.

## Guide du YAML

Le fichier YAML contrôle les options de votre seed.

Les options YAML d'Archipelago fonctionnent avec des poids. Plus le nombre est élevé, plus cette valeur a de chances d'être choisie. Si vous voulez forcer un choix exact, mettez `50` sur ce choix et `0` sur les autres.

### Choisir un seul objectif

Exemple pour un objectif Arcade :

```yaml
goal:
  shadaloo emblem cleared: 0
  all arcade modes cleared: 50
  all survival modes cleared: 0
  full game cleared: 0
  full game + shadaloo emblem cleared: 0
```

Exemple pour un objectif à tokens :

```yaml
goal:
  shadaloo emblem cleared: 50
  all arcade modes cleared: 0
  all survival modes cleared: 0
  full game cleared: 0
  full game + shadaloo emblem cleared: 0
```

### Choisir le nombre de tokens

Exemple pour demander exactement 50 Shadaloo Emblems :

```yaml
shadaloo_emblems_required:
  50: 50
  random: 0
  random-low: 0
  random-high: 0
  random-range-1-100: 0
```

Exemple pour demander un nombre random entre 1 et 100 :

```yaml
shadaloo_emblems_required:
  100: 0
  random: 0
  random-low: 0
  random-high: 0
  random-range-1-100: 50
```

Cette option sert seulement quand l'objectif choisi demande des Shadaloo Emblems.

### Options de modes de jeu

Au moins un mode de jeu doit rester activé.

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

Pour désactiver un mode, inversez les poids :

```yaml
dramatic_battle_mode:
  true: 0
  false: 50
```

Si un mode est désactivé, son item et ses checks sont retirés de la seed.

### Options de jeu optionnelles

Ces options sont désactivées par défaut :

- `difficulty`
- `damage_levels`
- `timer_speed`
- `speed_select`
- `max_rounds`

Quand elles sont activées, elles ajoutent des items et checks supplémentaires liés aux réglages de l'Arcade Mode.

Exemple :

```yaml
difficulty:
  true: 50
  false: 0
```

Si vous testez le manual pour la première fois, il est conseillé de garder ces options désactivées jusqu'à être à l'aise avec la logique principale.

### Combinaisons YAML invalides

Certaines combinaisons YAML sont bloquées pendant la génération.

Par exemple :

- `All Arcade Modes Cleared` ne peut pas être utilisé si `arcade_mode` est désactivé.
- `All Survival Modes Cleared` ne peut pas être utilisé si `survival_mode` est désactivé.
- Au moins un mode de jeu doit rester activé.
- La seed doit avoir assez de checks actifs pour le pool d'items choisi.

Si la génération échoue, vérifiez l'objectif choisi, les modes activés, les options optionnelles et le nombre de tokens.

## Explication des checks

La plupart des checks suivent une logique simple.

### Checks Fight Clear

Exemple :

```text
Ryu - Fight 01 Clear
```

Utilisez Ryu et terminez le combat indiqué.

### Checks Win Arcade Mode

Exemple :

```text
Ken - Win Arcade Mode
```

Utilisez Ken et terminez l'Arcade Mode.

### Checks Survival

Exemple :

```text
Rose - Fight 10 in Survival Mode
```

Utilisez Rose en Survival Mode et terminez le combat Survival indiqué.

### Checks Perfect Round

Exemple :

```text
Chun Li - Get Perfect Round
```

Utilisez Chun Li et gagnez un round sans prendre de dégâts.

### Checks Stun

Exemple :

```text
Guy - Get Stun
```

Utilisez Guy et provoquez un stun sur l'adversaire pendant le combat.

### Checks First Attack

Exemple :

```text
Adon - Get First Attack
```

Utilisez Adon et donnez le premier coup du round.

### Checks Super Combo

Exemple :

```text
Sagat - Win Round With Super
```

Utilisez Sagat et gagnez un round avec un Super Combo.

Les Super Combos sont des items progressifs et ne sont pas disponibles au début de la seed, sauf si votre YAML ou les réglages du multiworld vous les donnent plus tôt.

### Checks de rivalité et checks spéciaux

Certains checks sont basés sur des matchups précis ou des objectifs spéciaux.

Exemple :

```text
Ken - Rival's Pride - Defeat Ryu
```

Utilisez le personnage indiqué et complétez l'objectif décrit par le nom de la location.

### Checks d'options

Les checks d'options sont actifs seulement si l'option YAML correspondante est activée.

Exemple :

```text
Win Arcade Mode with Free Speed Select
```

Ce check demande que l'option YAML `speed_select` soit activée et que l'item Speed Select correspondant soit disponible.

## Notes particulières

- Ce manual est encore en bêta.
- La logique peut encore être ajustée dans de futures versions.
- Si une seed semble impossible, vérifiez l'objectif choisi, les modes activés, les options optionnelles et le spoiler log.
- Hyper Street Fighter Alpha n'est pas prévu pour ce manual parce que c'est principalement un mode versus 2 joueurs sans progression contre le CPU.
