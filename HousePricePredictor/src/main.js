import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router  from './router/router';


// Vuetify
import 'vuetify/styles'

import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import colors from 'vuetify/lib/util/colors'
import '@mdi/font/css/materialdesignicons.css';
import axios from 'axios'
import VueAxios from 'vue-axios'
// Translations provided by Vuetify
const vuetify = createVuetify({
  components: {
    ...components,
  },
  directives,

  theme: {
    themes: {
      light: {
        dark: false,
        colors: {
         primary:"#066aab",
         secondary:"#353666",
       } },

    },
  },
})
const app = createApp(App);
app.use(vuetify).use(router).use(VueAxios, axios).mount('#app')