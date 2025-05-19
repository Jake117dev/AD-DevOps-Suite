# Deklaration der Ordnerstruktur als Hashtable
$folders = @{
    "Abteilungsname" = @{  # Ersetzen Sie "Abteilungsname" durch den Namen Ihrer Abteilung
        "Ordner1" = $null  # Ersetzen Sie "Ordner1" durch den Namen Ihres Ordners
        "Ordner2" = $null  # Fügen Sie so viele Ordner hinzu, wie Sie benötigen
        "Ordner3" = @{
            "Unterordner1" = $null  # Sie können Unterordner auf die gleiche Weise hinzufügen
            "Unterordner2" = $null  # Die Anzahl der Unterordner ist unbegrenzt
        }
    }
}

# Funktion zur Erstellung der Ordnerstruktur
function New-FolderStructure {
    param (
        [Parameter(Mandatory = $true)]
        [string] $Path,  # Der Pfad, in dem die Ordnerstruktur erstellt wird

        [Parameter(Mandatory = $true)]
        [hashtable] $Structure  # Die Hashtable, die die Ordnerstruktur darstellt
    )

    # Für jeden Ordner in der Struktur
    foreach ($folder in $Structure.Keys) {
        # Berechnen Sie den vollständigen Pfad zum Ordner
        $folderPath = Join-Path -Path $Path -ChildPath $folder
        # Erstellen Sie den Ordner
        New-Item -ItemType Directory -Path $folderPath -ErrorAction SilentlyContinue

        # Wenn der Ordner Unterordner hat
        if ($null -ne $Structure[$folder]) {
            # Rufen Sie die Funktion rekursiv auf, um die Unterordner zu erstellen
            New-FolderStructure -Path $folderPath -Structure $Structure[$folder]
        }
    }
}

# Der Pfad, in dem die Ordnerstruktur erstellt wird
$rootPath = "Pfad-zu-Ihrem-Verzeichnis"  # Ersetzen Sie "Pfad-zu-Ihrem-Verzeichnis" durch den tatsächlichen Pfad
# Aufruf der Funktion zur Erstellung der Ordnerstruktur
New-FolderStructure -Path $rootPath -Structure $folders
