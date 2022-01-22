import express, { json } from "express";
import { categoriaRouter } from "./routes/categoria.routes.js";

const app = express();
//nullish coalesching operator
//valida el contenido de la izquierda y si es nulo o undefined entonces procedera tomar el valor de la derecha
const PORT = process.env.PORT ?? 3000;

//declarar el tipo de contenido que va a recibir
app.use(json());
//declaramos las rutas de nuestros archivos routes
app.use(categoriaRouter);

app.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
