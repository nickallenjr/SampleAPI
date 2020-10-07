//Example route for sending data along with route that's not in the url
// d3.request("http://127.0.0.1:5000/loadDB").send("POST","Alpha", response => {
//     console.log(response);

// })

document.addEventListener("DOMContentLoaded", (event) => {
    Swal.fire({
        title: 'Error!',
        text: 'Do you want to continue',
    })
});


  

d3.request("/loadDB/").get(res => {
    console.log('DB Loaded Successfully');

    d3.request("/allbreeds/").get(allBreedsData => {
        console.log(JSON.parse(allBreedsData.response));
    })
})