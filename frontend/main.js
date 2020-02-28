let url = '../datos_sin_saltos.json'

fetch(url)
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data[1322].TEL)
        const url = document.querySelector('.box');
        for(let i in data) {
            try {
                const newItem = document.createElement('li');
                const newContent = document.createTextNode(`Nombre: ${data[i].FN} TEL :${data[i].TEL}`);
                newItem.appendChild(newContent)
                url.appendChild(newItem)
            } catch (error) {
                console.log(error)
            }
        }
    })
    .catch(err => {
        console.log(err)
    })