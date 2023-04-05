function searchMedicine() {
    var medicineName = document.getElementById("medicine_name").value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var resultContainer = document.getElementById("result-container");
        var data = JSON.parse(this.responseText);
        if (data.hasOwnProperty("error")) {
          resultContainer.style.display = "block";
          resultContainer.innerHTML = "<h2>Error</h2><p>" + data.error + "</p>";
        } else {
          resultContainer.style.display = "block";
          resultContainer.innerHTML = "<h2>" + data.name + "</h2><p>Usage: " + data.usage + "</p><p>Side Effects: " + data.side_effects + "</p>";
        }
      }
    };
    xhttp.open("GET", "search.php?medicine_name=" + medicineName, true);
    xhttp.send
}