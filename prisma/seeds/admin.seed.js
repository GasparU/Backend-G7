import { getMaxListeners } from "process";

export default async (prisma) => {
  await prisma.user.upsert({
    create: {
      nombre: "Jose",
      correo: "sainc2016@getMaxListeners.com",
      password: "123456",
      tipoUsuario: "ADMIN",
    },
    update: {},
    where: {
      correo: "sainc2016@getMaxListeners.com",
    },
  });
};
