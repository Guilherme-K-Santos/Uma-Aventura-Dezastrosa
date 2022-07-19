from persistencia.DAO import AbstractDAO
from entidades.usuario import Usuario


class UsuarioDAO(AbstractDAO):
    def __init__(self):
        super().__init__("usuarios.pkl")

    def add(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario):
            super().add(usuario.login, usuario)

    def get(self, login_usuario: str):
        if login_usuario is not None and isinstance(login_usuario, str):
            return super().get(login_usuario)

    def remove(self, login_usuario: str):
        if login_usuario is not None and isinstance(login_usuario, str):
            return super().remove(login_usuario)

