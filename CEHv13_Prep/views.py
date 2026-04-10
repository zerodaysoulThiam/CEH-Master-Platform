"""
Routes and views for the Flask application CEHv13_Prep.
"""

from datetime import datetime
from flask import render_template, abort
import os
import json
from flask import request, redirect
from CEHv13_Prep import app
from flask import url_for
from flask import request, render_template
from datetime import datetime
# Liste de tous les modules disponibles avec leurs titres
MODULES = [
    {"id": 1, "title": "Introduction to Ethical Hacking"},
    {"id": 2, "title": "Footprinting and Reconnaissance"},
    {"id": 3, "title": "Scanning Networks"},
    {"id": 4, "title": "Enumeration"},
    {"id": 5, "title": "Vulnerability Analysis"},
    {"id": 6, "title": "System Hacking"},
    {"id": 7, "title": "Malware Threats"},
    {"id": 8, "title": "Sniffing"},
    {"id": 9, "title": "Social Engineering"},
    {"id": 10, "title": "Denial of Service"},
    {"id": 11, "title": "Session Hijacking"},
    {"id": 12, "title": "Evading IDS, Firewalls and Honeypots"},
    {"id": 13, "title": "Hacking Web Servers"},
    {"id": 14, "title": "Hacking Web Applications"},
    {"id": 15, "title": "SQL Injection"},
    {"id": 16, "title": "Hacking Wireless Networks"},
    {"id": 17, "title": "Hacking Mobile Platforms"},
    {"id": 18, "title": "IoT Hacking & OT Hacking"},
    {"id": 19, "title": "Cloud Computing"},
    {"id": 20, "title": "Cryptography"}
]

# Page d'accueil
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'index.html',
        title='Accueil',
        year=datetime.now().year,
        progress_percent=35
    )

# Page des modules (cours)
@app.route('/cours')
def cours():
    return render_template(
        'cours.html',
        title='Cours',
        year=datetime.now().year,
        message='La page de cours'
    )

# Détail d'un module (cours spécifique)
@app.route('/modules/<int:module>/cours')
def cours_detail(module):
    # Vérifie si le module existe
    if not any(m['id'] == module for m in MODULES):
        abort(404, description="Module non trouvé")
    
    return render_template(
        f'modules/module{module}/cours/cours.html',
        title=f'Détails du Module {module}',
        year=datetime.now().year,
        module=module
    )

# Glossaire
@app.route('/glossaire')
def glossaire():
    return render_template(
        'glossaire.html',
        title='Glossaire',
        year=datetime.now().year,
        message='Retrouvez ici les définitions essentielles pour le CEH.'
    )

# Examens blancs
@app.route('/examens-blancs')
def examens_blancs():
    return render_template(
        'examens_blancs.html',
        title='Examens blancs',
        year=datetime.now().year
    )

# Examen final
@app.route('/examen-final')
def examen_final():
    return render_template(
        'examen_final.html',
        title='Examen final',
        year=datetime.now().year
    )

# Statistiques
@app.route('/statistiques')
def statistiques():
    return render_template(
        'statistiques.html',
        title='Statistiques',
        year=datetime.now().year
    )

# Page de liste des quiz
@app.route('/quiz_list')
def quiz_list():
    return render_template(
        'quiz_list.html',
        title='Liste des Quiz',
        year=datetime.now().year,
        quiz_modules=MODULES
    )

# Route pour un quiz spécifique
@app.route("/modules/<int:module>/quiz")
def quiz_page(module):
    if module == 1:
        return render_template("modules/module1/quiz/quiz.html", module=module)
    elif module == 2:
        return render_template("modules/module2/quiz/quiz.html", module=module)
    elif module == 3:
        return render_template("modules/module3/quiz/quiz.html", module=module)
    elif module == 4:
        return render_template("modules/module4/quiz/quiz.html", module=module)
    elif module == 5:
        return render_template("modules/module5/quiz/quiz.html", module=module)
    elif module == 6:
        return render_template("modules/module6/quiz/quiz.html", module=module)
    elif module == 7:
        return render_template("modules/module7/quiz/quiz.html", module=module)
    elif module == 8:
        return render_template("modules/module8/quiz/quiz.html", module=module)
    elif module == 9:
        return render_template("modules/module9/quiz/quiz.html", module=module)
    elif module == 10:
        return render_template("modules/module10/quiz/quiz.html", module=module)
    elif module == 11:
        return render_template("modules/module11/quiz/quiz.html", module=module)
    elif module == 12:
        return render_template("modules/module12/quiz/quiz.html", module=module)
    elif module == 13:
        return render_template("modules/module13/quiz/quiz.html", module=module)
    elif module == 14:
        return render_template("modules/module14/quiz/quiz.html", module=module)
    elif module == 15:
        return render_template("modules/module15/quiz/quiz.html", module=module)
    elif module == 16:
        return render_template("modules/module16/quiz/quiz.html", module=module)
    elif module == 17:
        return render_template("modules/module17/quiz/quiz.html", module=module)
    elif module == 18:
        return render_template("modules/module18/quiz/quiz.html", module=module)
    elif module == 19:
        return render_template("modules/module19/quiz/quiz.html", module=module)
    elif module == 20:
        return render_template("modules/module20/quiz/quiz.html", module=module)
    else:
        return "Module non pris en charge", 404
# Nouvelle route pour les simulations d'examen
@app.route('/examen/<string:type>/<int:id>')
def examen_simulation(type, id):
    # Ici vous ajouterez la logique pour charger les questions
    # Pour l'instant nous affichons juste une page de démonstration
    
    title = "Examen Final" if type == "final" else f"Examen Blanc {id}"
    
    return render_template(
        'examen_simulation.html',
        title=title,
        year=datetime.now().year,
        exam_type=type,
        exam_id=id
    )
@app.route('/examen/resultats')
def examen_resultats():
    exam_type = request.args.get('type', 'blanc')
    exam_id = request.args.get('id', 1, type=int)
    score = request.args.get('score', 0, type=int)
    passed = score >= 70  # 70% est le seuil de réussite
    
    # Obtenir la date actuelle formatée
    current_date = datetime.now().strftime('%d/%m/%Y')

    return render_template(
        'examen_resultats.html',
        title='Résultats',
        year=datetime.now().year,
        exam_type=exam_type,
        exam_id=exam_id,
        score=score,
        passed=passed,
        current_date=current_date  # Passer la date formatée
    )