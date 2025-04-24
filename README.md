# Web-Security-Lab

Laboratoire d’outils de sécurité web pour la détection et l’exploitation de vulnérabilités.

## Structure du projet

- **Scripts/** : scripts d’automatisation (bash, Python, PowerShell, Go)  
- **Docs/** : guides et notes  
- **Tools/** : outils tiers pré-packagés (ne pas modifier)  
- **reports/** : résultats de tests  
- **requirements.txt** : dépendances Python  

## Prérequis

- Python 3.8+  
- Go 1.16+  
- PowerShell 5.1+  
- Bash  

Installer les dépendances Python :
```bash
pip install -r requirements.txt
```

## Utilisation

### Bash
```bash
bash Scripts/Bash/xss_scanner.sh --url https://target.com
```

### Python
```bash
python3 Scripts/Python/web_crawler.py --start https://target.com
```

### PowerShell
```powershell
.\Scripts\Powershell\header_tester.ps1 -Url https://target.com
```

### Go
```bash
go run Scripts/Go/session_cookie_checker.go --url https://target.com
```

## CI & Qualité

- Tests Python avec pytest  
- Linting Bash & Go  
- Workflow GitHub Actions dans `.github/workflows/ci.yml`  

## Licence

MIT. Voir [LICENSE](LICENSE).
