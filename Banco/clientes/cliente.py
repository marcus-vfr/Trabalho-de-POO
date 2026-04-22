class Cliente:
    _contador = 1

    def __init__(self, nome):
        self._id = Cliente._contador
        Cliente._contador += 1

        self._nome = nome

    # Getters (Encapsulation)
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def __str__(self):
        return f"{self._nome} (ID: {self._id})"