from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Templates (.html) :
# login
# logout
# 
# list_profile
# profile.usename
# 
# list.all
#
# lb.list
# lb.id
# lb.create
# rp.list
# rp.id
# rp.create
# ws.list
# ws.id
# ws.create


# Retourne du texte en attendant d'avoir des .html

# BIENVENUE

# Route pour la bage d'acceuil
@app.route("/")
def start(): 
    return render_template('start.html')
    
# Route pour la page de connexion
@app.route('/login')
def login():
    return 'Page de connexion'
    #return render_template('login.html')

# Route pour la déconnexion
@app.route('/logout')
def logout():
    return 'Vous êtes bien déco'
    #return render_template('logout.html')

# Route pour la liste des profils utilisateur
@app.route('/list_profile')
def list_profile():
    return 'Liste des profils utilisateur'
    #return render_template('list_profile.html')

# Route pour afficher le profil d'un utilisateur en particulier
@app.route('/profile/<username>')
def profile(username):
    return 'Profil de l\'utilisateur ' + username
    #return render_template('profile.html')

# Route pour la liste complète de toutes les configurations
@app.route('/list_all')
def list_all():
    return 'Liste complète de toutes les configurations'
    #return render_template('list.all.html')

#LOAD BALANCER

# Route pour la liste des Load Balancer
@app.route('/lb/list')
def lb_list():
    return 'Liste des Load Balancer'
    #return render_template('lb_list.html')

# Route pour afficher la configuration d'un Load Balancer en particulier
@app.route('/lb/<id>')
def lb_config(id):
    return 'Configuration du Load Balancer ' + id
    #return render_template('lb.' + id + '.html')

# Route pour créer un nouveau Load Balancer
@app.route('/lb/create', methods=['GET', 'POST'])
def lb_create():
    if request.method == 'POST':
        # Traitement des données de formulaire
        return redirect(url_for('lb_list'))
    else:
        return render_template('lb.create.html') #Page création lb

# Route pour supprimer un Load Balancer
@app.route('/lb/<id>', methods=['DELETE'])
def lb_delete(id):
    # Supprimer le Load Balancer avec l'ID spécifié
    return 'Load Balancer ' + id + ' supprimé'

#REVERSE PROXY

# Route pour la liste des Reverse Proxy
@app.route('/rp/list')
def rp_list():
    return 'Liste des Reverse Proxy'
    #return render_template('rp.list.html')

# Route pour afficher la configuration d'un Reverse Proxy en particulier
@app.route('/rp/<id>')
def rp_config(id):
    return 'Configuration du Reverse Proxy ' + id

# Route pour créer un nouveau Reverse Proxy
@app.route('/rp/create', methods=['GET', 'POST'])
def rp_create():
    if request.method == 'POST':
        # Traitement des données de formulaire
        return redirect(url_for('rp_list'))
    else:
        return render_template('rp.create.html') #Page création rp

# Route pour supprimer un Reverse Proxy
@app.route('/rp/<id>', methods=['DELETE'])
def rp_delete(id):
    # Supprimer le Reverse Proxy avec l'ID spécifié
    return 'Reverse Proxy ' + id + ' supprimé'

#WEB SERVER

# Route pour la liste des serveurs Web
@app.route('/ws/list')
def ws_list():
    #return 'Liste des serveurs Web'
    return render_template('alias.html')

# Route pour afficher la configuration d'un serveur Web en particulier
@app.route('/ws/<id>')
def ws_config(id):
    return 'Configuration du serveur Web ' + id

# Route pour créer un nouveau serveur Web
@app.route('/ws/create', methods=['GET', 'POST'])
def ws_create():
    if request.method == 'POST':
        # Traitement des données de formulaire
        return redirect(url_for('ws_list'))
    else:
        return render_template('ws_create.html') #Créer un serveur web

# Route pour supprimer un serveur Web
@app.route('/ws/<id>', methods=['DELETE'])
def ws