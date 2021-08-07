function add(){
    let name=document.querySelector("#name").value;
    let place=document.querySelector("#place").value;
     console.log(`${name} ${place}`);
     document.querySelector("#h").innerText=`${name} ${place}`;
}