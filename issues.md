---
layout: page
title: Segnalazioni
permalink: /issues/
---
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.0/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.0.0/dist/leaflet.js"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css" />
<script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.min.js"></script>
<link rel="stylesheet" href="{{ site.url }}/css/Control.Geocoder.css" />
<script src="{{ site.url }}/js/Control.Geocoder.js"></script>


<div class="row">
<div class="text-center">
  <span class="col-xs-12 col-sm-6">
	  <a href="#raccolte-fondi" class="btn btn-warning btn-lg col-xs-12 mb-15" role="button">Raccolte fondi</a>
	</span>
   <span class="col-xs-12 col-sm-6">
	  <a href="#notizie" class="btn btn-warning btn-lg col-xs-12 mb-15" role="button">Notizie</a>
	</span>
  <span class="col-xs-12 col-sm-6">
    <a href="#servizi-e-iniziative-solidali" class="btn btn-success btn-lg col-xs-12 mb-15" role="button">Servizi e iniziative solidali</a>
	</span>
  <span class="col-xs-12 col-sm-6">
    <a href="#iniziative-culturali-e-ricreative" class="btn btn-success btn-lg col-xs-12 mb-15" role="button">Iniziative culturali e ricreative</a>
	</span>
  <span class="col-xs-12 col-sm-6">
    <a href="#consegne-e-commissioni" class="btn btn-success btn-lg col-xs-12 mb-15" role="button">Consegne e commissioni</a>
	</span>
  <span class="col-xs-12 col-sm-6">
    <a href="#supporto-psicologico" class="btn btn-success btn-lg col-xs-12 mb-15" role="button">Supporto psicologico</a>
  </span>
</div>
</div>



<div class="row"><div class="col-md-12 col-sm-12 col-xs-12"> <div id="map" style="height: 600px;"></div> </div> </div>

---
# Raccolte fondi
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Raccolte fondi'"%}
{% for member in filteredissues %}
<div class="panel-body">
<div class="list-group-item">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="list-group-item-heading">{{member.title}}</h4></a>
<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " "}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>

---
# Notizie
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Notizia'" %}
{% for member in filteredissues %}
<div class="panel-body">
<div class="list-group-item">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="list-group-item-heading">{{member.title}}</h4></a>
<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " "}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>

---
# Servizi e iniziative solidali
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Servizi e iniziative solidali private' or member.issue.labels contains 'Servizi e iniziative solidali pubbliche'"%}
{% for member in filteredissues %}
<div class="panel-body">
<div class="list-group-item">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="list-group-item-heading">{{member.title}}</h4></a>
<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " "}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>

---
# Iniziative culturali e ricreative
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Attivita culturali e ricreative'" %}
{% for member in filteredissues %}
<div class="panel-body">
<div class="list-group-item">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="list-group-item-heading">{{member.title}}</h4></a>
<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " "}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>

---
# Consegne e commissioni
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Consegne e commissioni'"%}
{% for member in filteredissues %}
<div class="panel-body">
<div class="list-group-item">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="list-group-item-heading">{{member.title}}</h4></a>
<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " "}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>

---
# Supporto psicologico
<div class="panel-group">
{% assign filteredissues = site.data.issuesjson | where: "state","open" | where_exp: "member","member.issue.labels contains 'Supporto psicologico'"%}
{% for member in filteredissues %}
<div class="panel-body">
<div class="list-group-item">
<a href="{{site.url}}/issues/{{member.number}}"><h4 class="list-group-item-heading">{{member.title}}</h4></a>
<p class="list-group-item-text">{{member.issue.data.descrizione|markdownify}}</p>
<dl class="row">
{% for item in member.issue.data %}
{% if item[1] != blank %}
<dt class="col-sm-3">{{item[0] | replace: "_", " "}}</dt>
<dd class="col-sm-9">{{item[1] | newline_to_br | auto_link}}</dd>
{% endif %}
{% endfor %}
</dl>
</div>
{% include social-share-issue.html %}
</div>
{% endfor %}
</div>

{% assign filteredissues = site.data.issuesjson | where: "state","open" "%}
<script>
var markerList=[];
{% for member in filteredissues %}
{% if member.issue.data.Posizione != blank %}
{% assign coordinate = member.issue.data.Posizione | split: ' ' %}
markerList.push([{{coordinate[0]}}, {{coordinate[1]}}, "{{member.title|uri_escape}}", "{{ member.number }}", ""]);
{% endif %}
{% endfor %}

var alloggiMarker = L.AwesomeMarkers.icon({
icon: 'home',
prefix: 'fa',
markerColor: 'green'
});
var fabbisogniMarker = L.AwesomeMarkers.icon({
icon: 'child',
prefix: 'fa',
markerColor: 'blue'
});
var notizieutiliMarker = L.AwesomeMarkers.icon({
icon: 'newspaper-o',
prefix: 'fa',
markerColor: 'orange'
});
var donazioniMarker = L.AwesomeMarkers.icon({
icon: 'handshake-o',
prefix: 'fa',
markerColor: 'red'
});
var raccoltefondiMarker = L.AwesomeMarkers.icon({
icon: 'money',
prefix: 'fa',
markerColor: 'blue'
});

// initialize the map
var map = L.map('map')

// create the tile layer with correct attribution
var osmUrl='{{site.tile_map}}';
var osmAttrib='&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, Tiles courtesy of <a href="http://leafletjs.com/" target="_blank">Leaflet</a>';
var osm = new L.TileLayer(osmUrl, {minZoom: 5, maxZoom: 19, attribution: osmAttrib});


var sumLat = 0.;
var sumLon = 0.;

for (var i=0; i<markerList.length; i++) {
    var lat = markerList[i][0];
    var lon = markerList[i][1];
    var popupText = markerList[i][2];
    var popupURL = markerList[i][3];
    var type = markerList[i][4]

        if (!isNaN(lat) && !isNaN(lon)) {
            var markerLocation = new L.LatLng(lat, lon);
            var marker = new L.Marker(markerLocation);

            map.addLayer(marker);

            marker.bindPopup("<a href=\"" + popupURL + "\">" + decodeURI(popupText) + "</a>");

            sumLat += lat;
            sumLon += lon;
        }
}

map.addLayer(osm).setView([42.629381, 13.288372], 5);
var geocoder = L.Control.geocoder({collapsed:false,placeholder:"Cerca...",
        defaultMarkGeocode: false, geocodingQueryParams: { countrycodes: "it" },
        })
.on('markgeocode', function(e) {
        var latlon=e.geocode.center;
        $("#lat").html(latlon.lat);
        $("#lng").html(latlon.lng);
        var marker = new L.Marker(markerLocation);
        map.addLayer(marker);
        })
.addTo(map);

</script>
