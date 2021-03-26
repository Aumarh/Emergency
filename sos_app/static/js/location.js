
let map, infoWindow;

function initMap(getCurrent) {
  map = new google.maps.Map(document.getElementById("map"), {

    center: { lat: -34.397, lng: 150.644 },
    zoom: 6,

  });
  if (getCurrent){
      if (navigator.geolocation) {

        navigator.geolocation.getCurrentPosition(
          (position) => {
            const pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            };
            const url = location.href.split("/");
            const issue = document.getElementById('issue').textContent
            const user_id = url[url.length-1]

              localStorage.setItem("user", user_id);
              localStorage.setItem("issue", issue);

            $.ajax({
                type: 'POST',
                url: '/location/',
                dataType: "json",
                data : {
                    position: JSON.stringify(pos),
                    user: JSON.stringify(localStorage.getItem('user')),
                    issue: JSON.stringify(localStorage.getItem('issue'))

                },
                headers: {"Authorization": localStorage.getItem('user'), "issue" :localStorage.getItem('issue')},
  
            }),
  
            infoWindow.setPosition(pos)
            infoWindow.setContent("Location found.");
            infoWindow.open(map);
            map.setCenter(pos);
          },
          () => {
            handleLocationError(true, infoWindow, map.getCenter());
          }
        );
      } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
      }
  }}


