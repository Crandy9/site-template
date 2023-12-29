import { createStore } from 'vuex'

export default createStore({
  state: {
    language: localStorage.getItem("language") || process.env.VUE_APP_I18N_LOCALE || 'en',

  },
  getters: {
    getLanguage: (state) => state.language

  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
