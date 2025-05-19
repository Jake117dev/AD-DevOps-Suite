# AD-DevOps-Suite

Automatisierte PowerShell-Werkzeugsammlung zur effizienten Verwaltung und Neustrukturierung von Active Directory-Umgebungen – ursprünglich entwickelt für ein Krankenhaus mit über 1300 Mitarbeitenden, jetzt modularisiert und universell einsetzbar.

## Übersicht

Die **AD-DevOps-Suite** bietet eine Reihe leistungsstarker PowerShell-Skripte zur schnellen und konsistenten Verwaltung von:

- **Benutzern**
- **Gruppen & Gruppenzugehörigkeiten**
- **Organizational Units (OUs)**
- **Rechtestrukturen & Gruppentypen (Uni / DomLokal / Global)**
- **AD-Verzeichnisstruktur**
- **Ordnerstrukturen auf Dateiebene**
- **Verknüpfungsbereinigungen (z. B. SAMAccountName)**

Ideal für Admins, DevOps-Teams oder Auszubildende, die sich mit AD-Prozessen automatisiert auseinandersetzen wollen.

## Features

- **Skripte zur Benutzererstellung**  
  - Einzel- oder Massenanlage
  - Mit vordefinierten Parametern & Sicherheitsgruppen
- **Dynamische Gruppenzuweisung**
  - Nutzer automatisch in Gruppen einfügen oder entfernen
- **Gruppenstrukturierung**
  - Anlage und Konfiguration von Gruppentypen
- **OU-Verwaltung**
  - Erstellen, Löschen (inkl. "nicht-löschbarer" OUs)
  - Automatisierter Strukturimport möglich
- **Ordnerstruktur-Automatisierung**
  - Skriptgesteuerter Aufbau kompletter Dateiverzeichnisse
- **SAMAccount-Analyse**
  - Identifikation und Entfernung alter AD-Verknüpfungen
- **Universalisierte Maskierung**
  - Alle Skripte enthalten Platzhalter für produktive Umgebungen

## Struktur

```
AD-DevOps-Suite/
├── create_users.ps1
├── create_groups.ps1
├── create_ou_structure.ps1
├── assign_users_to_groups.ps1
├── cleanup_samaccount_refs.ps1
├── setup_folder_structure.ps1
├── remove_locked_ou.ps1
├── check_group_or_ou.ps1
└── tools/
    └── snippets, analyses, prototypes
```

## Verwendung

Alle Skripte sind portabel und nutzen Standard-Windows-PowerShell (ab Version 5). Vor der Ausführung:

1. Skript mit passender Umgebung (Domäne, Struktur) anpassen.
2. PowerShell als Administrator starten.
3. Optional: Sicherheitsrichtlinien (ExecutionPolicy) prüfen.

## Lizenz

**MIT License** – Nutzung auf eigene Verantwortung. Keine Garantie.  
Einzusetzen in produktiven wie Test-Umgebungen nach entsprechender Prüfung.
