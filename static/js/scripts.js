// The following are scripts used as interactions on the front end
function myFunction() {
  const xhttp = new XMLHttpRequest();

  const courseName = document.getElementById("172").id;

  xhttp.onload = function () {
    document.getElementById("172").innerHTML = "this works.";

    if (xhttp.status == 200 && this.readyState == 4) {
      console.log(xhttp.responseText);
    }
  };
  xhttp.open("GET", "/course?id=" + courseName, true);
  xhttp.send();
}

var prereqClassArray;
var globalCourseID;

$(document).ready(function () {
  // Get a reference to the dialog box
  var dialog = $("#dialog");

  // Hide the dialog box by default
  //dialog.hide();

  // Add a mouseover event listener to each course heading
  $(".class-list-item").mouseover(function () {
    // Get the course ID from the data attribute
    var courseId = $(this).data("course-id");
    globalCourseID = courseId;

    // Send an AJAX request to the server to get the course info
    $.ajax({
      url: "/get_course_info?course_id=" + courseId,
      method: "GET",
      data: { course_id: courseId },
      success: function (response) {
        // first check if courses have data
        document.getElementById("resc-lnks").style.display = "none";
        if (response.description) {
          document.getElementById(courseId).style.color = "#e7983d"; // highlight hovered course orange
          document.getElementById(courseId).style.textShadow =
            "1px 1px 10px white";
          // check here if a class has a prereq from the db
          if (response.prereq) {
            console.log(response.prereq);

            prereqClassArray = response.prereq.split(", "); // grab all prereqs
            // console.log(`Array: ${prereqClassArray}`);   // helper printout

            // cycle through the array and highlight the prereq classes
            for (let i = 0; i < prereqClassArray.length; i++) {
              // console.log(`Element at i: ${prereqClassArray[i]}`);

              const prereqElement = document.getElementById(
                prereqClassArray[i]
              );

              if (prereqElement) {
                prereqElement.style.color = "#48f44d";
                prereqElement.style.textShadow = "1px 1px 10px white";
              }
            }
          }

          // Set the dialog box content to the course info
          dialog.html(
            '<h5 id="course-name">Course Name</h5>' +
              response.name +
              "<br><br><strong>Description:</strong><br>" +
              response.description +
              '<br><br><strong id="prereqID">Prerequisites:</strong><br><br>' +
              response.prereq
          );

          // Show the dialog box
          dialog.show();
        } else {
          document.getElementById("resc-lnks").style.display = "unset";
          dialog.hide();
        }
      },
      error: function (xhr, status, error) {
        console.error("Error loading course info: " + error);
      },
    });
  });

  // Add a mouseout event listener to hide the dialog box when the user moves the mouse away from a course heading
  $(".class-list-item").mouseout(function () {
    dialog.hide();
    for (let i = 0; i < prereqClassArray.length; i++) {
      const prereqElement = document.getElementById(prereqClassArray[i]);
      // console.log(`Element at i: ${prereqClassArray[i]}`);
      if (prereqElement) {
        prereqElement.style.color = "white";
        prereqElement.style.textShadow = "none";
      }
    }
    document.getElementById(globalCourseID).style.color = "white";
    document.getElementById(globalCourseID).style.textShadow = "none";
    document.getElementById("resc-lnks").style.display = "unset";
  });
});

function playSound() {
  // Create an audio element and set its source to the sound file
  var audio = new Audio("");
  // Play the audio file
  audio.play();
}
