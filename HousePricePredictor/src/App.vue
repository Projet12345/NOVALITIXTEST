<template>
  <v-app fluid>
    <HeaderComponent/>
    <v-main class="height:100%">
      <router-view></router-view>
      
    </v-main>
    <FooterComponent/>
  </v-app>

</template>
<script setup>
import FooterComponent from './components/FooterComponent.vue';
import HeaderComponent from './components/HeaderComponent.vue';

</script>