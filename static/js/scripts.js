// The following are scripts used as interactions on the front end


function myFunction(){

    const xhttp = new XMLHttpRequest();

    const courseName = document.getElementById("172").id;

    xhttp.onload = function() {
      document.getElementById("172").innerHTML = "this works.";

      if (xhttp.status == 200 && this.readyState == 4) {
        console.log(xhttp.responseText);
      }

    }
    xhttp.open("GET", "/course?id=" + courseName, true);
    xhttp.send();

  }

  // this function is currently dog shit and does not work because 
  // I don't know JS
  function genSchedule() {
    const xhttp = new XMLHttpRequest();

    const schedule1 = document.getElementById("schedule1");
    const schedule2 = document.getElementById("schedule2");

    xhttp.onload = function() {
      if (xhttp.status == 200 && this.readyState == 4) {
        console.log(xhttp.responseText);
        schedule1.innerHTML = xhttp.responseText;
        schedule2.innerHTML = xhttp.responseText;
      }
    }
    xhttp.open("GET", "/schedule", true);
    xhttp.send();

  }

