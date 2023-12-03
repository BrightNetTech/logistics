function validateForm(){
    var Customer_NameName = document.getElementById("Customer_Name").value = '';
    var Origin = document.getElementById("Origin").value = '';
    var Destination = document.getElementById("Destination").value = '';
    var Phone_Number = document.getElementById("Phone_Number").value = '';
    var Email = document.getElementById("Email").value = '';
    var Mode_of_Payment = document.getElementById("Mode_of_Payment").value = '';
    var Service = document.getElementById("Service").value = '';

    if(Customer_Name == ""){
        alert("Customer_Name is required");
        return false;
    }
    
    if(Origin == ""){
        alert("Origin is required");
        return false;
    }
    
    if(Destination == ""){
        alert("Destination is required");
        return false;
    }
    
    if(Phone_Number == ""){
        alert("Phone_Number is required");
        return false;
    }
    
    if(Email == ""){
        alert("Email is required");
        return false;
    }

    else if(!Email.includes("@")){
        alert("Invalid email address");
        return false;

    }
       
    if(Mode_of_Payment == ""){
        alert("Mode_of_Payment is required");
        return false;
    }
    
    if(Service == ""){
        alert("Service is required");
        return false;
    }
    return true;
}

function showData(){
    var servicelist;
    if(localStorage.getItem("servicelist") ==null){
        servicelist = [];
    }
    else{
        servicelist = JSON.parse(localStorage.getItem("servicelist"));
    }
    var html = "";
    servicelist.forEach(function (element, index){
        html += "<tr>";
        html += "<td>" + element.Customer_Name + "</td>";
        html += "<td>" + element.Origin + "</td>";
        html += "<td>" + element.Destination + "</td>";
        html += "<td>" + element.Phone_Number + "</td>";
        html += "<td>" + element.Email + "</td>";
        html += "<td>" + element.Mode_of_Payment + "</td>";
        html += "<td>" + element.Service + "</td>";
        html += '<td><button onclick="deleteData('+index+')"class="btn btn-danger>Delete</button><button onclick="updateData('+index+')"class="btn btn-warning>Edit</button></td>';
        html += "</tr>";
    });
    document.querySelector("#servicelist tbody").innerHTML = html;
}


// load ALL data when document or page is loaded
document.onload = showData();

function AddData(){
    
}

var selectedRow = null();
function OnFormSubmit(){
    event.preventDefault();
    var formData = readFormData();
    if(selectedRow === null){
        insertNewRecord(formData);
    }
    else{
        updateRecord(formData)

    }
    resetForm();

}

//Retrieve the data
function readFormData(){
    var formData = {};
formData["Customer Name"] = document.getElementById("Customer name").value;
formData["Origin"] = document.getElementById("Origin").value;
formData["Destination"] = document.getElementById("Destination").value;
formData["Phone Number"] = document.getElementById("Phone Number").value;
formData["Email"] = document.getElementById("Email").value;
formData["Mode of Payment"] = document.getElementById("Mode of Payment").value;
formData["Service"] = document.getElementById("Service").value;
return formData;
}

//insert the data
function insertNewRecord(){
    var table = document.getElementById("servicelist").getElementsByTagName("tbody")[0];
    var newRow = table.insertRow(table.length);
    var cell0 = newRow.insertCell(0);
        cell0.innerHTML = data.Customer_Name
    var cell1 = newRow.insertCell(1);
        cell1.innerHTML = data.Origin
    var cell2 = newRow.insertCell(2);
        cell2.innerHTML = data.Destination
    var cell3 = newRow.insertCell(3);
        cell3.innerHTML = data.Phone_Number
    var cell4 = newRow.insertCell(4);
        cell4.innerHTML = data.email
    var cell5 = newRow.insertCell(5);
        cell5.innerHTML = data.Mode_of_Payment
    var cell6 = newRow.insertCell(6);
        cell6.innerHTML = data.Service
    var cell7 = newRow.insertCell(7);
        cell7.innerHTML = '<button onClick='onEdit(this)'>Edit</button> <button onClick='onDelete(this)'>Delete</button>'
    }

//edit the data
function onEdit(td){
    selectedRow = td.parentElement.parentElement;
    document.getElementById("Customer_Name").value = selectedRow.cells[0].innerHTML;
    document.getElementById("Origin").value = selectedRow.cells[1].innerHTML;
    document.getElementById("Destination").value = selectedRow.cells[2].innerHTML;
    document.getElementById("Phone_Number").value = selectedRow.cells[3].innerHTML;
    document.getElementById("Email").value = selectedRow.cells[4].innerHTML;
    document.getElementById("Mode_of_Payment").value = selectedRow.cells[5].innerHTML;
    document.getElementById("Service").value = selectedRow.cells[6].innerHTML;
}

function updateRecord(){
    selectedRow.cells.innerHTML[0] = formData.Customer_Name;
    selectedRow.cells.innerHTML[1] = formData.Origin;
    selectedRow.cells.innerHTML[2] = formData.Destination;
    selectedRow.cells.innerHTML[3] = formData.Phone_Number;
    selectedRow.cells.innerHTML[4] = formData.Email;
    selectedRow.cells.innerHTML[5] = formData.Mode_of_Payment;
    selectedRow.cells.innerHTML[6] = formData.Service;
}

//delete the data
function onDelete(td){
    if(confirm('Do you want to delete this record??')){
        row = td.parentElement.parentElement;
        document.getElementById("servicelist").deleteRow(row.rowIndex);
    }
    resetForm();
}

//Reset the data
function resetForm(){
    selectedRow = td.parentElement.parentElement;
    document.getElementById("Customer_Name").value = '';
    document.getElementById("Origin").value = '';
    document.getElementById("Destination").value = '';
    document.getElementById("Phone_Number").value = '';
    document.getElementById("Email").value = '';
    document.getElementById("Mode_of_Payment").value = '';
    document.getElementById("Service").value = '';
}