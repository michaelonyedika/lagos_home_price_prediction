// function getPropertyValue() {
//     var uiProperty_type = document.getElementsByName("uiProperty_type");
//     for(var i in uiProperty_type) {
//       if(uiProperty_type[i].checked) {
//           return parseInt(i)+1;
//       }
//     }
//     return -1; // Invalid Value
//   }
  
  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    // var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    // var bathrooms = getBathValue();
    var location = document.getElementById("uiLocations");
    var property_type = document.getElementById("uiProperty_type");
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    // var url = "http://127.0.0.1:5000/predict_home_price"; //Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        // total_sqft: parseFloat(sqft.value),
        bhk: bhk,
        // bath: bathrooms,
        location: location.value,
        property_type: property_type.value,

    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h4>" + data.estimated_price.toString() + " Naira</h4>";
        console.log(status);
    });
  }
  
  function onPageLoad_location() {
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;

            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });
  }

  function onPageLoad_property() {
    console.log( "document loaded" );
    // var url = "http://127.0.0.1:5000/get_property_type"; // Use this if you are NOT using nginx which is first 7 tutorials
    var url = "/api/get_property_type"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_property_type request");
        if(data) {
            var property_type = data.property_type;

            var uiProperty_type = document.getElementById("uiProperty_type");
            $('#uiProperty_type').empty();
            for(var i in property_type) {
                var opt = new Option(property_type[i]);
                $('#uiProperty_type').append(opt);
            }
        }
    });
  }


  

  
  window.onload = function() {
    onPageLoad_property();
    onPageLoad_location();
  };