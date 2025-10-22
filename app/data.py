import random

POKENEAS = [
    {
        "id": 1,
        "nombre": "Leoncini",
        "altura": 1.6,
        "habilidad": "Amigo de lo ajeno",
        "imagen_key": "Leoncini.png",
        "frase": "Las cosas no son del dueño, son de quien las necesita."
    },
    {
        "id": 2,
        "nombre": "Grillachu",
        "altura": 1.5,
        "habilidad": "Farra infinita",
        "imagen_key": "Grillachu.png",
        "frase": "Sonríe, que la vida es un soplo."
    },
    {
        "id": 3,
        "nombre": "Mozita",
        "altura": 1.4,
        "habilidad": "Dañar hogares",
        "imagen_key": "Mozita.png",
        "frase": "Cada quien cuida lo que le interesa y descuida lo que le estorba."
    },
    {
        "id": 4,
        "nombre": "Barbie",
        "altura": 0.6,
        "habilidad": "Recuperación rápida",
        "imagen_key": "Barbie.png",
        "frase": "Tú puedes ser lo que quieras ser."
    },
    {
        "id": 5,
        "nombre": "Bancolombio",
        "altura": 1.0,
        "habilidad": "Cabello inmóvil",
        "imagen_key": "Bancolombio.png",
        "frase": "¿Quieres ser tu propio jefe?"
    },
    {
        "id": 6,
        "nombre": "Dineroviejo",
        "altura": 1.2,
        "habilidad": "Evadir impuestos",
        "imagen_key": "Dineroviejo.png",
        "frase": "El que es pobre, es pobre porque quiere."
    },
    {
        "id": 7,
        "nombre": "Alternito",
        "altura": 0.9,
        "habilidad": "Diseñar interactivamente",
        "imagen_key": "Alternito.png",
        "frase": "Hay personas que se odian, porque un día se quisieron."
    },
    {
        "id": 8,
        "nombre": "Undergolio",
        "altura": 1.8,
        "habilidad": "Ser original",
        "imagen_key": "Undergolio.png",
        "frase": "Si no es oversized, ahí no es."
    }
]

def random_pokenea():
    return random.choice(POKENEAS)