import { createRouter, createWebHistory } from 'vue-router';


// dashboard
import index from '../views/MainView.vue';
import prediction from '../views/HousePrediction.vue';
import analys from '../views/SentimentAnalys.vue';







// Créez votre instance de routeur
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: index },
    { path: '/house-prediction', component: prediction },
    { path: '/sentiment-analys', component: analys },
 


  ],
});

export default router;