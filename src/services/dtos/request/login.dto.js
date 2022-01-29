import validator from "validator";

export function loginDto({ correo, password }) {
  // isStrongPassword => longitud minima 8 caracteres, al menos una mayuscula, al menos una minuscula, al menos un numero, al menos un simbolo
  //   el validador hace la validacion siempre y cuando sea un string, sino es un string, emitira un error pero la validacion retornara un booleano
  if (!validator.isEmail(correo)) {
    throw Error("El correo debe ser un correo válido");
  }
  if (!validator.isStrongPassword(password)) {
    throw Error(
      "La contraseña no es lo suficientemente segura, debe tener al menos una Mayuscula, una minuscula, un numero, un simbolo y una longitud minima de 8 caracteres"
    );
  }
  return { correo, password };
}
