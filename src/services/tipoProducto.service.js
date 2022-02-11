import { prisma } from "../prisma.js";

export class tipoProductoService {
  static async crearTipoProducto({ nombre }) {
    const nuevoTipoProducto = await prisma.tipoProducto.create({
      data: {
        nombre,
      },
    });

    console.log(usuarioEncontrado);

    return { content: nuevoTipoProducto };
  }
  static async listTipoProducto() {}
}
