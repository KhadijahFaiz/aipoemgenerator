<template>
  <div class="min-h-screen bg-gradient-to-r from-primary-100 via-secondary-100 to-primary-200 animate-gradient-x flex flex-col items-center justify-center p-4">
    <div class="bg-white bg-opacity-90 rounded-lg shadow-2xl p-8 max-w-2xl w-full mb-16 text-center">
      <h1 class="text-6xl font-extrabold text-gradient mb-6">
        POEM GENIE
      </h1>
      <p class="text-2xl text-gray-700 mb-8">
        Your Favorite AI Poem Generator
      </p>
      <div class="space-y-6 mb-12">
        <p class="text-lg text-gray-600">
          Welcome to Poem Genie, where artificial intelligence meets the art of poetry. 
          Our cutting-edge AI technology crafts unique, inspiring poems tailored to your inputs.
        </p>
        <p class="text-lg text-gray-600">
          Whether you're seeking inspiration, a personalized gift, or simply curious about AI-generated art, 
          Poem Genie is here to spark your imagination.
        </p>
      </div>
      <router-link 
        to="/generate" 
        class="btn-primary inline-block text-lg px-8 py-3 rounded-full transition-transform hover:scale-105"
      >
        Try Poem Genie Now 🧞‍♂️
      </router-link>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl w-full">
      <div class="bg-white bg-opacity-75 rounded-lg p-6 shadow-lg">
        <h3 class="text-xl font-semibold mb-3 text-primary-600">Instant Creativity</h3>
        <p class="text-gray-600">Get unique poems in seconds, inspired by your own ideas.</p>
      </div>
      <div class="bg-white bg-opacity-75 rounded-lg p-6 shadow-lg">
        <h3 class="text-xl font-semibold mb-3 text-secondary-600">Endless Inspiration</h3>
        <p class="text-gray-600">Explore a world of poetic possibilities with our AI.</p>
      </div>
      <div class="bg-white bg-opacity-75 rounded-lg p-6 shadow-lg">
        <h3 class="text-xl font-semibold mb-3 text-primary-600">Perfect for Any Occasion</h3>
        <p class="text-gray-600">From love poems to nature-inspired verses, we've got you covered.</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HomeView',
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

* {
  font-family: 'Poppins', sans-serif;
}

.text-gradient {
  @apply bg-clip-text text-transparent bg-gradient-to-r from-primary-500 to-secondary-500;
}
</style>