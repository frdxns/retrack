async function carregar() {
  const username = "frdxns";
  const resposta = await fetch(`api/toplastfm/${username}`);

  const respostajson = await resposta.json();
  tops = JSON.parse(respostajson);

  topartistas = tops[0].artistas;
  topmusicas = tops[1].musicas;
  topalbuns = tops[2].albuns;

  campo_artistas = document.querySelector("#rankartistas");
  campo_musicas = document.querySelector("#rankmusicas");
  campo_albuns = document.querySelector("#rankalbuns");
  const imagem_destaque = document.querySelector("#imagemmusica");

  imagem_destaque.src = topmusicas[1].imagem;

  topartistas.forEach(artista => {
    const lista = document.createElement("li");
    lista.innerText = artista.titulo;

    campo_artistas.appendChild(lista);
  });

  topmusicas.forEach(musica => {
    const lista = document.createElement("li");
    lista.innerText = musica.titulo;

    campo_musicas.appendChild(lista);
  });

  topalbuns.forEach(album => {
    const lista = document.createElement("li");
    lista.innerText = album.titulo;

    campo_albuns.appendChild(lista);

    const carregar = document.querySelector("#carregando");
    const conteudo = document.querySelector(".container");

    carregar.style.display = "none";
    conteudo.style.display = "grid";
  });
}

document.addEventListener("DOMContentLoaded", carregar);
