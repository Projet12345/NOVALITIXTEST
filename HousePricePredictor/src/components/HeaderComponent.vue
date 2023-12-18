<template>
   <v-app-bar
        color="white"
      >
        

        <template v-slot:prepend >
          <v-btn to="/" color="primary">Home</v-btn>
            <!-- <v-img @click="this.$router.push('/')"  style="cursor: pointer;"  width="200" src="/../../images/novalitix.png"></v-img> -->
        </template>


        <v-spacer></v-spacer>

        

        <v-btn to="/house-prediction" color="primary">
          Project 1
        </v-btn>

        <v-btn to="/sentiment-analys" color="primary">
          Project 2
        </v-btn>
      </v-app-bar>
</template>

<script setup>

</script>

<style>

</style>