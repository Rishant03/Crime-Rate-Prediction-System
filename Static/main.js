//  window.onload = function () {
//      //Reference the DropDownList.
//      var year = document.getElementById("year-dropdown");

//     //Loop and add the Year values to DropDownList.
//     for (var i = 2000; i <= 2050; i++) {
//         var option = document.createElement("OPTION");
//         option.innerHTML = i;
//         option.value = i;
//         year.appendChild(option);
//     }
// };


window.onload = function () {
    // Reference the dropdown element
    var year = document.getElementById("year-dropdown");

    // Populate years from 2000 to 2050
    for (var i = 2000; i <= 2050; i++) {
        var option = document.createElement("option");
        option.textContent = i;
        option.value = i;
        year.appendChild(option);
    }
};
