import { tipoProductoService } from "../services/tipoProducto.service.js";

export async function crearTipoProducto(req, res) {
  const resultado = await tipoProductoService.crearTipoProducto({
    nombreProducto: "",
    usuarioId: 1,
  });
  return res.status(201).json(resultado);
}
