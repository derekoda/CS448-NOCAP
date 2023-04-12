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

