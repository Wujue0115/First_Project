


let search_button = document.getElementById("search-button");
let search_text = document.getElementById("search-text");



search_button.onclick = function(){
    axios.post("http://127.0.0.1:3000/find_order", {
        id: search_text.value
    }).then(
        function(response){
            console.log(response.data);
        }
    )
}