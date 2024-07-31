const btn = document.querySelector('#btn')

const form = document.querySelector("#id_form")
const opcion = document.querySelector('#id_Pais')

async function getPais(){
  const res = await fetch('http://localhost:8000/myapp/data/pais')
  const data = await res.json();

  data.forEach(items => {
    opcion.innerHTML += `<option value=${items.IdPais}>${items.Nombre}</option>`
  });
}

getPais()
