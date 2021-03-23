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

getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

grabar_suscripcion = (form) => {
    console.log(this);
    const correo = form['email'].value;
    const myRequest = new Request('/suscripcion', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({email: correo})
    });
    fetch(myRequest)
        .then(response => {
            if (response.status === 200) {
                return response.json()
            }
        })
        .then(function (data) {
            console.log(data);
            form["email"].value = ""
            form["email"].placeholder = data.resultado
        })
        .catch(err => {
            console.log(err)
        })
    return false;
}
