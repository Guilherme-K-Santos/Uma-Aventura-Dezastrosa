from persistencia.DAO import AbstractDAO
from entidades.usuario import Usuario


class UsuarioDAO(AbstractDAO):

    __instance = None

    def __init__(self):
        super().__init__("usuarios.pkl")

    def __new__(cls):
        if UsuarioDAO.__instance == None:
            UsuarioDAO.__instance = object.__new__(cls)
        return UsuarioDAO.__instance

    def add(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario):
            super().add(usuario.login, usuario)
        else:
            return None

    def get(self, login_usuario: str):
        if login_usuario is not None and isinstance(login_usuario, str):
            return super().get(login_usuario)

    def remove(self, login_usuario: str):
        if login_usuario is not None and isinstance(login_usuario, str):
            return super().remove(login_usuario)
