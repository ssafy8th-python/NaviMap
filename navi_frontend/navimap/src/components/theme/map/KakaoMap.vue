<template>
  <div ref="map">

  </div>
</template>

<script>
export default {
    name:'KakaoMap',
    props:{
        options: Object
    }, 
    mounted() {
        if (!window.kakao || !window.kakao.maps){
            const script = document.createElement("script");
            script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${process.env.VUE_APP_KAKAOMAP_KEY}`;

            script.addEventListener("load", () => {
                kakao.maps.load(this.initMap);
            });
            document.head.appendChild(script);
        } else {
            this.initMap();
        }
        


        
    },
    methods: {
        initMap() {
            
        

            const container = this.$refs.map
            const {center, level} = this.options
            const mapInstance = new kakao.maps.Map(container, {
                center: new kakao.maps.LatLng(center.lat, center.lng),
                level: level,
            })
            console.log(mapInstance)

        }
    }

}
</script>

<style>
.kmap {
    width: 100%;
    height: 600px;
}

</style>