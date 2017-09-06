function alert_query_will_be_submitted(){
  alert('Your query will be submitted. Please press OK to confirm and continue');
}

function loading(){
    try{
      var x = document.getElementById('container');
      var y = document.getElementById('loading');
      if(x.style.display == 'none') {
        x.style.display = 'block';
      } else {
        y.style.display = 'block';
        x.style.display = 'none';
      }
    } catch(e) {
      console.log("nope :(");
    }
}
