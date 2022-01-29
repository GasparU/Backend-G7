import { tipoProductoService } from "../services/tipoProducto.service.js";

export async function crearTipoProducto(req, res) {
  tipoProductoService.crearTipoProducto({
    nombreProducto: "",
    usuarioId: "",
  });
  return res.json(resultado);
}
