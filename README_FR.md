# Manual_Archipelago_Street_Fighter_Alpha_Anthology

## Bienvenue !

Bienvenue sur le dépôt officiel du Manual Archipelago pour **Street Fighter Alpha Anthology** sur PlayStation 2. Cette compilation regroupe plusieurs versions des trois jeux Street Fighter Alpha.

## Projet :

Le projet est actuellement en ***Bêta***. L’objectif est de combiner les jeux compatibles disponibles dans la compilation en un seul projet Manual Archipelago. Je propose également la possibilité de jouer à chaque jeu individuellement. Voici la liste des jeux :

Les 5 jeux de base :

* **Street Fighter Alpha**
* **Street Fighter Alpha 2**
* **Street Fighter Alpha 2 Gold**
* **Street Fighter Alpha 3**
* **Super Gem Fighter Mini Mix**

Les 2 jeux secrets :

* **Street Fighter Alpha 3 Upper**
* **Hyper Street Fighter Alpha**

**Note importante concernant Hyper Street Fighter Alpha :**
Hyper Street Fighter Alpha ne sera pas ajouté au Manual Archipelago. C’est principalement un mode versus 2 joueurs et il n’a pas de progression contre le CPU, donc il ne correspond pas à la structure de checks et d’objectifs utilisée par ce projet.

Actuellement, je traite les jeux individuellement avant de commencer le travail sur la version unifiée. Je réfléchis encore à la manière de gérer les items. Par exemple, pour des personnages comme Ryu, qui apparaissent dans tous les jeux, dois-je les rendre disponibles dans tous les jeux avec un item nommé simplement "Ryu", ou les joueurs devront-ils les récupérer pour chaque jeu avec des items nommés "Ryu Alpha 1", "Ryu Alpha 2", etc. ?

Je propose aussi la possibilité de jouer aux jeux individuellement pour les personnes qui préfèrent ne jouer qu’à un ou deux jeux de la liste. Plus tard, je prévois de configurer le YAML afin de permettre la sélection des jeux dans le pool. Cependant, pour cela, j’aurais besoin d’utiliser des hooks, et je ne sais pas encore comment les mettre en place.

## Fonctionnalités actuelles

Les autres jeux seront ajoutés dans de futures mises à jour.

### Street Fighter Alpha 1 :

#### Objectif :

**Token** : L'objectif Shadaloo Emblem peut être configuré dans le YAML pour demander un nombre de tokens entre 1 et 100, ou être randomisé pour un objectif surprise. Les tokens sont ajoutés au pool d'items seulement quand l'objectif choisi en a besoin.

#### Options YAML :

* **Modes de jeu :** Arcade Mode, Survival Mode et Dramatic Battle Mode peuvent être activés ou désactivés depuis le YAML.
* **Options de jeu :** Difficulty, Damage Levels, Timer Speed, Speed Select et Max Rounds peuvent être activés ou désactivés depuis le YAML.
* Au moins un mode de jeu doit rester actif.
* Certaines combinaisons d'options peuvent être bloquées pendant la génération s'il n'y a pas assez de checks actifs pour le pool d'items choisi.

#### Modes :

* **Arcade Mode :** Le mode de jeu classique.
* **Survival Mode :** Mode survie dans lequel l’objectif actuel est de gagner 10 combats.
* **Dramatic Battle Mode :** Un mode très difficile dans lequel vous combattez en 2 contre 1 et devez terminer 4 combats.

#### Autres règles :

* Les Super Combos sont des items progressifs et ne sont pas disponibles au début de la seed.
* La vitesse est présente dans le pool d’items, donc faites attention à ce paramètre.
* En Dramatic Battle Mode, le PNJ qui vous accompagne doit être choisi en fonction des personnages que vous avez débloqués, car vous pouvez valider des checks comme subir un stun, obtenir un perfect, gagner avec un Super Combo ou obtenir le first attack dans ce mode.

## Fonctionnalités futures (non garanties)

Les autres jeux seront ajoutés dans de futures mises à jour.

### Street Fighter Alpha 1 :

J’aimerais ajouter davantage d’objectifs et rendre la configuration du YAML aussi flexible que possible. Peut-être qu’un système où il faudrait récupérer les techniques de chaque personnage dans le pool d’items pourrait être ajouté, mais ce sera lorsque j’aurai appris à utiliser les hooks, afin de laisser aux joueurs la possibilité d’activer ou de désactiver cette fonctionnalité.

## Notes de patch

### Version 0.5.0 : Alpha 2 Update

#### Street Fighter Alpha 1
- Ajout d'un check `Finish the Survival Mode` pour chaque personnage de Street Fighter Alpha 1.
- Renommage des checks Survival Mode de Street Fighter Alpha 1 afin d'inclure l'ordre corrigé des adversaires de Ken jusqu'à Akuma.
- Conversion des fichiers `items.json` et `locations.json` de Street Fighter Alpha 1 vers le format Manual actuel avec enveloppe `data`, afin de garder la génération des templates compatible avec le launcher Archipelago.
- Ajout de l'option YAML `shadaloo_emblems_available_percentage` afin de permettre d'avoir plus de Shadaloo Emblems dans le pool d'items que le nombre requis pour l'objectif choisi.
- Mise à jour du hook Shadaloo Emblem afin que les tokens requis restent en progression et que les tokens supplémentaires soient considérés comme utiles.
- Mise à jour du tri des locations afin de mieux organiser les checks Survival, les checks de fin de Survival, les rivalités, les checks spéciaux, les options et les objectifs.
- Réorganisation des données de locations pour suivre le même tri propre que celui utilisé côté client.

#### Street Fighter Alpha 2
- Début du nettoyage et de l'intégration du manual Street Fighter Alpha 2.
- Conversion des fichiers `items.json` et `locations.json` de Street Fighter Alpha 2 vers le format Manual actuel avec enveloppe `data`, afin de garder la génération des templates compatible avec le launcher Archipelago.
- Correction des références restantes à Street Fighter Alpha 1 dans les données Alpha 2, la documentation d'installation, les informations meta et les messages de hooks.
- Ajout des checks Survival Mode manquants jusqu'au Fight 18 pour chaque personnage d'Alpha 2.
- Ajout d'un check `Finish the Survival Mode` pour chaque personnage d'Alpha 2.
- Renommage des checks Survival Mode d'Alpha 2 afin d'inclure l'ordre des adversaires de Ken jusqu'à Akuma.
- Synchronisation des hooks Alpha 2 avec le style de Street Fighter Alpha 1, incluant les fillers dynamiques, la validation des modes, la gestion des tokens et le tri côté client.
- Ajout de l'option YAML `shadaloo_emblems_available_percentage` à Alpha 2.
- Correction du JSON invalide et des fautes dans les `requires` de checks spéciaux concernant Dhalsim, Dhalsim EX et Zangief EX.
- Harmonisation des noms de checks Alpha 2 avec les vrais noms d'items, notamment `Chun Li`, `Chun Li Classic/SF2` et `M.Bison`.
- Réorganisation des checks de rivalité après les checks Survival et tri des checks spéciaux par nombre de personnages requis.
- Ajout des guides Street Fighter Alpha 2 en anglais et en français avec les notes de personnages, les manipulations des variantes cachées, les objectifs, les checks, les tokens et les explications YAML.

### Version 0.4.2 : Filler Update
- Ajout d'items filler personnalisés pour Street Fighter Alpha 1 avec la catégorie `Filler` et `count: 0`.
- Traduction des nouveaux noms d'items filler du français vers l'anglais.
- Ajout d'un hook filler dynamique basé sur la logique filler de Tekken 2.
- Les checks vides reçoivent maintenant un item filler personnalisé aléatoire au lieu d'utiliser uniquement le fallback générique `Points`.
- Ajout de clés de tri côté client afin de garder les checks mieux ordonnés.
- Ajout de la catégorie visible `Filler` afin que les items filler personnalisés soient correctement groupés dans le client.
- Ajout d'une sécurité pour limiter le nombre de tokens Shadaloo Emblem entre 1 et 100 quand un objectif à tokens est choisi.

### Version 0.4.1 : Documentation Update
- Ajout des guides Street Fighter Alpha 1 en anglais et en français dans le nouveau dossier `guides`.
- Ajout d'explications pour les personnages, les modes de jeu, les objectifs, les tokens Shadaloo Emblem, les checks courants et la configuration YAML.
- Ajout d'un guide d'installation en français pour la documentation du manual Street Fighter Alpha 1.
- Mise à jour de la documentation meta de Street Fighter Alpha 1 afin que le guide d'installation français puisse être listé par Archipelago.
- Clarification du fait que Hyper Street Fighter Alpha ne sera pas inclus, car c'est un mode versus 2 joueurs sans progression contre le CPU.

### Version 0.4.0 : YAML Cleanup + Game Mode Selection
- Ajout des options YAML `arcade_mode`, `survival_mode` et `dramatic_battle_mode`.
- Renommage des options YAML optionnelles avec des noms plus propres : `difficulty`, `damage_levels`, `timer_speed`, `speed_select` et `max_rounds`.
- Ajout de catégories de modes afin que désactiver un mode de jeu retire son item et ses checks de la seed.
- Mise à jour des items de départ optionnels pour utiliser les nouveaux noms d'options YAML.
- Ajout de sécurités de génération pour éviter les combinaisons de modes invalides.
- Ajout d'une validation pour bloquer les configurations YAML qui n'ont pas assez de checks actifs pour le pool d'items choisi.
- Ajout d'une logique pour retirer les personnages qui n'ont plus de checks actifs quand c'est possible.
- Mise à jour du template YAML par défaut avec les nouveaux noms de modes et d'options.

### Version 0.3.0 : Yaml + Token Update
- Ajout de l'option YAML `shadaloo_emblems_required` pour les objectifs Shadaloo Emblem.
- Les joueurs peuvent maintenant choisir un nombre de tokens Shadaloo Emblem entre 1 et 100.
- Ajout du support des valeurs random dans le YAML pour avoir un objectif surprise.
- Mise à jour de la logique des objectifs Shadaloo Emblem afin d'utiliser la valeur du YAML au lieu d'un nombre fixe de tokens.
- Ajout d'un hook afin que les tokens Shadaloo Emblem soient ajoutés au pool d'items seulement quand l'objectif choisi en a besoin.
- Mise à jour du template YAML par défaut avec la nouvelle option de tokens.
- Mise à jour des README pour expliquer le nouveau comportement des tokens.
- Reconstruction du fichier manual_sfa1_narusnake.apworld.

### Version 0.2.2 : Correctif Update
- Correction des problèmes de Street Fighter Alpha 1 après la mise à jour de Manual Archipelago.
- Suppression des events et régions d'exemple qui pouvaient bloquer la génération du YAML, comme Marvel event, Capcom event, Stars%, ExampleRegion et Example_Range.
- Nettoyage des options de jeu optionnelles afin que les options désactivées retirent maintenant leurs items et leurs checks.
- Ajout des conditions YAML sur les items de départ optionnels.
- Suppression de l'option inutilisée DLC_enabled dans le projet Street Fighter Alpha 1.
- Mise à jour du YAML par défaut avec les nouvelles options include.
- Nettoyage de la documentation web et des informations meta pour Street Fighter Alpha 1.
- Suppression du fichier de documentation template UltimateMarvelVsCapcom3 inutilisé.
- Correction de plusieurs noms de locations et fautes, comme Shadowloo, Deafeat et le problème d'apostrophe de Sodom.
- Reconstruction du fichier manual_sfa1_narusnake.apworld.

### Version 0.2.1 : Migration vers la nouvelle version archipelago
- Mise a jour de tout les dossier vers la nouvelel version archipelago pour tout les projet.

### Version 0.2.0 : Street Fighter Alpha 1 New Logic Update

* Réécriture de la syntaxe des `requires`.
* Amélioration de la logique.
* Suppression des catégories `Other Game Mode` et `Other Character`.
* Reclassement des personnages par ordre alphabétique dans `item.json` et `location.json`.
* Ajout de checks pour le Survival Mode.
* Ajout des options `Max_Rounds`, `Speed_Select`, `Timer_Speed`, `Damage_Levels` et `Difficulty` dans le pool d’items. Elles sont regroupées dans la catégorie `Game_Options` dans le client.
* Ajout de plusieurs nouveaux objectifs.
* Ajout de checks de rivalité pour chaque personnage.
* Modification des conditions `requires` pour les checks impliquant les Super Combos.
* Ajout de checks spéciaux.
* Modification de `Option.json`.
* Création de checks pour la catégorie `Option`.
* Ajout d’items de départ dans `Game.json`.

### Version 0.1.0 : Street Fighter Alpha 1 Update

* Première version bêta.
* Création de tous les types d’items : personnages, modes de jeu, tokens, supers, etc.
* Ajout de checks pour chaque mode histoire, triés par personnage.
* Ajout de checks pour le Survival Mode.
* Ajout de checks pour le Dramatic Super Battle Mode.
* Ajout de checks pour le first attack, le stun, le perfect win et la victoire avec un Super Combo.
* Les Super Combos sont définis comme des items progressifs pendant la randomisation de la liste.
* La vitesse du jeu est actuellement soit en mode normal, soit activée.
* Ajout de tous les personnages pour l’Arcade Mode.
* Ajout de Dan, Akuma et M.Bison pour les modes Survival et Dramatic Battle. Afin d’éviter de bloquer la génération des seeds, ces trois personnages disposent de leur propre catégorie.
* Objectif fixé à 100 tokens.

## Comment contribuer

Les contributions de tout le monde sont les bienvenues. Voici quelques manières de nous aider :

* **Retours :** Jouez les scénarios et donnez vos retours sur le gameplay et les instructions du manual.
* **Contributions au code :** Proposez des pull requests avec des corrections de bugs ou des suggestions de fonctionnalités.
* **Documentation :** Aidez à améliorer ce README ou à ajouter d’autres documentations.

## Contact

Si vous êtes streamer ou si vous avez des questions, n’hésitez pas à nous contacter sur le Discord Archipelago ou à ouvrir une issue ici sur GitHub. Je ferai de mon mieux pour répondre lorsque je serai disponible.

Nous avons hâte de voir comment vous aiderez à façonner l’avenir de ce projet !
