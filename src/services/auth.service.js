import { prisma } from "../prisma.js";
import { compareSync } from "bcrypt";
import jwt from "jsonwebtoken"; //esta libreria es para generar token

export class AuthServise {
  static async login({ correo, password }) {
    // SELECT password, tipo_usuario FROM USUARIO WHERE correo=...;
    // si no lo encuentra lanzara un error en el found
    const usuarioEncontrado = await prisma.usuario.findUnique({
      where: { correo },
      select: { password: true, TipoUsuario: true, id: true },
      rejectOnNotFound: true,
    });

    const resultado = compareSync(password, usuarioEncontrado.password);

    if (resultado === true) {
      const token = jwt.sign(
        { id: usuarioEncontrado.id, mensaje_oculto: "Hola, soy un mensaje" },
        "ArribaPeru",
        { expiresIn: "120" }
      );
      //se puede pasar un valor numerico (que pueden ser segundos) o un string indicando el formato de la siguiente manera "7d" (7 dias) "10h" (10 horas) 2days (2 días) si le ponemos "100" encontes sera un valor expresado en milisegundos. Para poner 1 minuto, se pone "60" si se quiere 2 minutos se pondra "120"
      return { message: "Sí es el usuario" };
    } else {
      return { message: "Credenciales incorrectas" };
    }
  }
}
