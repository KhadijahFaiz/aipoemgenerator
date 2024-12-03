<template>
  <div id="app">
    <AppHeader />
    <NavBar />
    <router-view />
    <AppFooter />
  </div>
</template>

<script lang="ts">
import AppHeader from './components/AppHeader.vue';
import AppFooter from './components/AppFooter.vue';
import NavBar from './components/NavBar.vue';

export default {
  name: 'App',
  components: {
    AppHeader,
    NavBar,
    AppFooter
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #f7f7f7; /* Lighter gray background for the app */
}

#app > header {
  background-color: #c5deea; /* Original background color for the header */
}
</style>


