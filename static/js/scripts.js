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

  var prereqClassArray

  $(document).ready(function () {
    // Get a reference to the dialog box
    var dialog = $("#dialog");

    // Hide the dialog box by default
    dialog.hide();

    // Add a mouseover event listener to each course heading
    $(".level-4-box").mouseover(function () {
        // Get the course ID from the data attribute
        var courseId = $(this).data("course-id");

        // Send an AJAX request to the server to get the course info
        $.ajax({
            url: "/get_course_info?course_id=" + courseId,
            method: "GET",
            data: { course_id: courseId },
            success: function (response) {

                if(response.prereq) {
                  console.log(response.prereq);


                  prereqClassArray = response.prereq.split(', ');
                  console.log(`Array: ${prereqClassArray}`);
                  for(let i =0; i < prereqClassArray.length; i++) {

                    console.log(`Element at i: ${prereqClassArray[i]}`)
                    document.getElementById(prereqClassArray[i]).style.backgroundColor = 'green';
                  }

                }


                // Set the dialog box content to the course info
                dialog.html("<h5>Course Name</h5>"+response.name + "<br><br><strong>Description:</strong><br>"+response.description + "<br><br><strong>Prerequisites:</strong><br><br>" + response.prereq);

                // Show the dialog box
                dialog.show();
            },
            error: function (xhr, status, error) {
                console.error("Error loading course info: " + error);
            }
        });
    });

    // Add a mouseout event listener to hide the dialog box when the user moves the mouse away from a course heading
    $(".level-4-box").mouseout(function () {
        dialog.hide();
        for(let i =0; i < prereqClassArray.length; i++) {

          console.log(`Element at i: ${prereqClassArray[i]}`)
          document.getElementById(prereqClassArray[i]).style.backgroundColor = '#9c1f32';
        }
    });

});

function playSound() {
  // Create an audio element and set its source to the sound file
  var audio = new Audio('');
  // Play the audio file
  audio.play();
}





