function Create-OU {
    param (
        [Parameter(Mandatory=$true)]
        [string]$ouPath,
        [Parameter(Mandatory=$true)]
        [string]$ouName
    )
    $ou = "OU=$ouName,$ouPath"
    if (!(Get-ADOrganizationalUnit -Identity $ou -ErrorAction SilentlyContinue)) {
        New-ADOrganizationalUnit -Name $ouName -Path $ouPath -ProtectedFromAccidentalDeletion $false
    }
}

$baseOU = "OU=Benutzer,OU=,DC=,DC="

$OUs = @{
    "" = @{
        "" = $null
        }
    }
}

$excludedOUs = @("")

function createGroupName($ouName, $suffix) {
    $ouName = $ouName -replace "/", "_"
    return "_${ouName}_$suffix"
}

function createOUs($ouHierarchy, $parentPath) {
    foreach ($ou in $ouHierarchy.GetEnumerator()) {
        $ouName = $ou.Name
        $ouPath = "OU=$ouName,$parentPath"

	Create-OU -ouPath $parentPath -ouName $ouName
        
        New-ADOrganizationalUnit -Name $ouName -Path $parentPath -ProtectedFromAccidentalDeletion $False -PassThru

        if ($excludedOUs -notcontains $ouName) {
            $readGroupName = createGroupName $ouName "lesen"
            $writeGroupName = createGroupName $ouName "lesen_schreiben"

            New-ADGroup -Name $readGroupName -Path $ouPath -GroupCategory Security -GroupScope DomainLocal
            New-ADGroup -Name $writeGroupName -Path $ouPath -GroupCategory Security -GroupScope DomainLocal
        }

        if ($ou.Value -is [Hashtable]) {
            createOUs $ou.Value $ouPath
        }
    }
}

createOUs $OUs $baseOU
