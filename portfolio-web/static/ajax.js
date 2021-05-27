async function goToPage(url) {
    let xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            // change url
            const newUrl = window.location.protocol + '//' + window.location.host + url;
            window.history.pushState(null, null, newUrl);

            // change page
            let response = JSON.parse(xhttp.responseText);
            document.querySelector('header h4').innerHTML = response['title']
            document.querySelector('main').innerHTML = response['html']
        }
    };

    xhttp.open('get', url + '?spa=true', true);
    xhttp.send(null);
}
