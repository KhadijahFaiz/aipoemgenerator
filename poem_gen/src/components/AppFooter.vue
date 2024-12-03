<template>
  <footer class="bg-gray-800 text-white p-4 text-center" role="contentinfo">
    <p>&copy; {{ currentYear }} Poem Genie. All rights reserved.</p>
  </footer>
</template>

<script lang="ts">
export default {
  name: 'AppFooter',
  computed: {
    currentYear() {
      return new Date().getFullYear()
    }
  }
}
</script>

