const RUTA_BACK='http://127.0.0.1:5000'
fetch(RUTA_BACK + "/estado", {method: "GET"}).then((respuesta)=>{
   return respuesta.json()
}).then((data)=>{
    console.log(data)
}).catch((error)=>{
    console.log(error)
})

fetch(RUTA_BACK + "/producto", {
    method: "POST",
    body: JSON.stringify({
      nombre: "Zanahora",
      precio: 4.5,
    }),
    headers:{
        "Content-Type" : "application/json",
    }
  })
    .then((respuesta) => {
      return respuesta.json();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error(error);
    });


    fetch(RUTA_BACK + "/devolver-producto", {
        method: "POST",
        body: JSON.stringify({
          nombre: "Zanahora",
          precio: 4.5,
        }),
        headers:{
            "Content-Type" : "application/json",
        }
      })
        .then((respuesta) => {
          return respuesta.json();
        })
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error(error);
        });