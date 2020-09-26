d3.request("http://127.0.0.1:5000/allbreeds").get(response => {
    console.log(JSON.parse(response.response));

})