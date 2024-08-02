const btn = document.querySelector('#id_create')

const opcion = document.querySelector('#Pais')

async function getPais(){
  const res = await fetch('http://localhost:8000/myapp/data/pais')
  const data = await res.json();

  data.forEach(items => {
    opcion.innerHTML += `<option value=${items.IdPais}>${items.Nombre}</option>`
  });
}


getPais()