import Vue from 'vue';
import Router from 'vue-router';
import Notes from '../components/Notes.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Notes',
      component: Notes,
    }
  ],
});
