let url = 'datos_sin_saltos.json'

fetch(url)
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data[1322].TEL)
        for(let i in data) {
            try {
                // console.log(data[i].FN +' numero ' + i)
                
            } catch (error) {
                console.log(error)
            }
            const newItem = document.createElement('li');
            const newContent = document.createTextNode(`N: ${data[i].FN} TEL :${data[i].TEL}`);
            newItem.appendChild(newContent)
            url.appendChild(newItem)
        }
        // console.log(data)
    })
    .catch(err => {
        console.log(err)
    })