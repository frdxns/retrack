async function carregar() {
  const username = "frdxns";
  const resposta = await fetch(`api/toplastfm/${username}`);

  const respostajson = await resposta.json();
  tops = JSON.parse(respostajson);

  topartistas = tops[0].artistas;
  topmusicas = tops[1].musicas;
  topalbuns = tops[2].albuns;
  recentes = tops[3].recente;

  const campo_artistas = document.querySelector("#rankartistas");
  const campo_musicas = document.querySelector("#rankmusicas");
  const campo_albuns = document.querySelector("#rankalbuns");
  const imagem_destaque = document.querySelector("#imagemmusica");
  const nome_destaque = document.querySelector(".rec-nome");
  const recente = document.querySelector("#stk-dias");

  imagem_destaque.src = topmusicas[1].imagem;
  nome_destaque.innerText = topmusicas[0].titulo;

  if (recentes.tocando == true) {
    recente.innerText = `Tocando Agora: ${recentes.titulo} - ${recentes.artista}`;
  } else {
    recente.innerText = `Última Reprodução: ${recentes.titulo} - ${recentes.artista}`;
  }

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
