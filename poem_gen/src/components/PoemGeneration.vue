<template>
    <div>
      <input v-model="prompt" placeholder="Enter your prompt" />
      <button @click="generatePoem">Generate Poem</button>
      <div v-if="poem">
        <h2>Generated Poem:</h2>
        <p>{{ poem }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        prompt: '',
        poem: ''
      };
    },
    methods: {
      async generatePoem() {
        try {
          const response = await fetch('http://localhost:5001/api/generate-poem', { // Update URL as necessary
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: this.prompt })
          });
          const data = await response.json();
          this.poem = data.poem;
        } catch (error) {
          console.error('Error generating poem:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Your styles here */
  </style>
  