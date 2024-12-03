<template>
  <header class="bg-warm-gray-500 text-warm-gray-700 p-4 flex items-center shadow-sm">
    <img src="@/assets/logo.png" alt="Poem Genie Logo" class="h-8 mr-3">
    <router-link to="/" class="text-xl font-bold tracking-wider no-underline">
      <span class="text-primary-800">POEM</span>
      <span class="text-neutral-800">GENIE</span>
    </router-link>
  </header>
</template>

<script lang="ts">
export default {
  name: 'AppHeader'
}
</script>
