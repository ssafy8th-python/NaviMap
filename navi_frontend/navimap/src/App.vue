<template>
  <div id="app">

    <!-- navbar -->
    <!-- <nav class="navbar navbar-light bg-light">
    <div class="container">
      <a class="navbar-brand" href="#">
      <img src="@/assets/Navimap_logo.png" style="width:150px; text-align:left;">      </a>
    </div>
    </nav> -->
    <nav class="navbar navbar-expand-lg bg-body-tertiary">

  <div class="container-fluid">
    <a class="navbar-brand" href="#"><img src="@/assets/Navimap_logo.png" style="width:150px; text-align:left;"></a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
      <ul class="navbar-nav" >
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">π ν</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">π¦νλ§λ³΄κΈ°</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">πΌλμ νλ§</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">βοΈλ§μ΄νμ΄μ§</a>
        </li>
        <li class="nav-item">
          <span class="nav-link" @click="kakaoLogin">πλ‘κ·ΈμΈ</span>
        </li>

        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown link
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li> 
      </ul>
    </div>
  </div>
</nav>


    <!-- νμ΄ν -->
    <h1 style="text-align:center; font-size:100px;"> λλΉμ§λ </h1>
    <h4 style="text-align:center;"> λλ§μ λΉλ° μ§λ </h4>
    <!-- κ²μμ°½ -->
    <SearchBar/>

    <!-- <router-view></router-view> -->

    <!-- μΆμ²μΉ΄λλ€ -->
    <v-row>
      <TodayRecommended/>
      <PersonalRecommended/>
    </v-row>
    <br>
    <v-divider></v-divider>      
          </ul>
        </div>
      </div>
    </nav>
    <router-view></router-view>

    
    <!-- νλ§ μΆκ° λ²νΌ -->
    <div>
      <v-btn
        id="show-btn" @click="$bvModal.show('bv-modal-example')"
        v-b-modal.modal-center
        class="mx-2"
        fab
        dark
        style="position:fixed; left:92%; right:0px; bottom:5%;"
      >
        <v-icon>
            mdi-plus
        </v-icon>
      </v-btn>

      <!-- νλ§ μμ± λͺ¨λ¬ -->
      <ThemaCreateModal/>
      
      <!-- λ§¨ μλ‘ λ²νΌ -->
      
      
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import ThemaCreateModal from '@/views/Home/ThemaCreateModal.vue'

export default {
  name: 'App',
  components: {
    ThemaCreateModal,

  },
  methods:{
    kakaoLogin(){
      axios({
        method:'get',
        url:"http://127.0.0.1:8000/api/v1/accounts/kakao/login/getcode/",
      })
        .then((res)=>{
          window.location.href=res.data.kakao_login_url
        })
        .catch((err)=> {console.log(err)})
    }
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
