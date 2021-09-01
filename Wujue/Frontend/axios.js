


let search_button = document.getElementById("search-button");
let search_id = document.getElementById("text-id");
let serach_name = document.getElementById("text-name");

const order_block = document.getElementById("order-block");

function check(obj){
    console.log(obj);
    console.log("hello");
    console.log(this.innerText);
}

function getNewFirstProperty(i){
    const property = document.createElement("div");
    const checkbox = document.createElement("div");
    const checkbox_text = document.createElement("div");

    property.className = "first-property";
    checkbox.className = "checkbox-div";
    checkbox_text.className = "checkbox-text";
    // checkbox_text.id = "checkbox-id" + i;
    checkbox_text.innerText = "\u2713";
    checkbox_text.style.display = "block";
    checkbox_text.onclick = check();
    checkbox.appendChild(checkbox_text);
    property.appendChild(checkbox);
    return property;
}

function getNewProperty(text){
    const property = document.createElement("div");
    property.className = "property";
    property.innerText = text;
    return property;
}

function getNewTimeProperty(text){
    const property = document.createElement("div");
    property.className = "time-property";
    property.innerText = text;
    return property;
}

function insertNewOrder(i, data){
    const order_div = document.createElement("div");
    order_div.className = "order-div";
    order_div.value = (i + 1).toString;
    order_div.style.boxShadow = "none";
    order_div.style.borderBottom = "2px solid #000";
    // order_div.style.boxShadow = "1px 1px 2px 0px #000";
    order_div.style.height = "40px";
    
    order_div.appendChild(getNewFirstProperty(i));
    order_div.appendChild(getNewProperty(data["_id"].toString()));
    order_div.appendChild(getNewProperty(data["name"].toString()));
    order_div.appendChild(getNewTimeProperty(data["time"].toString()));
    order_div.appendChild(getNewProperty(data["commodity"].toString()));
    order_div.appendChild(getNewProperty("$ " + data["price"].toString()));
    order_div.appendChild(getNewProperty(data["status"].toString()));
    order_block.appendChild(order_div);
}

function clearTableData(){
    while(order_block.childElementCount > 1){
        order_block.removeChild(order_block.lastChild);
    }
}


search_button.onclick = function(){
    axios.post("http://127.0.0.1:3000/find_order", {
        id: search_id.value,
        name: serach_name.value
    }).then(
        function(response){
            clearTableData();
            data = response.data["orders"];
            console.log("Query data counts: " + data.length);
            for(let i=0; i<data.length; ++i){
                insertNewOrder(i, data[i]);
            }
        }
    )
}



