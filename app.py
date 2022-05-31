from flask import *
from templates import *
from objects import *

app = Flask(__name__)


@app.route('/')
def main():  # put application's code here
    return render_template('index.html', header=header('index'), footer=footer)


################################################################################
#                                Tootale                                       #
################################################################################

tootale_hall = Piece(
    "hall",
    "Hall D'entrée",
    [
        lampe,
        carte
    ]
) # création de la pièce
@app.route(f"/tootale_{tootale_hall.id}")
def mission_hall():  # déclaration de la fonction
    return render_template(f'./tootale/{tootale_hall.id}.html', header=header(f'/tootale/{tootale_hall.id}'), footer=footer, piece=tootale_hall, inventaire=inventaire) # affichage de la page


tootale_cage_escalier = Piece(
    "cage_escalier",
    "Cage d'escalier",
    [

    ]
) # création de la pièce
@app.route(f"/tootale_{tootale_cage_escalier.id}")
def mission_cage_escalier():  # déclaration de la fonction
    return render_template(f'./tootale/{tootale_cage_escalier.id}.html', header=header(f'/tootale/{tootale_cage_escalier.id}'), footer=footer, piece=tootale_cage_escalier, inventaire=inventaire) # affichage de la page


tootale_cave = Piece(
    "cave",
    "Cave de tootale",
    [
        clef_USB,
        papier
    ]
) # création de la pièce
@app.route(f"/tootale_{tootale_cave.id}")
def mission_cave():  # déclaration de la fonction
    return render_template(f'./tootale/{tootale_cave.id}.html', header=header(f'/tootale/{tootale_cave.id}'), footer=footer, piece=tootale_cave, inventaire=inventaire) # affichage de la page


tootale_pause = Piece(
    "pause",
    "Salle de pose",
    [
        document,
        pile
    ]
) # création de la pièce
@app.route(f"/tootale_{tootale_pause.id}")
def mission_pause():  # déclaration de la fonction
    return render_template(f'./tootale/{tootale_pause.id}.html', header=header(f'/tootale/{tootale_pause.id}'), footer=footer, piece=tootale_pause, inventaire=inventaire) # affichage de la page

tootale_serveurs_porte = Piece(
    "serveurs_porte",
    "Porte de la salle des serveurs",
    [

    ]
) # création de la pièce
@app.route(f"/tootale_{tootale_serveurs_porte.id}")
def mission_serveurs_porte():  # déclaration de la fonction
    return render_template(f'./tootale/{tootale_serveurs_porte.id}.html', header=header(f'/tootale/{tootale_serveurs_porte.id}'), footer=footer, piece=tootale_serveurs_porte, inventaire=inventaire) # affichage de la page

tootale_serveurs = Piece(
    "serveurs",
    "Salle des serveurs",
    [

    ]
) # création de la pièce
@app.route(f"/tootale_{tootale_serveurs.id}", methods=['POST'])
def mission_serveurs():  # déclaration de la fonction
    if request.form['code'] == '5985': # si le code est bon
        return render_template(f'./tootale/{tootale_serveurs.id}.html', header=header(f'/tootale/{tootale_serveurs.id}'), footer=footer, piece=tootale_serveurs, inventaire=inventaire) # affichage de la page
    else: # sinon
        return render_template(f'./tootale/{tootale_serveurs_porte.id}.html', header=header(f'/tootale/{tootale_serveurs_porte.id}'), footer=footer, piece=tootale_serveurs_porte, inventaire=inventaire)  # affichage de la page


tootale_mystere_porte = Piece(
    "mystere_porte",
    "Porte fermée",
    [

    ]
) # création de la pièce
@app.route(f"/tootale_{tootale_mystere_porte.id}")
def mission_mystere_porte():  # déclaration de la fonction
    return render_template(f'./tootale/{tootale_mystere_porte.id}.html', header=header(f'/tootale/{tootale_mystere_porte.id}'), footer=footer, piece=tootale_mystere_porte, inventaire=inventaire) # affichage de la page


tootale_mystere = Piece(
    "mystere",
    "Porte fermée",
    [

    ]
) # création de la pièce
@app.route(f"/tootale_{tootale_mystere.id}", methods=['POST'])
def mission_porte():  # déclaration de la fonction
    if request.form['code'] == '1854':  # si le code est bon
        return render_template(f'./tootale/{tootale_mystere.id}.html', header=header(f'/tootale/{tootale_mystere.id}'), footer=footer, piece=tootale_mystere, inventaire=inventaire) # affichage de la page
    else: # sinon
        return render_template(f'./tootale/{tootale_mystere_porte.id}.html', header=header(f'/tootale/{tootale_mystere_porte.id}'), footer=footer, piece=tootale_mystere_porte, inventaire=inventaire)  # affichage de la page


if __name__ == '__main__':
    app.run(debug=True) # démarrage de l'application
