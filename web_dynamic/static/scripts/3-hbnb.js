$(document).ready(() => {
    const mydict = {};
    $('input[type="checkbox"]').change(function () {
      if (this.checked) {
        mydict[$(this).attr('data-id')] = $(this).attr('data-name');
      } else {
        delete mydict[$(this).attr('data-id')];
      }
      $('DIV.amenities H4').text(Object.values(mydict).join(', '));
    });
    $.get('http://0.0.0.0:5001/api/v1/status/', (data) => {
      if (data.status === 'OK') {
        $('DIV#api_status').addClass('available');
      } else {
        $('DIV#api_status').removeClass('available');
      }
    });
  
    $.ajax({
      url: 'http://0.0.0.0:5001/api/v1/places_search/',
      type: 'POST',
      data: {},
      contentType: 'application/json',
      dataType: 'json',
      success: function (data) {
        for (let i = 0; i < data.length; i++) {
          $('section.places').append(addPlace(data[i]));
        }
      }
    });
  
    function addPlace (place) {
      return `
        <article>
        <h2>${place.name}</h2>
        <div class="title_box">
        <div class="price_by_night">$${place.price_by_night}
        </div>
        </div>
        <div class="information">
        <div class="max_guest">
        ${place.max_guest} Guest
        </div>
        <div class="number_rooms">${place.number_rooms} Bedroom
        </div>
        <div class="number_bathrooms">${place.number_bathrooms} Bathroom
        </div>
        </div>
        <div class="description">${place.description}
        </div>
        </article>
        `;
    }
  });