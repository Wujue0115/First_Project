


let orders_table = document.getElementById("orders-table");
let search_button = document.getElementById("search-button");
let delete_button = document.getElementById("delete-button");
let search_text = document.getElementById("search-text");

function push_back_table_row(data){
    let row = orders_table.insertRow(orders_table.rows.length);
    row.insertCell(0).innerHTML = data["_id"].toString();
    row.insertCell(1).innerHTML = data["name"].toString();
    row.insertCell(2).innerHTML = data["commodity"].toString();
    row.insertCell(3).innerHTML = data["price"].toString();
    row.insertCell(4).innerHTML = data["status"].toString();
}

function delete_all_table_row(){
    while(orders_table.rows.length > 1){
        orders_table.deleteRow(1);

    }
}


search_button.onclick = function(){
    axios.post("http://127.0.0.1:3000/find_order", {
        id: search_text.value
    }).then(
        function(response){
            data = response.data["orders"];
            for(let i=0; i<data.length; ++i){
                push_back_table_row(data[i]);
            }
        }
    )
}

delete_button.onclick = function(){
    delete_all_table_row();
}