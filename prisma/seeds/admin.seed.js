import { hashSync } from "bcrypt";

export default async (prisma) => {
  const password = hashSync("Welcome123!", 10);

  await prisma.usuario.upsert({
    create: {
      nombre: "Jose",
      correo: "sainc2016@gmail.com",
      password,
      TipoUsuario: "ADMIN",
    },
    update: {
      password,
    },
    where: {
      // solamente se pueden declarar las columnas que sean unicas (unique) o las pk
      correo: "sainc2016@gmail.com",
    },
  });
};
