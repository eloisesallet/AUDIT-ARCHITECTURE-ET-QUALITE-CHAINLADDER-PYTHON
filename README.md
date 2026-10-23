# Software Design & Evolution Analysis — Chainladder-python

Ce dépôt contient l'analyse socio-technique et l'étude d'évolution logicielle (réalisées entièrement en **anglais**) du projet open-source **[Chainladder-python](https://github.com/casact/chainladder-python)** (Casualty Actuarial Society). Ce travail a été effectué dans le cadre du cours **Software Design & Analysis (CSU33D06)** lors de mon semestre Erasmus à **Trinity College Dublin**.

> 🌐 **Note :** Le rapport complet, les analyses et le code sont intégralement rédigés en anglais.

---

## Objectif du Projet

L'objectif est d'analyser la structure, la santé architecturale et la dynamique de développement d'un paquet Python actuariel majeur de plus de 1 700 commits, utilisé pour la modélisation des réserves en assurance non-vie.

---

## Principaux Axes d'Analyse

### 1. Parties Prenantes & Vue Contexte (Rozanski & Woods)
* **Cartographie des acteurs :** Identification du groupe cœur de mainteneurs (John Bogaardt, Kenneth Hsu, Henry Ding, Gene Dan), de la communauté de plus de 30 contributeurs et du rôle de la **Casualty Actuarial Society (CAS)**.
* **Écosystème :** Analyse de l'intégration de la librairie au sein de la stack Data Science (`pandas`, `scikit-learn`, `numpy`).

### 2. Évolution Logicielle & Identification des Hotspots
Analyse extraite à l'aide de scripts Python utilisant **PyDriller** :
* **Fréquence des commits (2017–2026) :** Maintien régulier avec une moyenne de **~21 commits/mois**, marqué par des pics liés aux événements de l'industrie (ex. CAS Annual Meeting) et aux releases majeures (v0.9.0).
* **Hotspots principaux :** Identification des fichiers subissant le plus de modifications (`chainladder/core/triangle.py` avec 199 modifications, `base.py` avec 180).

### 3. Analyse de Complexité Cyclomatique
Mesures effectuées avec l'outil **Lizard** :
* **Moyenne globale excellente :** Complexité cyclomatique moyenne (AvgCCN) maintenue entre **3.0 et 5.0** sur le module core, garantissant une forte maintenabilité.
* **Zones complexes isolées :** Analyse des constructeurs et fonctions spécifiques (`triangle.py::__init__`, `grain`, `dunders.py`) qui centralisent la complexité algorithmique pour offrir une API simple à l'utilisateur final.

### 4. Vélocité de Revues de Code & Pull Requests
* Évaluation de la réactivité de l'équipe face aux PR automatisées (Dependabot) vs aux fonctionnalités actuarielles complexes nécessitant une validation métier rigoureuse[cite: 57].

---

## Outils & Technologies Utilisés

* **Langage :** Python 3
* **Analyse d'évolution :** PyDriller, Pandas, Matplotlib
* **Analyse de complexité :** Lizard
* **Rapport & Modélisation :** LaTeX, Cadre Rozanski & Woods

---

## Contenu du Dépôt

* `REPORT_SALLET_3.pdf` : Rapport d'analyse complet (*en anglais*).
* `softwareEvolution.py` : Script Python d'extraction des commits et de génération de la courbe d'évolution/hotspots.
