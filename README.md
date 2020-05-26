Die Anwendung erstellt und verwaltet eine ToDo-Liste basierend auf einer Client-/Server-Architektur. Die Anwendung benötigt Django. Die folgende Anleitung setzt ferner die Installation von Virtual Environment voraus.

Start des Servers auf Ubuntu:

Virtual Environment starten. Hierfür in den Ordner gehen, in dem das Projekt ablegt wurde. Dort den Befehl virtualenv .venv eingeben. Anschließend mit dem Befehl source .venv/bin/activate virtuelle Umgebung aktivieren. 

Anschließend in den obersten Ordner des Projekts mit den Namen mytodo wechseln (cd mytodo). Dort mit dem Befehl python3 manage.py runserver den Server starten. 

Nur beim erstmaligen Start der Anwendung: Vor dem Start des Servers muss die SQLite-Datenbank eingerichtet werden. Hierfür im obersten Ordner des Projekts mit den Namen mytodo den Befehl python3 manage.py makemigrations eingeben. Anschließend den Befehl python3 manage.py migrate
