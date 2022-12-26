<template>
  <div id="app">

    <router-view/>
    <div>
      <TodayRecommended/>
      <PersonalRecommended/>
    </div>
    <div>
      <AddTheme/>
    </div>
  </div>
</template>

<script>
import TodayRecommended from '@/views/Home/TodayRecommended.vue'
import PersonalRecommended from '@/views/Home/PersonalRecommended.vue'
import AddTheme from '@/components/theme/AddTheme.vue'
export default {
  name: 'App',
  components: {
    TodayRecommended,
    PersonalRecommended,
    AddTheme,
  }
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
