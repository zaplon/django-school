// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import App from './App'
import router from './router'
import FullCalendar from 'vue-full-calendar'
import VueGoodTable from 'vue-good-table'

window.jQuery = window.$ = require('jquery')

Vue.use(FullCalendar)
Vue.use(BootstrapVue)
Vue.use(VueGoodTable)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App
  }
})
