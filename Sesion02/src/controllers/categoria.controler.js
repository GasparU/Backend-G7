import { Prisma } from "../prisma.js";

export const crearCategoria = async (req, res) => {
  // req.body => {nombre: 'Lacteos'}
  const data = req.body;
  const content = await Prisma.categoria.create({ data });
  return res.json({ content });
};

export const listaCategoria = async (req, res) => {
  const categorias = await Prisma.categoria.findMany({});

  return res.json({ content: categorias });
};
