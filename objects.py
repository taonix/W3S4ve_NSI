class Piece:
    def __init__(self, id, name, content):
        self.id = id
        self.name = name
        self.content = content


class Object:
    def __init__(self, name, description, text_to_introduce, count):
        self.name = name
        self.description = description
        self.text_to_introduce = text_to_introduce
        self.count = count


# Inventory

inventaire = []

# Création des objets

lampe = Object(
    "Lampe Torche",
    "Simple lampe torche déchargé",
    """Vous trouvez une Lampe Torche posée au sol. 
            Elle ne semble plus fonctionner. Vous décidez de 
            la prendre avec vous.""",
    1
)

carte = Object(
    "Carte",
    "Une carte de locaux",
    """Vous trouvez une carte juste en dessous. Elle semble
    abîmé mais vous pouvez encore la lire. Il s'agit d'une partie
    de plans des locaux de tootale.""",
    1
)

pile = Object(
    "Pile",
    "Pile de 5V",
    """Au détour d'un tas dossiers vous trouvez une pile qui semble être fonctionnelle. 
            Vous decidez de l'utilser pour reparer votre lampe.""",
    1
)

clef_USB = Object(
    "Clef USB",
    "Clef USB contenant les documents confidentiels",
    """En explorant cette nouvelle pièce, vous faites face à un dossier mystérieux. En l'ouvrant vous trouvez une clef USB. Elle semble contenir des documents confidentiels que vous cherchez""",
    1
)

papier = Object(
    "Papier",
    "Papier blanc avec des traces de crayon. Vous lisez : 59**",
    """Par terre se trouve aussi un bout de papier blanc avec des traces de crayon. Vous lisez : 59**""",
    1
)

document = Object(
    "Document",
    "Document vierge à l'exeption d'une donnée censuré en son centre : **85",
    """Vous trouvez dans l'encolure d'une fenêtre un document vierge à l'exeption d'une donnée censuré en son centre : **85""",
    1
)
