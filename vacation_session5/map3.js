const getPlace = () => {
  let keyword = document.getElementById("text").value;
  ps.keywordSearch(keyword, placesSearchCB);
};

let mapContainer = document.getElementById("map"), // 지도를 표시할 div
  mapOption = {
    center: new kakao.maps.LatLng(37.566826, 126.9786567), // 지도의 중심좌표
    level: 3, // 지도의 확대 레벨
  };

// 지도를 생성합니다
let map = new kakao.maps.Map(mapContainer, mapOption);

// 장소 검색 객체를 생성합니다
let ps = new kakao.maps.services.Places();

// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB(data, status, pagination) {
  if (status === kakao.maps.services.Status.OK) {
    // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
    // LatLngBounds 객체에 좌표를 추가합니다
    let bounds = new kakao.maps.LatLngBounds();
    for (let i = 0; i < data.length; i++) {
      displayMarker(data[i]);
      let thismarker = displayMarker(data[i]);
      displayOverlay(thismarker, data[i]);
      // let thisoverlay = displayOverlay(thismarker, data[i]);
      bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
    }

    // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
    map.setBounds(bounds);
  }
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {
  // 마커를 생성하고 지도에 표시합니다
  var marker = new kakao.maps.Marker({
    map: map,
    position: new kakao.maps.LatLng(place.y, place.x),
  });

  return marker;
}

function closeOverlay() {
  current_overlay.setMap(null);
}

function displayOverlay(marker, place) {
  var content =
    '<div class="wrap">' +
    '    <div class="info">' +
    '        <div class="title">' +
    place.place_name +
    '            <div class="close" onclick="closeOverlay()" title="닫기"></div>' +
    "        </div>" +
    '        <div class="body">' +
    '            <div class="desc">' +
    '                <div class="ellipsis">' +
    place.address_name +
    "</div>" +
    '                <div class="jibun ellipsis"> 전화번호 : ' +
    place.phone +
    "</div>" +
    "                <div><a href=" +
    place.place_url +
    ' target="_blank" class="link">카카오맵 연결</a></div>' +
    "            </div>" +
    "        </div>" +
    "    </div>" +
    "</div>";

  // 마커 위에 커스텀오버레이를 표시합니다
  // 마커를 중심으로 커스텀 오버레이를 표시하기위해 CSS를 이용해 위치를 설정했습니다
  var overlay = new kakao.maps.CustomOverlay({
    content: content,
    map: map,
    position: marker.getPosition(),
  });

  // 마커를 클릭했을 때 커스텀 오버레이를 표시합니다
  kakao.maps.event.addListener(marker, "click", function () {
    //current overlay를 전역변수로 설정
    if (typeof current_overlay !== "undefined") {
      current_overlay.setMap(null);
    }
    overlay.setMap(map);
    current_overlay = overlay;
  });
  overlay.setMap(null);
  // 커스텀 오버레이를 닫기 위해 호출되는 함수입니다

  return overlay;
}
