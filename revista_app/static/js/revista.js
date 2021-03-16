window.onload = (event) => {
    //ajustar_margenes();
};

ajustar_margenes = () => {
    const hijos = document.querySelector('.pie').querySelectorAll('a');
    const cols = document.querySelector(".pie").querySelectorAll(".row");
    hijos.forEach((nodo) => {
        const altura = nodo.parentElement.clientHeight;
        const pad = Math.round((altura - nodo.offsetHeight) / 2);
        nodo.style.marginTop = pad + "px"
    });
}