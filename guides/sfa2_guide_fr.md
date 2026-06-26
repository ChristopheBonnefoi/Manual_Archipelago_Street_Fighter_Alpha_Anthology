# Guide Street Fighter Alpha 2

Ce guide explique le manual Street Fighter Alpha 2 pour Archipelago. Il sert à aider les joueurs à comprendre les personnages, les variantes cachées, les modes de jeu, les objectifs, les checks, les tokens Shadaloo Emblem et les options YAML utilisées par ce manual.

Street Fighter Alpha 2 est en cours d'intégration dans le projet Street Fighter Alpha Anthology. La logique pourra encore être ajustée dans de futures mises à jour.

## Personnages

Street Fighter Alpha 2 utilise des items de personnages pour décider quels personnages le joueur peut utiliser pour valider les checks.

Les items de personnages actuels sont :

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

### Notes des personnages

Les noms ci-dessous correspondent aux noms d'items utilisés par le manual.

- **Adon**
  - Rival conditionnel : M.Bison
  - Boss final : Sagat
- **Akuma**
  - Rival conditionnel : Ryu
  - Boss final : Gen
- **Birdie**
  - Rival conditionnel : Dhalsim
  - Boss final : M.Bison
- **Charlie Nash**
  - Rival conditionnel : Rolento
  - Boss final : M.Bison
- **Chun Li**
  - Rival conditionnel : Gen
  - Boss final : M.Bison
- **Chun Li Classic/SF2**
  - Comment jouer : sur Chun Li, maintenir Start environ 5 secondes, puis valider.
  - Rival conditionnel : Gen
  - Boss final : M.Bison
- **Dan**
  - Rival conditionnel : Guy
  - Boss final : Sagat
- **Dhalsim**
  - Rival conditionnel : Zangief
  - Boss final : M.Bison
- **Dhalsim EX**
  - Comment jouer : sur Dhalsim, maintenir Start, faire Gauche, Bas, Droite, Haut, puis valider.
  - Rival conditionnel : Zangief
  - Boss final : M.Bison
- **Evil Ryu**
  - Comment jouer : sur Ryu, maintenir Start, faire Droite, Haut, Bas, Gauche, puis valider.
  - Rival conditionnel : Sakura
  - Boss final : Akuma
- **Gen**
  - Rival conditionnel : Chun Li
  - Boss final : Akuma
- **Guy**
  - Rival conditionnel : Rose
  - Boss final : M.Bison
- **Ken**
  - Rival conditionnel : Dan
  - Boss final : Ryu
- **M.Bison**
  - Rival conditionnel : Charlie Nash
  - Boss final : Ryu
- **Rolento**
  - Rival conditionnel : Sodom
  - Boss final : Guy
- **Rose**
  - Rival conditionnel : Akuma
  - Boss final : M.Bison
- **Ryu**
  - Rival conditionnel : Sakura
  - Boss final : Akuma
- **Sagat**
  - Rival conditionnel : Adon
  - Boss final : Ryu
- **Sakura**
  - Rival conditionnel : Sagat
  - Boss final : Ryu
- **Shin Akuma**
  - Comment jouer : sur Akuma, maintenir Start environ 5 secondes, puis valider.
  - Rival conditionnel : Ryu
  - Boss final : Gen
- **Sodom**
  - Rival conditionnel : Ken
  - Boss final : Guy
- **Zangief**
  - Rival conditionnel : Birdie
  - Boss final : Ken
- **Zangief EX**
  - Comment jouer : sur Zangief, maintenir Start, faire Bas, Gauche quatre fois, Haut deux fois, Droite quatre fois, Bas, puis valider.
  - Rival conditionnel : Birdie
  - Boss final : Ken

### Utilisation des personnages

Quand vous recevez un item de personnage, vous pouvez utiliser ce personnage pour les checks qui le demandent.

Par exemple :

- `Ryu - Fight 01 Clear` demande Ryu.
- `Chun Li Classic/SF2 - Win Arcade Mode` demande Chun Li Classic/SF2.
- `Evil Ryu - Survival Fight 18 - Defeat Akuma` demande Evil Ryu et Survival Mode.

Les variantes cachées comme Evil Ryu, Shin Akuma, Dhalsim EX, Zangief EX et Chun Li Classic/SF2 doivent être utilisées seulement pour les checks qui demandent leur propre item.

## Modes de jeu

Le manual supporte actuellement trois modes de jeu principaux.

### Arcade Mode

Arcade Mode est le mode classique de Street Fighter Alpha 2.

La plupart des checks Arcade sont basés sur le fait de terminer des combats avec un personnage précis, finir l'Arcade Mode, et compléter des objectifs spécifiques, des checks de rivalité ou des checks spéciaux.

### Survival Mode

Survival Mode est basé sur des combats de survie à terminer avec les personnages débloqués.

Les checks sont écrits par personnage, numéro de combat et nom d'adversaire, par exemple :

- `Adon - Survival Fight 01 - Defeat Ken`
- `Ryu - Survival Fight 10 - Defeat Rolento`
- `Chun Li Classic/SF2 - Survival Fight 18 - Defeat Akuma`

Si Survival Mode est désactivé dans le YAML, les checks Survival et l'item Survival Mode sont retirés de la seed.

### Dramatic Battle Mode

Dramatic Battle Mode est un mode difficile en 2 contre 1.

Le manual peut utiliser des checks dans ce mode, notamment des objectifs liés aux combats ou aux actions de combat. Comme ce mode utilise un partenaire, le partenaire doit être choisi parmi les personnages débloqués quand c'est possible.

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

Street Fighter Alpha 2 utilise des items filler cosmétiques personnalisés au lieu d'utiliser seulement le fallback générique `Points`.

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

### Ajouter des tokens disponibles en plus

L'option `shadaloo_emblems_available_percentage` contrôle combien de Shadaloo Emblems sont placés dans le pool d'items par rapport au nombre requis.

Exemple : si l'objectif demande 25 Shadaloo Emblems et que cette option est réglée sur 200, la seed placera 50 Shadaloo Emblems au total.

```yaml
shadaloo_emblems_available_percentage:
  200: 50
  random: 0
  random-low: 0
  random-high: 0
  random-range-100-400: 0
```

Le nombre total est limité à 100 Shadaloo Emblems.

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
Chun Li Classic/SF2 - Win Arcade Mode
```

Utilisez le personnage ou la variante indiquée et terminez l'Arcade Mode.

### Checks Survival

Exemple :

```text
Rose - Survival Fight 10 - Defeat Rolento
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
Ken - The Rival Finally Smiles - Defeat Dan
```

Utilisez le personnage indiqué et complétez l'objectif décrit par le nom de la location.

Note Rival Match pour Street Fighter Alpha 2 :

- Les rival checks se font en Arcade Mode.
- Pour déclencher le rival, ne perdez aucun round.
- Gagnez au moins 5 rounds avec un Super Combo Finish ou un Custom Combo Finish.
- Le rival remplace ensuite un adversaire normal avant la fin de la route.

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
- Les variantes cachées doivent utiliser le nom exact de l'item indiqué dans ce guide.
- Si une seed semble impossible, vérifiez l'objectif choisi, les modes activés, les options optionnelles et le spoiler log.
- Hyper Street Fighter Alpha n'est pas prévu pour ce manual parce que c'est principalement un mode versus 2 joueurs sans progression contre le CPU.
