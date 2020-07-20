function addBootstrapClass() {

    let campos = [
        document.getElementById("id_nome"),
        document.getElementById("id_marca"),
        document.getElementById("id_descricao"),
        document.getElementById("id_quantidade"),
        document.getElementById("id_preco"),
        document.getElementById("id_usuario"),
        document.getElementById("id_status")
    ]

    for(let i = 0; i < campos.length; i++){
        if (campos[i].classList) campos[i].classList.add('form-control')
        else campos[i].className += 'form-control'
    }
}
addBootstrapClass()