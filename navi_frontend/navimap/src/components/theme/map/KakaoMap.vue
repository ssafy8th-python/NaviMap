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
        let kakao = window.kakao
        console.log(this.$refs.map)

        const container = this.$refs.map
        // const options = {
        //     center: new kakao.maps.LatLng(35.193681, 126.825577, 16),
        //     level: 5,
        // }
        const {center, level} = this.options
        const mapInstance = new kakao.maps.Map(container, {
            center: new kakao.maps.LatLng(center.lat, center.lng),
            level: level,
        })
        console.log(mapInstance)
    }

}
</script>

<style>
.kmap {
    width: 100%;
    height: 600px;
}

</style>