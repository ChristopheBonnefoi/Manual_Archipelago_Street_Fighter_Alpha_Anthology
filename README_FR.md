# Manual_Archipelago_Street_Fighter_Alpha_Anthology

## Bienvenue !

Bienvenue sur le dépôt officiel du Manual Archipelago pour **Street Fighter Alpha Anthology** sur PlayStation 2. Cette compilation regroupe plusieurs versions des trois jeux Street Fighter Alpha.

## Projet :

Le projet est actuellement en ***Bêta***. L’objectif est de combiner les 5 jeux disponibles dans la compilation ainsi que les 2 jeux secrets en un seul projet, pour créer un total de 7 jeux en 1. Je propose également la possibilité de jouer à chaque jeu individuellement. Voici la liste des jeux :

Les 5 jeux de base :

* **Street Fighter Alpha**
* **Street Fighter Alpha 2**
* **Street Fighter Alpha 2 Gold**
* **Street Fighter Alpha 3**
* **Super Gem Fighter Mini Mix**

Les 2 jeux secrets :

* **Street Fighter Alpha 3 Upper**
* **Hyper Street Fighter Alpha**

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
* Ajout de Dan, Akuma et M. Bison pour les modes Survival et Dramatic Battle. Afin d’éviter de bloquer la génération des seeds, ces trois personnages disposent de leur propre catégorie.
* Objectif fixé à 100 tokens.

## Comment contribuer

Les contributions de tout le monde sont les bienvenues. Voici quelques manières de nous aider :

* **Retours :** Jouez les scénarios et donnez vos retours sur le gameplay et les instructions du manual.
* **Contributions au code :** Proposez des pull requests avec des corrections de bugs ou des suggestions de fonctionnalités.
* **Documentation :** Aidez à améliorer ce README ou à ajouter d’autres documentations.

## Contact

Si vous êtes streamer ou si vous avez des questions, n’hésitez pas à nous contacter sur le Discord Archipelago ou à ouvrir une issue ici sur GitHub. Je ferai de mon mieux pour répondre lorsque je serai disponible.

Nous avons hâte de voir comment vous aiderez à façonner l’avenir de ce projet !
