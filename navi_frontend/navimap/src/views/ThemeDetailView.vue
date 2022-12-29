<template>
    <div>
        <h3>ThemeDetailView</h3>
        
        <KakaoMap class="kmap" :options="mapOption"/>
    </div>
</template>

<script>
import KakaoMap from '@/components/theme/map/KakaoMap'

export default {
    name:'ThemeDetailView',
    components: {
        KakaoMap
    },
    data() {
        return{
            mapOption:{
                center: {
                    lat: 35.193681,
                    lng: 126.825577,
                },
                level : 8
            }
        }
    },
    mounted() {
    
    },

}
</script>

<style scoped >


</style>